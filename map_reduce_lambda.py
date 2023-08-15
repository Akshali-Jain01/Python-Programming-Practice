rudhra =lambda a:a*a
print(rudhra(4))
num1=[3,4,6,778,45,6,34,23,346,67]
def evenlist1(num):
    if(num%2==0):
        return(num)
result = list(filter(evenlist1,num1))
result1 = list(filter(lambda num: num%2==0,num1))
print(result,result1)
print(list(map(lambda num: num%2==0,num1)))
from functools import reduce
print(reduce(lambda a,b:a*b,[1,2,3,4,5]))
ans=[i for i in range(1,100) if i%2==0]
print(ans)