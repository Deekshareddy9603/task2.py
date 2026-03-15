
# Task 1
a = 10
b = 6
print(a & b)

# 10 = 1010
# 6  = 0110

# 1010
# 0110

# 0010 = 2

# Output:
# 2


# Task 2
x = 12
y = 5
print(x | y)


# 12 = 1100
# 5  = 0101
# 1100
# 0101
# 1101 = 13

# Output:
# 13



# Task 3
num = 8
print(~num)

# Formula → -(num + 1)
# -(8+1) = -9

# Output:
# -9



# Task 4
a = 15
b = 9

print(a ^ b)
# 15 = 1111
# 9  = 1001
# 0110 = 6

# Output:
# 6



# Task 5
num = 7
print(num << 2)

# 7 << 2 = 7 * 4 = 28

# Output:
# 28



# Task 6
num = 20
print(num >> 1)

# 20 >> 1 = 20 / 2 = 10

# Output:
# 10



# Task 7
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a & b)

# output Example
# Input: 10,6
# Output: 2



# Task 8
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a ^ b)

# Output Example
# Input: 6,3
# Output: 5


# Task 9
s = "hi"
print(s * 4)


# Output:
# hihihihi



# Task 10
s = "python"
print(s * 3)

# Output
# pythonpythonpython



# Task 11
a = "super"
b = "man"

print(a + b)

# Output
# superman



# Task 12
a = "hello"
b = " "
c = "world"

print(a + b + c)

# Output
# hello world



# Task 13
name = input("Enter name: ")

print(name * 5)

# Example Output
# Input: Ravi
# RaviRaviRaviRaviRavi



# Task 14
a = input("Enter first string: ")
b = input("Enter second string: ")

print(a + b)

# Example
# hello + world
# helloworld

# Task 31
num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Task 32
marks = int(input("Enter marks: "))

if marks >= 35:
    print("Pass")
else:
    print("Fail")


# Task 33
num = int(input("Enter number: "))

if num > 0:
    print("Positive")
else:
    print("Negative")


# Task 34
num = int(input("Enter number: "))

if num > 10:
    print("Greater than 10")
else:
    print("Not greater than 10")

    # Task 35

age = int(input("Age: "))
height = int(input("Height: "))
weight = int(input("Weight: "))

if age >= 18:
    if height >= 160:
        if weight >= 60:
            print("Selected")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")


# Task 36

marks = int(input("Marks: "))
age = int(input("Age: "))

if marks >= 60:
    if age >= 17:
        print("Admission Granted")
    else:
        print("Age not eligible")
else:
    print("Marks not sufficient")


# Task 37

age = int(input("Age: "))
height = int(input("Height: "))
weight = int(input("Weight: "))

if age >= 16:
    if height >= 150:
        if weight >= 50:
            print("Selected")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")

    # Task 38

day = int(input("Enter number 1-7: "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")


# Task 39

num = int(input("Enter number 1-3: "))

match num:
    case 1:
        print("Red")
    case 2:
        print("Blue")
    case 3:
        print("Green")


# Task 40

num = int(input("Enter number 1-4: "))

match num:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")