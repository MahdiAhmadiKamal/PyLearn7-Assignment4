numbers = []
res = []

m = int(input("enter number of numbers in your list: "))
print ("")
print ("Now, you should enter the numbers.")

for i in range (m):
    n = float(input ("enter your number:"))
    numbers.append(n)

# removing the duplicate elements (this loop doesn't change the order of the numbers)
for i in numbers:
    if i not in res:
        res.append(i)
print ("The list after removing duplicates:", res)


