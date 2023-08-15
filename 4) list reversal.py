numbers = []

m = int(input("enter number of numbers in your list: "))
print ("")
print ("Now, please enter", m, "numbers.")

for i in range (m):
    n = float(input ("enter your number:"))
    numbers.append(n)

print ("your numbers list: ", numbers)

# reversing the order of list elements
numbers.reverse()
print ("Reversed List:", numbers)
