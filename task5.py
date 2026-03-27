# Create user function
def create_user(name, age, role):
    return {
        "name": name.title(),
        "age": age,
        "role": role
    }

# Store users
users = []
users.append(create_user("ravi", 22, "developer"))
users.append(create_user("meena", 21, "tester"))

# Print users
for u in users:
    print(u)

    

#Dynamic Calculator
def calculate_total(*numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg

result = calculate_total(10, 20, 30, 40)
print("Sum:", result[0])
print("Average:", result[1])



#Keyword Config System(**Kwargs)
def system_config(**settings):
    for key, value in settings.items():
        print(key, ":", value)

system_config(mode="debug", version="1.0")




#Factorial(Recursion)
def factorial(n):
    if n < 0:
        return "Error: Negative number"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
print(factorial(0))
print(factorial(-2))



#Generator
def square_generator(n):
    for i in range(1, n+1):
        yield i*i

gen = square_generator(5)

print("Generator type:", type(gen))

for val in gen:
    print(val)



#Exception Handling
try:
    num = int(input("Enter numerator: "))
    den = int(input("Enter denominator: "))
    print("Result:", num / den)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")

finally:
    print("Program Completed")



#File Handling
# Write to file
file = open("team_data.txt", "w")
file.write("Ravi, Developer\nMeena, Tester\n")
file.close()

# Read file
file = open("team_data.txt", "r")
content = file.read()
print(content)

# Check file closed
file.close()
print("File closed:", file.closed)