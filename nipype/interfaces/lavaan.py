# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
""" 
========================
Lavaan nipype interface
========================

Lavaan is an R library for strucutral equation modelling. 

This interface allows Lavaan models to be specifed and run 
through nipype. 

Two types of input are required: 

1. Strings defining the model to be fitted
2. File containng the data to be used. 

Example: 
--------

>> blah 
>> blahblah
>> blahblahblah
>>
>>

l = lavaan()

l.inputs.latent_variables = {'l1': ['v1', 'v2', 'v3'],
                             'l2': ['v2', 'v3', 'v4']}

l.inputs.covariances = [['v1', 'v2'],
                        ['v3', 'v5'],
                        ['l1', 'l4']]


l.inputs.data = 'data_file.csv'

l.inputs.fit_measures = True
#fit.measures = TRUE


l.inputs.model_type = 'cfa' # (or 'sem')

l.run()


--- 


NOTES:
------

- make some workflows that take ROIs from DWI and fit lavaan models
- always spit out the lavaan code as a text file
- make use of iterables or workflows, or something to make it worth 
  using nipype at all

- special options for mediation / multiple mediation?

- also do one of these for bayesmed? and for bayesfactor?




"""

def specify_model():
  blah

 
def get_modindices():
  mi <- modindices(fit)



TRYING THIS AGAIN. 


RIGHT. ONE MORE TIME. TEMPORARY COMMIT HERE. 

...NOW ADDING MORE TO IT ON THE OTHER SIDE. 
