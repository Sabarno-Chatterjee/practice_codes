#Algorithm to obtain product of a number

num = int(input("Please enter a number to obtain it's product\n"))
c= 0
is_product = False
product = 1

while(num):           # Change is here.
    c = num % 10
    product = product * c
    num = num // 10
print(product)
