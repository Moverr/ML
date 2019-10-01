
# from feature import ContinuousFeature
# from feature import DiscreteFeature
# from naive_bayes import NaiveBayes


import pandas  
url =  "loan-defaulters.csv"
names =  ["D1","D2","D3"]
# always describe names against the column dataset 
dataset = pandas.read_csv(url, names=names)

# Dataset is quite important 
print(dataset)

# todo import data from samples 