from  sklearn import tree

#Need to understand sklean package , what it can do and explore a few items
features = [
[140,0],
[130,0],
[150,1],
[170,1] 
]
labels = [0,0,1,1]

# Decision Tree Classifier 
clf = tree.DecisionTreeClassifier()
# Find Pattens in Data FIT 
clf.fit(features,labels)

result = (clf.predict([[110,1]]))

result_extp = { }
result_extp[0] = "Orange"
result_extp[1] = "Apple"
 
# print (result)
print(result_extp[result[0]])

