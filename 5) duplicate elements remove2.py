numbers = []

m = int(input("enter number of numbers in your list: "))
print ("")
print ("Now, you should enter the numbers.")

for i in range (m):
    n = float(input ("enter your number:"))
    numbers.append(n)

print ("your numbers list: ", numbers)

# removing the duplicate elements (but set() function will order the numbers from small to large)
res = set (numbers)
print ("The list after removing duplicates:", res)
