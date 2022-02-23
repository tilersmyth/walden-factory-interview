from tkinter import messagebox, ttk
import tkinter as tk
import random 
import re
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import PackageModel, ProductModel

class LabelerApplication(object):

    def __init__(self, root):
        self.root = root

        # Connect to db
        self.db_session = sessionmaker(bind=create_engine('sqlite:///db/labeler.db'))
        self.all_products = []

        self.build_ui(self.root)

    def build_ui(self, master):
        self.tkobject = tk.Frame(master)

        self.tkobject.rowconfigure(0, weight=0)
        self.tkobject.rowconfigure(1, weight=0)
        self.tkobject.rowconfigure(2, weight=0)
        self.tkobject.rowconfigure(3, weight=1)
        self.tkobject.rowconfigure(4, weight=1)

        self.tkobject.columnconfigure(0, weight=0)
        self.tkobject.columnconfigure(1, weight=1)

        # Title
        ttk.Label(self.tkobject,
                 text="Package Labeler").grid(row=0,
                                              column=0,
                                              sticky='w')

        # product selector
        self.product_var = tk.StringVar()
        self.product_var.set('')
        self.product_picker = ttk.Combobox(self.tkobject,
                                 textvar=self.product_var,
                                 width=20,
                                 font=('Arial', 16))

        with self.db_session() as session:
            self.all_products = session.query(ProductModel).all()

            product_names = []
            for product in self.all_products:
                product_names.append(product.name)

        self.product_picker['values'] = product_names
        self.product_picker.grid(row=1, column=0, columnspan=2)

        # lot entry (user manually types)
        ttk.Label(self.tkobject,
                 text="Lot Number:", 
                 font=('Arial', 14, 'bold'),
                 width=16).grid(row=2,
                                column=0,
                                sticky='w')
        self.lot_var = tk.StringVar()
        self.lot_entry = ttk.Entry(self.tkobject,
                                   textvariable = self.lot_var)
        self.lot_entry.grid(row=2, column=1)

        # weight entry (user manually types)
        ttk.Label(self.tkobject,
                 text="Measured Weight:", 
                 font=('Arial', 14, 'bold'),
                 width=16).grid(row=3,
                                column=0,
                                sticky='w')
        self.weight_var = tk.StringVar()
        self.weight_entry = ttk.Entry(self.tkobject,
                                   textvariable = self.weight_var)
        self.weight_entry.grid(row=3, column=1)

        # Print button
        ttk.Button(self.tkobject, text='PRINT LABEL', command = self.generate_label).grid(row=4,
                                                                                          column=0,
                                                                                          columnspan=2)
        self.tkobject.grid(row=0, column=0)

    def get_product(self):
        product_name = self.product_var.get()
        try:
            product = next(product for product in self.all_products if product.name == product_name)
            product_code = str(product.unique_code)
        except StopIteration:
            messagebox.showinfo('WARNING', 'Unable to find product: {}'.format(product_name))
            self.product_var.set('')
            return None
        return product_code

    def get_lot_code(self):
        lot_code = self.lot_var.get()
        lot_code = re.sub('[^0-9]','', lot_code)
        if len(lot_code) < 5:
            messagebox.showinfo('WARNING', 'Lot code must be a 5 digit number: {}'.format(lot_code))
            self.lot_var.set('')
            return None
        return lot_code

    def get_weight(self):
        """
        Normally this would be connected via RS-232 to a scale. For the purposes of this exercise, 
        assume that the weight is inputted manually
        """
        weight = self.weight_var.get()
        try:
            weight = float(weight)
        except ValueError:
            messagebox.showinfo('WARNING', 'Weight must be a float: {}'.format(weight))
            self.weight_var.set('')
            return None

        return weight

    def generate_cut_id(self):
        with self.db_session() as session:
            package_count = session.query(PackageModel).count()
            return str(package_count + 1).zfill(5) 

    def create_package(self, cut_id, lot_code, weight, product_code):
        package = PackageModel(
            cut_id=cut_id, 
            lot_code=lot_code, 
            weight=weight, 
            product_code=product_code
        )

        with self.db_session() as session:
            session.add(package)
            session.commit()
            session.refresh(package)
    
        return package


    def generate_label(self, *args):
        """
        Generate a barcode based on inputs from UI an database. Send the label to the printer
        """

        product_code = self.get_product()
        if product_code == None:
            return

        lot_code = self.get_lot_code()
        if lot_code == None:
            return
            
        weight = self.get_weight()
        if weight == None:
            return

        cut_id = self.generate_cut_id()

        package = self.create_package(cut_id, lot_code, weight, product_code)

        messagebox.showinfo('INFO', 'Printing barcode: {}'.format(package.barcode))
        self.weight_var.set('')
        return 


def main():
    root = tk.Tk()
    labeler = LabelerApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()

