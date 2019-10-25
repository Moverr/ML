from sklearn.datasets import load_iris

irisDataset = load_iris()

print("The Iris Dataset {}".format(irisDataset.keys()))
print("----------------------Type of Data-----------------------------")
print("  Type of Data {} \n ".format(type(irisDataset['data'])))

print("----------------------Shapee of Data-----------------------------")
print("  Shape of Data {} \n ".format(irisDataset['data'].Shape))

