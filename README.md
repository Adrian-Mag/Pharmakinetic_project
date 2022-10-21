[![Python versions test](https://github.com/Adrian-Mag/Pharmakinetic_project/actions/workflows/python-versions.yml/badge.svg)](https://github.com/Adrian-Mag/Pharmakinetic_project/actions/workflows/python-versions.yml)
[![OS tests](https://github.com/Adrian-Mag/Pharmakinetic_project/actions/workflows/os-tests.yml/badge.svg)](https://github.com/Adrian-Mag/Pharmakinetic_project/actions/workflows/os-tests.yml)
[![codecov](https://codecov.io/gh/Adrian-Mag/Pharmakinetic_project/branch/main/graph/badge.svg?token=NNG4YNS1H3)](https://codecov.io/gh/Adrian-Mag/Pharmakinetic_project)
[![Documentation Status](https://readthedocs.org/projects/pharmacokinetic-modelling/badge/?version=latest)](https://pharmacokinetic-modelling.readthedocs.io/en/latest/?badge=latest)

# 2020-software-engineering-projects-pk
This project runs a basic pharmacokinetic (PK) model, allowing the user to quantitatively examine the flow of drugs in and out of the body. This model accounts for absorption, distribution, metabolism, and excretion (ADME). Here, the body itself is modelled as a series of compartments, with the number of compartments able to be chosen by the user, with a maximum of two peripheral compartments and the addition of a compartment to account for subcutaneous dosing. This package allows the user to specify, solve, and visualize the solution to a PK model. The user can select whether or not they would like to model a constant rate of drug dosage, instantaneous drug dosage at predetermined intervals, or a combination of the two. The choice of model can be made independently of that of dosage type.

# Instructions for installing the package
First, make sure you are working in a virtual environment. This can be done by running the following lines in the terminal:

    $ python3 -m venv venv
    $ source venv/bin/activate
    
To clone the repository:

    (venv) $ git clone git@github.com:Adrian-Mag/Pharmakinetic_project.git
    
And install the dependencies:

    (venv) $ python setup.py install

# Files contained in this package
setup.py: A python script that, when run, installs the necessary dependencies required to use this package

LICENSE: A text file describing the license associated with this package.

README.md: The file you're reading right now! Contains information about what the package can do, how to install and run the code, the contents of the package, and who the authors are.

pkmodel: A folder containing all of the code needed to construct and solve a PK model.

    - __init__.py: A python script that initializes the model.py, protocol.py, and solution.py scripts

    - model.py: A python script that establishes a class Model, which has a number of attributes chosen by the user, representing the specifications of the model the user wishes to examine

    - protocol.py: A python script that establishes a class Protocol, which has a dosage method chosen by the user.

    - solution.py: A python script that establishes a class Solution, which takes in an object of class Model and class Protocol, and derives a solution to the PK model. This script also contains a function compare() which allows for the direct comparison of multiple Solution objects.

    - example.py: A python script that provides a template for creating and solving a PK model, which should be modified according to the user's needs in order to test the desired models and dosage protocols.

    - version_info.py: A python script containing the version info for the Pharmakinetic_project package.

    - tests: A folder containing the unit tests used to make sure all of the code runs properly.

docs: A folder containing all of the code used to create the documentation associated with this package. The user should have no need to access this folder.

# Authors
This package was created by Adrian Mag, Sam Scivier, and Spencer Pevsner, as part of the 2022 Software Engineering & Sustainable Research course at the University of Oxford.
