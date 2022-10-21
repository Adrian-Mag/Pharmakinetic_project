.. Pharmacokinetic Modelling Project documentation master file, created by
   sphinx-quickstart on Fri Oct 21 10:09:03 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Pharmacokinetic Modelling Project's documentation!
=============================================================

**Pharmacokinetic Modelling Project** is a Python library for running a basic Pharmacokinetic (PK) model. 
It allows the user to quantitatively examine the flow of drugs in and out of the body. This model accounts 
for absorption, distribution, metabolism, and excretion (ADME). Here, the body itself is modelled as a 
series of compartments, with the number of compartments able to be chosen by the user, with a maximum 
of two peripheral compartments and the addition of a compartment to account for subcutaneous dosing. 
This package allows the user to specify, solve, and visualize the solution to a PK model. The user can 
select whether or not they would like to model a constant rate of drug dosage, instantaneous drug dosage 
at predetermined intervals, or a combination of the two. The choice of model can be made independently 
of that of dosage type.

.. note::

   This project is under development.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   usage
   modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
