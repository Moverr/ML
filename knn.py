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

knn  = KNeighborsClassifier(n_neighbors = 1)


knn.fit(X_train,y_train)
print("pass {} ".format(knn))

x_new = np.array([[5,2.9,1,0.2]])

print("Shape {}".format(x_new.shape))

# print("Training Data Dimension {} ".format(X_train.shape))
prediction = knn.predict(x_new)

print("Prediction {} ".format(prediction))
print("Predicted Target Name : {}".format(iris_dataset['target_names'][prediction]))



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
