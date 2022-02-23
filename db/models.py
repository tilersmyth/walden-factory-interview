from datetime import datetime
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class ProductModel(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    unique_code = Column(Integer, unique=True, nullable=False)
    packages = relationship("PackageModel")

class PackageModel(Base):
    __tablename__ = 'packages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cut_id = Column(String, unique=True, nullable=False)
    lot_code = Column(Integer, nullable=False)
    weight = Column(Float, nullable=False)
    is_validated = Column(Boolean, default=False, nullable=False)
    product_code = Column(Integer, ForeignKey('products.unique_code'), nullable=False)
    created = Column(DateTime, default=datetime.utcnow)

    @property
    def barcode(self):
        weight = '{:04d}'.format(int(self.weight*100))
        return f'{self.product_code}{self.lot_code}{weight}{self.cut_id}'