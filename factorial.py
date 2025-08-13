#8.	Factorial – Find the factorial of a given number using a loop.
n = int(input("Enter a number: "))
fact = 1   
for i in range(1, n + 1):
    fact *= i 
print("The factorial of", n, "is:", fact)