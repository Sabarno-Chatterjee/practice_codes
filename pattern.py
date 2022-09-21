#Patterns:

num = int(input("Please enter a number to obtain a left sided stacked pattern.\n"))
c=""
for i in range(1, num+1):
    c = c + str(i)
    print(c)



num = int(input("Please enter a number to obtain a left sided reverse symbol stacked pattern.\n"))


for i in range(num, 0, -1):
    for j in range(i):
        print("*", end='')
    print()

