# 15.	Number of Digits – Count the number of digits in a number.
n = int(input("Enter any number: "))
count = 0

while n > 0:
    n = n // 10   
    count += 1    
print("Number of digits:", count)