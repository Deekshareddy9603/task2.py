# ---------------- IMPORTS ----------------
from abc import ABC, abstractmethod
from functools import reduce


# ---------------- TASK 2: ABSTRACTION ----------------
class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass


# ---------------- PARENT CLASS ----------------
class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id


# ---------------- STUDENT ----------------
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)   # Task 1 super()
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"Student: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"


# ---------------- FACULTY ----------------
class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"Faculty: {self.name}, ID: {self.id}, Salary: {self.salary}"


# ---------------- TEMP FACULTY ----------------
class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self):
        return f"TempFaculty: {self.name}, ID: {self.id}, Salary: {self.salary}, Duration: {self.duration}"


# ---------------- DATA ----------------
students = [
    Student("Ravi", 1, "CSE", 60000),
    Student("Meena", 2, "ECE", 45000),
    Student("Arun", 3, "MECH", 70000)
]

faculty = [
    Faculty("Kiran", 101, 40000),
    Faculty("Divya", 102, 25000),
    Faculty("Rahul", 103, 50000)
]


# ---------------- TASK 3: SORTING ----------------
students.sort(key=lambda x: x.fees)
faculty.sort(key=lambda x: x.salary)

print("Sorted Students by Fees:")
for s in students:
    print(s.get_details())

print("\nSorted Faculty by Salary:")
for f in faculty:
    print(f.get_details())


# ---------------- TASK 4: MAP ----------------
student_names = list(map(lambda s: s.name, students))
print("\nStudent Names:", student_names)


# ---------------- TASK 5: FILTER ----------------
high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))

print("\nHigh Fee Students:")
for s in high_fee_students:
    print(s.get_details())

print("\nHigh Salary Faculty:")
for f in high_salary_faculty:
    print(f.get_details())


# ---------------- TASK 6: REDUCE ----------------
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

print("\nTotal Fees Collected:", total_fees)
print("Total Salary:", total_salary)


# ---------------- TASK 7: HIGHER ORDER FUNCTION ----------------
def process_users(users, func):
    return list(map(func, users))


names = process_users(students, lambda s: s.name)
print("\nProcessed Student Names:", names)


# ---------------- FINAL CHALLENGE ----------------
print("\n===== FINAL MINI SYSTEM =====")
print("All Student Details:")
for s in students:
    print(s.get_details())

print("\nAll Faculty Details:")
for f in faculty:
    print(f.get_details())

print("\nFiltered Students (>50000):")
for s in high_fee_students:
    print(s.get_details())

print("\nTotal Fees:", total_fees)
print("Total Salary:", total_salary)