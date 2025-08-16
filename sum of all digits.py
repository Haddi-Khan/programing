# 16.	Sum of Digits – Sum all digits of a number
n = int(input("Enter any number: "))
total = 0

while n > 0:
    digit = n % 10   
    total = total+ digit    
    n = n // 10      
print("Sum of digits:", total)