# Sum of odd and even numbers between a range:

start =  int(input("Enter the starting point of a range.\n"))
end = int(input("Enter the ending point of the range.\n"))

odd = 0
even = 0

for i in range(start, end+1):
    if i %  2 == 0:
        even += i
    else:
        odd += i

print(f"The sum of the even and odd numbers between the range {start} and {end} is even = {even} and odd = {odd}.\n")

# Enter a number to obtain its table:

num = int(input("Please enter a number to obtain it's table.\n"))

for i in range(1,11):
    calc = num * i
    print(f"{num} * {i} = {calc}")
    
 

# Decimal to binary conversion:

num = int(input("Please enter a number to obtain it's binary notation.\n"))

i= 0
list = ""

while(num):
    i = num % 2
    list = list + str(i)
    num = num//2

length = len(list)

for i in range(length-1, -1, -1):
    print (list[i], end= '')
    

# Pallindrome checker:

num = input("Please enter a number to check whether it's pallindrome of not.\n")
x = ""
length = len(num)

for i in range(length-1, -1, -1):
    x += num[i]
if x==num:
    print(f"{num} is a pallindrome.")
else:
    print(f"{num} is not a pallindrome.")



