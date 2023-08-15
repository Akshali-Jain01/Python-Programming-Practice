# '''for i in range(1,11):
#     print(i)'''
# for i in range(1,11,2):
#     print(i)
# for i in range (2,11,2):
#     print(i)
# for i in range (n,n*10+1,n):
#     print(i,end="")
# sum =0
# for i in range (1,11):
#     sum = sum+i
from random import *
x = randint(1,100)
for i in range(1,11):
    num=int(input("guess the number"))
    if(x==num):
      print("perfect choice")
      print(" You gave the answer in ",i," try")
      break
    elif(x>num):
      print("Try again",num ,"is less than actual")
    elif(x<num):
      print("Try again",num ,"is greater than actual")
    print("you are left with ",10-i," try")
else:
    print("you are loser and perfect number is ", x)
    
