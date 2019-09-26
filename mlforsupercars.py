 from sklearn import tree

# Horse Power and Seating capacity 
features = [
    [300,2],
    [450,2],
    [200,8],
    [150,9] 
]

# change supercar for 1 and minivan for 2
labels = [
    [1,1,2,2] 
]


result_extp = { }
result_extp[1] = "Super Car"
result_extp[2] = "Mini Van"

clf = tree.DecisionTreeClassifier()




