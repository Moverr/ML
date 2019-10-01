
# from feature import ContinuousFeature
# from feature import DiscreteFeature
# from naive_bayes import NaiveBayes


import pandas  
url =  "loan-defaulters.csv"
names =  ["D1","AMOJNT","D3"]
# always describe names against the column dataset 
dataset = pandas.read_csv(url, names=names)

# Dataset is quite important 
print(dataset)

# todo import data from samples 

import numpy as np
data_coin_flips = np.random.randint(2, size=1000)

result = np.mean(data_coin_flips)

print("-------------------------------------")
print(result)
