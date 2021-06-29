#Manufacturing Software Engineer Takehome

# Instructions
This problem is a simplified representation of a problem you may encounter in this role.. You are welcome to consult outside sources (including me, please ask clarification questions!), but please list any reference materials that you use. Your answer will be the starting point for a larger discussion during the technical screen. Keep in mind that the goal of this exercise is for you to demonstrate how you approach problems. Getting to the ‘correct’ answer is less important than explaining your process, laying out your assumptions, and being able to defend your decisions.

Using the repo:
- Please fork the repo and do all of your work in a branch off master
- you may need to install tkinter using pip or an equivalent package manager, depending on which version of python you install
- you are welcome to use other packages, but be sure to create a requirements.txt file if you do!

# Overview
Your assignment is to complete a packing application started by another engineer. This tool will be used by our processors as they label package and label individual cuts of meat. The application is a proof of concept idea consisting of a form where operators provide information about the lot they are processing, and an RS-232 connection to a scale for measuing package weights (omitted for the purposes of this exercise). The propose workflow is as follows:
- Setup: 
    - line supervisor starts the application for each packing line (assume 5 total)
    - line supervisor sets the product type from a list of options
    - line supervisor sets the lot code, which should be a 5 digit julian date code corresponding to the date the items were cut (may not be the day the items are labeled)
- Normal operator flow
    - Operator takes a packaged cut, and places it on the scale
    - Scale reads input and send to the application (omitted for simplicity, replaced with a text box)
    - Operator checks reading, then triggers label generation using the print button
    - Operator places printed label onto the package, and moves the package to a secondary flow, where labeled packages are packed into cases

Assume that this process is somewhat error prone, and operators have a tendency to double-print labels, or misweigh labels. Therefore, the case packing station contains a workflow where the labels printed in the packing flow are scanned, verified, and associated with a case. Cases will also be serialized and be assigned a barcode. You may make the following assumptions about case packing:
- Cases only ever consist of 1 product type
- Cases may consist of multiple lots
- Cases will be labeled with a gross (as measured by a scale) and net (sum of package weights) weight, printed on the label

# Part 1
Your task is to design and implement a database to support this application. Use whatever tooling you are most comfortable with, if you don't have a preference we suggest starting with a community edition of MySQL. 
The data model you design should enable the application to:
- Supports 5 instances of the application running simultaneously on different computers on a local network (assume connection to the internet is spotty)
- Assign a unique, nonrepeating barcode for each cut
- log printed labels
- Specify a framework for assigning label statuses (whether or not they have been validated at case packing) and assigning individual packages to a case

# Part 2
Congratulations! Your implementation of the packing application was successfully deployed. The analytics team is eager to start to use this data, which means we must design a workflow for how to collect data from your database, and merge it into Walden's database, Your next task is to write up a proposal and any proof of concept code to demonstrate your idea. 

Acceptance Criteria:
- The collection process should be simple enough for our logistics drivers to handle. They will not be comfortable running command-line scripts, but can do things like plug in USB sticks/mobile hotspots,  start shortcuts from a folder, or click and drag files
- You may assume that merging processor data into Walden's data happens at HQ, (ie the Logistics driver leaves the USB key with you when they finish their run)
- Your proposal should include a simple guide to how the data is structured, and how you intend it to be accessed







