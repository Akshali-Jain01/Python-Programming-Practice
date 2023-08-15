from math import sqrt
a,b,c = eval(input("Enter a,b,c"))
x1 = ((-b)+sqrt((b**2)-4*a*c))/(2*a)
x2 = ((-b)-sqrt((b**2)-4*a*c))/(2*a)
print(x1,x2)
