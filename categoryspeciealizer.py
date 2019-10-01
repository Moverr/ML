# get the most likely category  to be used  git stat

#  we need to categorize data 
olddata= [
    [1,1],
    [2,1],
    [1,1],
    [1,1],
    [1,1]
    
    ]

d = {}
first_record = olddata[0]

for x,y in olddata:
    count = 1
    for keys in d.keys():
        if(keys == x):
            print("Pass")
    d[x] = count


print(d)
print(olddata)
def bayern_probabilyt():
    pass


def main():
    print("Entry point ")


main()

