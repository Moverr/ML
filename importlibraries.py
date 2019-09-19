# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

print("FInished importing")
 
# Load dataset
#url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
url =  "iris.csv"

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

print("Importing Data in Pythong")

#shape of the dataset
print(dataset.shape)

#head of the dataset
print(dataset.head(20))

#Descriptions
print(dataset.describe())


#Descriptions
#print(dataset["sepal-length"].describe())


# class distribution
# print(dataset.groupby('class').size())



# box and whisker plots
# dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
# plt.show()


# scatter matrix
# scatter_matrix(dataset)
# plt.show()


# histograms
# dataset.hist()
# plt.show()


# Split-out validation dataset
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)


# Test options and evaluation metric
seed = 7
scoring = 'accuracy'
1
2
3
# Test options and evaluation metric
seed = 7
scoring = 'accuracy'


 
# Test options and evaluation metric
seed = 7
scoring = 'accuracy'


print("END")

