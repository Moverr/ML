# upgrading a package 
# pip3 install --upgrade pandas --user
import numpy as np
# print("NUMPY {}".format(np.__version__))
import scipy as sc
# print("SCIPY {}".format(sc.__version__))
import pandas as pd 

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris_dataset = load_iris()


X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)

print("Training Data {} ".format(X_train))



# print("PANDA {}".format(pd.__version__))

# data = {
#     'Name':["John","Anna","Peter","Linda"],
#     'Location':["New Yourk","Paris","Berlin","London"],
#     'Age':[24,13,53,33]
# }


# data_pandas = pd.DataFrame(data)

# print(" ****************************88 \n ")

# print(data_pandas.Name)
# print(data_pandas.Location)
# print(data_pandas.Age)

# print("Different  ..............................\n")
# print(data_pandas.loc[1])

# from sklearn.nieghbors import train_test_split
