#  statistical summary
import pandas  
url =  "iris2.csv"
names =  ["D1","D2","D3","D4","D5","D6","D7","D8","D9","d10","d11"]
# always describe names against the column dataset 
dataset = pandas.read_csv(url, names=names)



print(dataset)
# description  = dataset.descdribe()

# print(descriptiondata.head(10))