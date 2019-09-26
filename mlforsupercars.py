from sklearn import tree
from sklearn.externals.six import StringIO  
import pydot

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
 

print (result)
print(result_extp[result[0]])

 

# dot_data = StringIO()
# tree.export_graphviz(clf,out_file=dot_data,
# feature_names=feature_names,
# class_names=["Super Car","Mini Van"],
# filled=True, rounded=True,impurity=False
# )

 
# # print(dot_data.getvalue())
# graph = pydot.graph_from_dot_data(dot_data.getvalue())

# result_extp = { }
# result_extp[1] = "Super Car"
# result_extp[2] = "Mini Van"
 


# graph[0].write_pdf("iris.pdf")
# #
