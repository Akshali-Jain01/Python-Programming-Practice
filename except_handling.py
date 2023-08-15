# a,b = eval(input("enter 2 numbers : "))
# try:
#     print(a/b)
# except Exception as e:
#     print('Error :',e)

# print("testing")

# try:
#     char= int(input("enter character"))
# except Exception as e:
#     print(e)

# a,b = eval(input("enter numbers : "))
# try:
#     print(a/b)
#     x=int(input("enter char "))

# except ZeroDivisionError as e:
#     print("please dont enter zero..",e)
# except ValueError as v:
#     print(v)
# except Exception as ex:
#     print(ex)
# finally:
#     print("Inside Finally")
from time import *
print(asctime(localtime(time())))
print(localtime(time()))
for i in range(0,5):
    print(i)
    sleep(1)
from calendar import *
prcal(2016)
