#  statistical summary
import pandas  
url =  "iris2.csv"
names =  ["D1","D2","D3","D4","D5","D6","D7","D8","D9","d10","d11"]
# always describe names against the column dataset 
dataset = pandas.read_csv(url, names=names)





simple_data = dataset.head(5)
print(simple_data)

# this is a statists formula for finding and cleaning data in the simplest ways possible
description  = simple_data.describe()
print("-----------------------------------")
print(description)

# print(descriptiondata.head(10))