
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
data_coin_flips = np.random.randint(2, size=5)

print(":::::::::::::::::::::::::::::::")
print(data_coin_flips)
result = np.mean(data_coin_flips)

print("-------------------------------------")
print(result)


import scipy.stats as st
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
sns.set(style='ticks', palette='Set2')

params = np.linspace(0, 1, 100)
p_x = [np.product(st.bernoulli.pmf(data_coin_flips, p)) for p in params]
plt.plot(params, p_x)
sns.despine()

