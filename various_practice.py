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



# Enter a number to check whether it's perfect number or not.

num = int(input("Please enter a number to check for perfect numbers.\n"))
sum = 0
for i in range(1, int(num/2)+1):
    if num % i ==0:
        sum += i
if sum == num:
    print("It's a perfect number.")
else:
    print("It's not a perfect number.")


    
    
# Number of days in a month using return function:


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid input."
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]

year = int(input("Enter a year: \n"))
month = int(input("Enter a month: \n"))
days = days_in_month(year, month)
print(days)
