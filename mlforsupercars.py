from sklearn import tree

feature_names = ["Horse Power","# Seats"]
# Horse Power and Seating capacity 
features = [
    [300,2],
    [450,2],
    [200,8],
    [150,9] 
]

# change supercar for 1 and minivan for 2
labels = [1,1,2,2] 



# Decision Tree Classifier 
clf = tree.DecisionTreeClassifier()

# Find Pattens in Data FIT 
clf.fit(features,labels)

result = (clf.predict([[250,2]]))


result_extp = { }
result_extp[1] = "Super Car"
result_extp[2] = "Min Van"
 

# print (result)
print(result_extp[result[0]])


from sklearn.externals.six import StringIO
import pydot
import cStringIO

dot_data = cStringIO()
tree.export_graphviz(clf,out_file=dot_data,
feature_names=feature_names,
class_names=["Super Car","Mini Van"],
filled=True, rounded=True,impurity=False
)

 

graph = pydot.graph_from_dot_data(dot_data.getValue())

result_extp = { }
result_extp[1] = "Super Car"
result_extp[2] = "Mini Van"
 



