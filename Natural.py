# 7Sum of N Natural Numbers – Take a number n and find the sum of first n natural numbers.
n = int(input("enter any number"))
sum_n=0
for i in range(1,n+1,):
    sum_n+=i
print("the sum of first number", n , "natural number is:",sum_n)