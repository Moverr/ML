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
total_sum = d.values()
for keys in d.keys():
    print(d[keys])
    # x[keys] = (d[keys]/total_sum) * 100

print(x)
print(olddata)
def bayern_probabilyt():
    pass


def main():
    print("Entry point ")


main()

