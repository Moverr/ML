from  sklearn import tree

#Need to understand sklean package , what it can do and explore a few items
features = [
[140,0],
[130,0],
[150,1],
[170,1] 
]
labels = [0,0,1,1]

clf = tree.DecisionTreeClassifier()