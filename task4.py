# -------------PROJECT 1: EMPLOYEE --------------
employees = []

def add_employee():
    name = input("Name: ")
    age = int(input("Age: "))
    role = input("Role: ")
    salary = float(input("Salary: "))
    employees.append({"name": name, "age": age, "role": role, "salary": salary})
    print("Employee Added!")

def update_employee():
    name = input("Enter name to update: ")
    for emp in employees:
        if emp["name"] == name:
            emp["salary"] = float(input("New Salary: "))
            print("Updated!")
            return
    print("Not Found")

def delete_employee():
    name = input("Enter name to delete: ")
    for emp in employees:
        if emp["name"] == name:
            employees.remove(emp)
            print("Deleted!")
            return
    print("Not Found")

def show_employees():
    for emp in employees:
        print(emp)


# ---------------- PROJECT 2: REPORT CARD ---------------
    name = input("Name: ")
    m1 = int(input("M1: "))
    m2 = int(input("M2: "))
    m3 = int(input("M3: "))
    total = m1 + m2 + m3
    avg = total / 3

    print(f"Total: {total}, Average: {avg}")

    if avg >= 90:
        print("Grade A")
    elif avg >= 70:
        print("Grade B")
    else:
        print("Grade C")


# ------------PROJECT 3: SHOPPING CART ----------
cart = []

def add_item():
    name = input("Product: ")
    price = float(input("Price: "))
    qty = int(input("Qty: "))
    cart.append({"name": name, "price": price, "qty": qty})

def show_cart():
    total = 0
    for item in cart:
        total += item["price"] * item["qty"]
        print(item)
    print("Total Bill:", total)

def remove_item():
    name = input("Remove item: ")
    for item in cart:
        if item["name"] == name:
            cart.remove(item)
            print("Removed!")
            return


# -----------PROJECT 4: LOGIN ------------
users = {"admin": "1234"}

def login():
    u = input("Username: ")
    p = input("Password: ")
    if u in users and users[u] == p:
        print("Login Success")
    else:
        print("Login Failed")


# ----------PROJECT 5: VISITOR ----------
visitors = set()

def add_visitor():
    name = input("Visitor: ")
    visitors.add(name)

def show_visitors():
    print("Visitors:", visitors)
    print("Total:", len(visitors))


# ------------PROJECT 6: STRING FORMAT -------------
def formatter():
    name = input("Name: ")
    product = input("Product: ")

    print(f"{name} bought {product}")
    print(name.ljust(10, "*"))
    print(name.rjust(10, "*"))
    print(name.center(10, "*"))


# -----------PROJECT 7: BANK --------------
account = {"name": "User", "balance": 1000}

def deposit():
    amt = int(input("Deposit: "))
    account["balance"] += amt

def withdraw():
    amt = int(input("Withdraw: "))
    if amt <= account["balance"]:
        account["balance"] -= amt
    else:
        print("Insufficient Balance")

def check_balance():
    print(account)


# ----------PROJECT 8: VOTING ----------
votes = {"A": 0, "B": 0}

def vote():
    choice = input("Vote A/B: ")
    if choice in votes:
        votes[choice] += 1

def result():
    print(votes)
    print("Winner:", max(votes, key=votes.get))


# -----------ROJECT 9: COURSE ---------------
students = {}

def add_student():
    name = input("Name: ")
    courses = input("Courses (comma): ").split(",")
    students[name] = courses

def show_students():
    print(students)


# ----------------PROJECT 10: NUMBER TOOL ---------------
def number_tool():
    num = int(input("Enter number: "))
    print("Binary:", bin(num))
    print("Octal:", oct(num))
    print("Hex:", hex(num))
    print("Comma:", format(num, ","))
    print("Scientific:", "{:.2e}".format(num))


# ------------ MENU -----------
while True:
    print("\n===== MENU =====")
    print("1.Employee")
    print("2.Report Card")
    print("3.Cart")
    print("4.Login")
    print("5.Visitors")
    print("6.String Format")
    print("7.Bank")
    print("8.Voting")
    print("9.Course")
    print("10.Number Tool")
    print("0.Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        add_employee()
        show_employees()
    elif ch == "3":
        add_item()
        show_cart()
    elif ch == "4":
          login()
    elif ch == "5":
        add_visitor()
        show_visitors()
    elif ch == "6":
        formatter()
    elif ch == "7":
        deposit()
        withdraw()
        check_balance()
    elif ch == "8":
        vote()
        result()
    elif ch == "9":
        add_student()
        show_students()
    elif ch == "10":
        number_tool()
    elif ch == "0":
        break
    else:
        print("Invalid")