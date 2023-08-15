# a,b = eval(input("enter a,b"))
# if(a>b):
#     print("a is greatest")
# else:
#     print("b is greatest")


# true part if condition else false part
# print("a is greatest") if(a>b) else print("b is greatest")
# if(n&1)==0 : print("odd")
#else : print("even")

# nation = input("enert your nationality ")
# nation=nation.upper()
# if(nation=="INDIAN"):
#     n = int(input("enter age"))
#     if(n>=18):
#         print("Yes Allow for PAN card")
#     else:
#         print("Not allowed due to age")
# else:
#     print("Not allowed due to nationality")
n = input("enter name").upper()
reverse = n[::-1].upper()
if n==reverse :
    print("pallindrome")
else:
    print("not pallindrome")