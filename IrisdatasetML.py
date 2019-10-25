from sklearn.datasets import load_iris

irisDataset = load_iris()

print("The Iris Dataset {}".format(irisDataset.keys()))
print("---------------------------------------------------")
print("  XXX {} \n ".format(irisDataset['target_names']))
