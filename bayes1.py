
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
# sns.set(style='ticks', palette='Set2')

# params = np.linspace(0, 1, 100)
# p_x = [np.product(st.bernoulli.pmf(data_coin_flips, p)) for p in params]
# plt.plot(params, p_x)
# sns.despine()



print("....................................................")
def bern_post(n_params=100, n_sample=100, true_p=.8, prior_p=.5, n_prior=100):
    params = np.linspace(0, 1, n_params)
    sample = np.random.binomial(n=1, p=true_p, size=n_sample)
    likelihood = np.array([np.product(st.bernoulli.pmf(sample, p)) for p in params])
    #likelihood = likelihood / np.sum(likelihood)
    prior_sample = np.random.binomial(n=1, p=prior_p, size=n_prior)
    prior = np.array([np.product(st.bernoulli.pmf(prior_sample, p)) for p in params])
    prior = prior / np.sum(prior)
    posterior = [prior[i] * likelihood[i] for i in range(prior.shape[0])]
    posterior = posterior / np.sum(posterior)
     
    fig, axes = plt.subplots(3, 1, sharex=True, figsize=(8,8))
    axes[0].plot(params, likelihood)
    axes[0].set_title("Sampling Distribution")
    axes[1].plot(params, prior)
    axes[1].set_title("Prior Distribution")
    axes[2].plot(params, posterior)
    axes[2].set_title("Posterior Distribution")
    sns.despine()
    plt.tight_layout()
     
    return posterior

example_post = bern_post()


print(example_post)