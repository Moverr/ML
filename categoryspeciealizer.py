# get the most likely category  to be used  git stat

#  we need to categorize data 
olddata= [
    [2,1],
    [1,1],
    [1,1],
    [1,1]
    ]

 
def clean_data(sample_data):
    records = {}
    first_record = sample_data[0] 
    for x,y in sample_data:
        count = 1
        for keys in records.keys():
            if(keys == x):            
                count = records[keys] + 1
        records[x] = count
    return records

 
def percentileviewership(records):
    x = {}
    total_sum = sum(d.values())
    for keys in d.keys():
        percentile = float(d[keys]) /float(total_sum) * 100 
        x[keys] = percentile        
    return x


def main():
  
    cleaned_data = clean_data(olddata)
    result =   percentileviewership(clean_data) 
    print("Debugging :: ")
    print(result)
 
main()

