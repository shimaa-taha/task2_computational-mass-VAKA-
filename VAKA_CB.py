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
cnt=1
# print coarse isotope distribution
isotopes = seq_Formula.getIsotopeDistribution( CoarseIsotopePatternGenerator(4) )
for iso in isotopes.getContainer():
    print ("Iso ",cnt ," ", iso.getMZ(), "has abundance", iso.getIntensity()*100, "%")
    cnt=cnt+1
    x=x+iso.getMZ()
print("mass of V + mass of A + mass of K + mass of A = ",x)
mz = seq.getMZ(1)+seq.getMZ(2)+seq.getMZ(3)+seq.getMZ(4)
print("MZ = ",mz)


# In[26]:





# In[35]:





# In[ ]:




