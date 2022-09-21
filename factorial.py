#Algorithm to obtain factorial of a number.(Using while loop)

num = int(input("Please enter a number to obtain it's factorial.\n"))
factorial = 1

while(num):
    factorial *= num
    num -= 1
print(factorial)

#Algorithm to obtain factorial of a number.(Using for loop)

#Algorithm to obtain factorial of a number

num = int(input("Please enter a number to obtain it's factorial.\n"))
factorial = 1

for i in range(1, num+1):
    factorial *= i
print(factorial)
