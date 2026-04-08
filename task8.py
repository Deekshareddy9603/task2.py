import mysql.connector
from abc import ABC, abstractmethod
from functools import reduce

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vinith@9603",
    database="expense_db"
)

cursor = conn.cursor()


# Abstract Class
class BaseReport(ABC):
    @abstractmethod
    def show_report(self):
        pass


# User Class
class User:
    def __init__(self, name):
        self.__name = name   # encapsulation

    def add_user(self):
        sql = "INSERT INTO users(name) VALUES (%s)"
        cursor.execute(sql, (self.__name,))
        conn.commit()
        print(" User added successfully")

    def get_name(self):
        return self.__name


# Expense Class
class Expense(User, BaseReport):
    def __init__(self, name, user_id):
        super().__init__(name)
        self.user_id = user_id

    def add_expense(self):
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")
        date = input("Enter date (YYYY-MM-DD): ")

        sql = """
        INSERT INTO expenses(user_id, amount, category, description, date)
        VALUES (%s,%s,%s,%s,%s)
        """
        cursor.execute(sql, (self.user_id, amount, category, description, date))
        conn.commit()
        print(" Expense added successfully")

    def view_expenses(self):
        sql = """
        SELECT users.name, expenses.amount, expenses.category,
               expenses.description, expenses.date
        FROM expenses
        JOIN users ON users.user_id = expenses.user_id
        WHERE expenses.user_id=%s
        """
        cursor.execute(sql, (self.user_id,))
        data = cursor.fetchall()

        for row in data:
            print(row)

    def filter_by_category(self):
        category = input("Enter category: ")
        sql = "SELECT amount, category FROM expenses WHERE user_id=%s"
        cursor.execute(sql, (self.user_id,))
        data = cursor.fetchall()

        result = list(filter(lambda x: x[1] == category, data))
        print(result)

    def total_expense(self):
        sql = "SELECT amount FROM expenses WHERE user_id=%s"
        cursor.execute(sql, (self.user_id,))
        data = cursor.fetchall()

        amounts = list(map(lambda x: x[0], data))
        total = reduce(lambda a, b: a + b, amounts, 0)
        print(" Total Expense:", total)

    def category_wise(self):
        sql = "SELECT category, amount FROM expenses WHERE user_id=%s"
        cursor.execute(sql, (self.user_id,))
        data = cursor.fetchall()

        result = {}
        for cat, amt in data:
            result[cat] = result.get(cat, 0) + amt

        print(" Category-wise spending")
        for k, v in result.items():
            print(k, ":", v)

    def highest_expense(self):
        sql = "SELECT amount FROM expenses WHERE user_id=%s"
        cursor.execute(sql, (self.user_id,))
        data = cursor.fetchall()

        amounts = list(map(lambda x: x[0], data))
        highest = reduce(lambda a, b: a if a > b else b, amounts)
        print(" Highest Expense:", highest)

    def smart_insight(self):
        sql = "SELECT category, amount FROM expenses WHERE user_id=%s"
        cursor.execute(sql, (self.user_id,))
        data = cursor.fetchall()

        result = {}
        for cat, amt in data:
            result[cat] = result.get(cat, 0) + amt

        highest_cat = max(result, key=result.get)
        print(f" Smart Insight: You are spending too much on {highest_cat}")

    def show_report(self):
        print(" Monthly report feature can be added here")


# MENU
while True:
    print("\n===== SMART EXPENSE MANAGER =====")
    print("1. Add User")
    print("2. Add Expense")
    print("3. View Expenses")
    print("4. Filter by Category")
    print("5. Total Expense")
    print("6. Category Wise Spending")
    print("7. Highest Expense")
    print("8. Smart Insight")
    print("9. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        name = input("Enter user name: ")
        user = User(name)
        user.add_user()

    elif ch in ["2", "3", "4", "5", "6", "7", "8"]:
        uid = int(input("Enter user id: "))
        exp = Expense("temp", uid)

        if ch == "2":
            exp.add_expense()
        elif ch == "3":
            exp.view_expenses()
        elif ch == "4":
            exp.filter_by_category()
        elif ch == "5":
            exp.total_expense()
        elif ch == "6":
            exp.category_wise()
        elif ch == "7":
            exp.highest_expense()
        elif ch == "8":
            exp.smart_insight()

    elif ch == "9":
        print(" Exiting...")
        break