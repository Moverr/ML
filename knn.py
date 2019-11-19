# upgrading a package 
# pip3 install --upgrade pandas --user
import numpy as np
print("NUMPY {}".format(np.__version__))
import scipy as sc
print("SCIPY {}".format(sc.__version__))
import pandas as pd 
print("PANDA {}".format(pd.__version__))

data = {
    'Name':["John","Anna","Peter","Linda"],
    'Location':["New Yourk","Paris","Berlin","London"],
    'Age':[24,13,53,33]
}


# from sklearn.nieghbors import train_test_split
