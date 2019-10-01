
# from feature import ContinuousFeature
# from feature import DiscreteFeature
# from naive_bayes import NaiveBayes


import pandas  
url =  "iris2.csv"
names =  ["D1","D2","D3","D4","D5","D6","D7","D8","D9","d10","d11"]
# always describe names against the column dataset 
dataset = pandas.read_csv(url, names=names)



# todo import data from samples 