# get the most likely category  to be used  git stat


 
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

 
def percentileviewership(records,labels):
    x = {}
    total_sum = sum(records.values())
    for keys in records.keys():
        percentile = float(records[keys]) /float(total_sum) * 100 
        x[labels[keys]] = percentile        
    return x


def main(): 
    #  we need to categorize data 
    features = ["Category","Views"]
    labels = {}
    labels[1] = "Politics"
    labels[2] = "Sports"    

    dataset= [  [2,1], [1,1], [1,1], [1,1] ]    
    cleaned_data = clean_data(dataset)
    result =   percentileviewership(cleaned_data,labels) 
    print("Debugging :: ")
    print(result)
 
main()

