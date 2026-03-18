# 1. Print numbers from 1 to 50
for i in range(1, 51):
    print(i)

# Output:
# 1 2 3 ... 50


# 2. Even numbers 1–100
for i in range(2, 101, 2):
    print(i)

# Output:
# 2 4 6 ... 100


# 3. Odd numbers 1–100
for i in range(1, 101, 2):
    print(i)

# Output:
# 1 3 5 ... 99


# 4. Table of 7
for i in range(1, 11):
    print(7 * i)

# Output:
# 7 14 21 ... 70


# 5. Sum 1–100
total = 0
for i in range(1, 101):
    total += i  # adding each number
print(total)

# Output:
# 5050


# 6. Reverse 50 to 1
for i in range(50, 0, -1):
    print(i)

# Output:
# 50 49 ... 1


# 7. Count numbers divisible by 3
count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count += 1
print(count)

# Output:
# 33


# 8. Squares 1–10
for i in range(1, 11):
    print(i * i)

# Output:
# 1 4 9 ... 100


# 9. Cubes 1–10
for i in range(1, 11):
    print(i ** 3)

# Output:
# 1 8 27 ... 1000


# 10. Input n
n = int(input("Enter n:5"))
for i in range(1, n+1):
    print(i)

# Example Output:
# Input: 5
# 1 2 3 4 5

# 11. Print 1–20
i = 1
while i <= 20:
    print(i)
    i += 1


# 12. Factorial
n = int(input("Enter number:5"))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(fact)

# Example:
# 5 → 120


# 13. Reverse number
num = int(input("Enter number:123 "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print(rev)

# Example:
# 123 → 321


# 14. Count digits
num = int(input("Enter number: "))
count = 0

while num > 0:
    count += 1
    num //= 10

print(count)

# Example:
# 4567 → 4


# 15. Stop input
while True:
    text = input("Enter (type stop to exit): ")
    if text == "stop":
        break

    # 16. *
for i in range(1, 5):
    print("*" * i)

# Output:
# *
# **
# ***
# ****


# 17. Numbers pattern
for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end="")
    print()

# Output:
# 1
# 12
# 123
# 1234


# 18. Tables 1–5
for i in range(1, 6):
    for j in range(1, 6):
        print(i*j, end=" ")
    print()


# 19. A B C
for i in range(3):
    print("A B C")


# 20. Matrix
num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()

# Output:
# 1 2 3
# 4 5 6
# 7 8 9

# 21. Count characters
s = input("Enter string: ")
print(len(s))


# 22. Count vowels
s = input("Enter string: ")
count = 0
for ch in s:
    if ch in "aeiouAEIOU":
        count += 1
print(count)


# 23. Count consonants
count = 0
for ch in s:
    if ch.isalpha() and ch not in "aeiouAEIOU":
        count += 1
print(count)


# 24. Reverse string
s = input("Enter string: ")
rev = ""
for ch in s:
    rev = ch + rev
print(rev)


# 25. Palindrome
s = input("Enter string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

    s = "pythonprogram"

# 26
print(s[:5])

# 27
print(s[-3:])

# 28
print(s[::-1])

# 29
print(s[::2])

# 30
print(s[1:-1])

nums = [10, 20, 30, 40, 50]

# 31 Sum
print(sum(nums))

# 32 Max
print(max(nums))

# 33 Min
print(min(nums))

# 34 Count
print(len(nums))

# 35 Check
print(20 in nums)

nums = []

# 36 Append
nums.append(10)
nums.append(20)
nums.append(30)
print(nums)

# 37 Insert
nums.insert(1, 15)
print(nums)

# 38 Remove
nums.remove(20)
print(nums)

# 39 Reverse without reverse()
rev = []
for i in nums:
    rev = [i] + rev
print(rev)

# 40 Sort without sort()
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
print(nums)