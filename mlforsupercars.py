from sklearn import tree

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





result_extp = { }
result_extp[1] = "Super Car"
result_extp[2] = "Mini Van"
 



