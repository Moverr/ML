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
    for keys in d.keys():
        if(keys == x):
            print("Pass")
    d[x] = 1


print(d)
print(olddata)
def bayern_probabilyt():
    pass


def main():
    print("Entry point ")


main()

