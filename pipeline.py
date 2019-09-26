from sklearn import datasets
iris = datasets.load_iris()
x = iris.data
y = iris.target 

from sklearn.model_selection import  train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = .5)

# Decision Tree Classifier 
# from sklearn import tree
# my_classifier = tree.DecisionTreeClassifier()

from sklearm import  KNeighborClassifier
my_classifier = KNeighborClassifier()

my_classifier.fit(x_train,y_train)

predictions = my_classifier.predict(x_test)

print(predictions)

# Measure the Accuracy of the Classifier 
from sklearn.metrics import accuracy_score
print accuracy_score(y_test,predictions)
