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
for x,y in olddata:
    count = 0
    if(len(d) > 0 ):
        for z in d.keys():
            if(z == x):
                count = d[z] + 1
    else:
        count = 1
                
    print("COUNT : ")
    print(count)
    d[x] = y

print(d)
print(olddata)
def bayern_probabilyt():
    pass


def main():
    print("Entry point ")


main()

