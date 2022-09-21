#Length of a list without using len function:

list =["Apple","Banana","Orange","Kiwi","Coconut"]
list.append("Grapes")
list.append("Mango")

print(list)

list = list + ["Grapefruit", "Dragonfruit", "Litchi"]
print(list)
length = 0
i = 0
try:
    while list[i]:
        length += 1
        i += 1
except IndexError:

    print(length)
