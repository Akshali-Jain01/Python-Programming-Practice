from random import randint
def function ():
    n = int(input("enter n"))
    password =''
    for i in range(n):
        a = chr(randint(48,122))
        if a not in password:
            password+=a
        # else:
            # n=n+1
            # i=i-1
    # print(len(password))
    if n==len(password):
        print(password)
    else:
         for i in range(n):
            a = chr(randint(48,122))
            if a not in password:
                password+=a
            if n==len(password):
                break
        
    print(password)
    print(len(password))
        


function()