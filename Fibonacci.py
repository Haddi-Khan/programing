# 13.	Fibonacci Series – Print the first n Fibonacci numbers.
num=int(input("enter any number "))
a,b=0,1
p=0
while p<=num:
    print(a,end="")
    c=a+b
    a=b
    b=c
    p=p+1
    