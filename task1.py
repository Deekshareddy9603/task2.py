
# Task 1 – Print Formatting
print("Hello", "World", "Welcome", "Python", sep=" ")
print("Laptop", "Mouse", "Keyboard", sep=" | ")

# Output:
# Hello World Welcome Python
# Laptop | Mouse | Keyboard




# Task 2 – Variables
name = "Ravi"
age = 22
city = "Chennai"
print(name, age, city, sep="-")
# sep="-" joins the variables with dash

# Output:
# Ravi-22-Chennai




# Task 3 – Multiple Assignment
name, age, student = "Meena", 20, True
print(name, age, student)

# Output:
# Meena 20 True




# Task 4 – Indexing
word = "Python"
print("First letter:", word[0])
# Index starts from 0 → P
print("Third letter:", word[2])
# P(0) y(1) t(2)
print("Last letter:", word[-1])
# -1 means last character

# Output:
# First letter: P
# Third letter: t
# Last letter: n




# Task 5 – Arithmetic Operators
print(25 + 10)  
print(50 - 20)  
print(8 * 5)    
print(100 / 10) 
print(10 % 3) 
print(2 ** 4)   
print(20 // 3)  

# Output:
# 35
# 30
# 40
# 10.0
# 1
# 16
# 6



# Task 6 – BODMAS Expression
print(3 + 2 * 5 ** 2)
# BODMAS rule
# 1) Power → 5**2 = 25
# 2) Multiplication → 2*25 = 50
# 3) Addition → 3+50 = 53

# Output:
# 53




# Task 7 – Assignment Operator
num = 50
num += 25
# num = num + 25
# 50 + 25 = 75
print(num)
num = 100
num /= 10
# num = num / 10
# 100 / 10 = 10.0
print(num)

# Output:
# 75
# 10.0




# Task 8 – Comparison Operators
print(10 > 5)   # True
print(20 < 15)  # False
print(5 == 5)   # True
print(10 != 8)  # True
print(7 >= 7)   # True
print(6 <= 2)   # False

# Output:
# True
# False
# True
# True
# True
# False




# Task 9 – String Comparison
a = "apple"
b = "Apple"
print(a == b)
# small 'a' ≠ capital 'A'

# Output:
# False




# Task 10 – Logical Operators
print(10 > 5 and 5 == 5)
# True and True → True
print(5 > 10 or 10 == 10)
# False or True → True
print(not(5 > 2))
# not(True) → False

# Output:
# True
# True
# False




# Task 11 – Membership Operator
numbers = [10, 20, 30, 40, 50]
print(20 in numbers)
# 20 exists in list → True
print(60 in numbers)
# 60 not in list → False
print(30 not in numbers)
# 30 exists so → False

# Output:
# True
# False
# False




# Task 12 – Swap Variables
a = 10
b = 20
a, b = b, a
# Values swapped
print("a =", a)
print("b =", b)

# Output:
# a = 20
# b = 10




# Task 13 – Bitwise XOR
a = 6
b = 3
print(a ^ b)

# 6 → 110
# 3 → 011

# 1^1 = 0
# 1^0 = 1
# 0^1 = 1

# 110
# 011
# 101 → 5

# Output:
# 5