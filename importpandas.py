#  statistical summary
import pandas  
url =  "iris2.csv"
names =  []
# always describe names against the column dataset 
dataset = pandas.read_csv(url, names=names)



print(dataset)
# description  = dataset.descdribe()

# print(descriptiondata.head(10))