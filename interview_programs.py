from operator import mul
import random

# Add two numbers

a = 12
b = 14
c = a + b
print('sum of 2 digits is', c)

# Swap two numbers

s1 = 33
s2 = 44
print("Before swapping", s1, s2)
temp = s1
s1 = s2
s2 = temp
print("After swapping", s1, s2)

# Generate Random Number

print("The random number between 0 to 9 is", random.randint(0, 9))

# Convert Kilometers to Miles conversion factor conv_fac = 0.621371

conv_fact = 0.621371
kms = int(input("Enter in Kilometers "))
in_miles = kms / conv_fact
print("The conversion of Kilometers to miles is ", in_miles)

# Check if a number is positive or not

num = float(input("Enter a number to check if it is positive "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive Number")
else:
    print("Negative Number")

# Multiplication Table

def multi_table(multi_num):
    for i in range(1, 11):
        print(multi_num, 'x', i, '=', num*i)

multi_table(11)

