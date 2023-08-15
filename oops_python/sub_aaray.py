import itertools
def chetan(s,n):
    return list(itertools.combinations(s,n))
s={1,2,3,4}
for i in range (1,len(s)+1):
    print(chetan(s,i))