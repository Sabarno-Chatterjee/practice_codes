#Algorithm to check prime.

num = int(input("Please enter a number to check for prime.\n"))
i = 0
is_prime = False

while not is_prime:
    for n in range(2, num):
        if num % n == 0 and n != 2:
            is_prime = True
            print("Not prime.")
            break

    if not is_prime:
        print("Prime")
        break
