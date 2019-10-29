from sklearn.datasets import load_iris

irisDataset = load_iris()

print("The Iris Dataset {}".format(irisDataset.keys()))
print("----------------------Type of Data-----------------------------")
print("  Type of Data {} \n ".format(type(irisDataset['data'])))

print("----------------------Shapee of Data-----------------------------")
print("  Shape of Data {} \n ".format(irisDataset['data'].shape))


print("----------------------First FIve Columns of Data -----------------------------")
print("  First five columns  of Data {} \n ".format(irisDataset['data'][:5]))

print("Spliting Data into 2 ")

print("Target : {} ".format(irisDataset['target']))
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(irisDataset['data'],irisDataset['target'],random_state = 0)


print("Train Data")
print("X TRAIN SHAPE {} ".format(x_train.shape))
print("Y TRAIN SHAPE {} ".format(y_train.shape))

print("X TEST SHAPE {} ".format(x_test.shape))
print("Y TEST SHAPE {} ".format(y_test.shape))


print("SOme Plotting NEeded  in Pandas")

import pandas as pd 
iris_dataFrame  =  pd.DataFrame(x_train,columns=irisDataset.feature_names)

print("intersting \n {}".format(iris_dataFrame[:5]))
from pandas.plotting import scatter_matrix as smt

grr = smt(iris_dataFrame, c=y_train,figsize=(15,15),marker='o',hist_kwds={'bins':20},s=60,alpha=.8,cmap=mglearn.CM3)