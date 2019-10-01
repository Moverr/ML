# get the most likely category  to be used  git stat

#  we need to categorize data 
olddata= [
    [2,1],
    [1,1],
    [1,1],
    [1,1]
    ]

d = {}
first_record = olddata[0]

# get the view count 
for x,y in olddata:
    count = 1
    for keys in d.keys():
        if(keys == x):            
            count = d[keys] + 1
    d[x] = count

# todo: loop through and get the probability list of viewership vs category 
x = {}
 
total_sum = sum(d.values())
 
for keys in d.keys():
    percentile = float(d[keys]) /float(total_sum) * 100 
    x[keys] = percentile


print(x)
print(olddata)
def clean_data(sample_data):
    record = {}
    first_record = sample_data[0] 
    for x,y in sample_data:
        count = 1
        for keys in record.keys():
            if(keys == x):            
                count = record[keys] + 1
        record[x] = count

 
def bayern_probabilyt():
    pass


def main():
    print("Entry point ")


main()

