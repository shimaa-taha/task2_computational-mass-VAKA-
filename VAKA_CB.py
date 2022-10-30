#!/usr/bin/env python
# coding: utf-8

# In[34]:

get_ipython().system('pip install pyopenms')
import pyopenms
from pyopenms import *
from pyopenms.Constants import *
seq = AASequence.fromString("VAKA")     # create AASequence object
seq_Formula = seq.getFormula()
print("Peptide", seq, "has molecular formula", seq_Formula)
x=0
for aa in seq:
    x=x+ aa.getMonoWeight()# every element alone 
print("mass of VAKA ",seq.getMonoWeight())#mass of VAKA
print ("every element alone ",x)
