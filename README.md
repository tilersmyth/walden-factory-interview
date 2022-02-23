# Tyler's Response

## Local Requirements

- Pipenv
- SQLite

## Getting Started

1. `cd factory-interview`
2. `pipenv shell` (Activate Python environment)
3. `pipenv install` (Install requirements - Alembic, SQLAlchemy)
4. `alembic upgrade head` (Run latest migration to setup/seed db)
5. `python labeler.py`

## Part 1b - Recommendations

### Maintenance

- Agile CI deployment strategy
- Tkinter GUI versioning
- Dedicated remote DB instance

### Features

- Simple form validation, input masking
- Barcode scanner at packaging step to validate package
- Collect other data points (operator, timing, etc)

## Resources

- https://www.youtube.com/watch?v=nt5sSr1A_qw&t=929s (Setting up Alembic with SQLAlchemy)
- https://docs.sqlalchemy.org/en/14/
- https://alembic.sqlalchemy.org/en/latest/

## <br />

---

# Manufacturing Software Engineer Takehome

# Instructions

This challenge is a simplified representation of a project you may encounter at Walden.. You are welcome to consult outside sources (including me, please ask clarification questions!), but please list any reference materials that you use. Your answer will be the starting point for a larger discussion during the technical screen. Keep in mind that the goal of this exercise is for you to demonstrate how you approach problems. Getting to the ‘correct’ answer is less important than explaining your process, laying out your assumptions, and being able to defend your decisions.

Using the repo:

- you may need to install tkinter using pip or an equivalent package manager, depending on which version of python you install
- you are welcome to use other packages, but be sure to document the setup process for others to use the repo

# Overview

Your assignment is to complete a packing application started by another engineer. This tool will be used by our processors as they label meat products from one of our processors. The application is a proof of concept idea consisting of a form where operators provide information about the lot they are processing, and data entry from a digital scale (omitted for the purposes of this exercise). The proposed workflow is as follows:

- Setup:

  - line supervisor starts the application on a laptop
  - line supervisor sets the product type from a list of options
  - line supervisor sets the lot code, which should be a 5 digit julian date code corresponding to the date the items were cut (may not be the day the items are labeled)

- Normal operator flow
  - Operator takes a packaged cut of product, and places it on the scale
  - Scale reads input and send to the application (omitted for simplicity, replaced with a user-entered text box)
  - Operator checks reading, then triggers label generation using an on-screen button (omitted for simplicty, replaced with a dialog window)
  - Operator affixes printed label onto the package, and moves the package to a secondary assembly line, where labeled packages are packed into cases

## Label Convention

Each label contains a barcode, which encodes information about the package: 1. A five (5) digit product code 2. A five (5) digit lot code, formed as a julian date (YYDDD) 3. A four (4) digit representation of the weight, including 2 decimal places (4.2 -> 0420) 4. A non-repeating five (5) digit serial that uniquely identifies the package

Assume that the weigh/label process is error prone, and operators have a tendency to double-print labels or misweigh labels. Therefore, the system needs a way to mark which labels correspond to real product. A downstream application (omitted for simplicity) guides operators through scanning packages into a case, weighing the case, and printing a label for the case.

# Part 1a

Your task is to design and implement a schema to store information from the packing process, and write an implementation for reading and writing from the database. You are welcome to use any tools, databases, or libraries you deem appropriate including postgres, mysql, alembic, SQLAlchemy, redis, etc. Don't worry about provisioning a fully 'production ready' system, but you should be able to sketch how you would scale up your solution to a production enivornment.

Your design should meet the following requirements:

- Multiple instances of the application can maintain connections to the database, and simultaneously read and write data
- Allows an instance of the program to assign a unique barcode to each cut
- Logs captured weights to a structured data format
- Specifies a convention for downstream applications to annotate labels with a status (whether or not they have been validated at case packing)

# Part 1b

This proof of concept application is obviously not ready for release. Please prepare some recommendations for steps you would take to facilitate maintaining this application long term. Your list can be fairly brief, covering major missing components, and proposing a basic structure to address each. We will discuss your recommendations during the second part of the exercise, so you need only include as much detail as necessary to illustrate your point. Your response to this question could be as simple as a bulleted list, or include psuedocode, sample code, or examples of similar work.

# Part 2

The second part of the exercise is a video call where we will discuss your solution. Be prepared to speak to your design and your recommendations for productionizing the script. As part of the challenge, we may ask you to change small portions of your code, or implement additional functionality.
