# ---------------- TASK 1: ENCAPSULATION ----------------

class User:
    def __init__(self):
        self.__user_name = ""
        self.__pwd = ""

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name   # password hidden

    def register(self):
        print("Registering user:", self.__user_name)

    def login(self):
        print("Logging in:", self.__user_name)


u1 = User()
u1.set_user("john", "1234")
u1.register()
u1.login()


# ---------------- TASK 2: INHERITANCE ----------------

class User:
    def register(self):
        print("User Registered")

    def login(self):
        print("User Logged In")


class Student(User):
    def student_greet(self):
        print("Hello Student")


class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")


class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")


s = Student()
s.register()
s.login()
s.student_greet()

f = Faculty()
f.register()
f.faculty_greet()

t = TempFaculty()
t.register()
t.faculty_greet()
t.tempFaculty_greet()

# ---------------- TASK 3: METHOD OVERRIDING ----------------

class User:
    def greet(self):
        print("Welcome User")


class Student(User):
    def greet(self):
        print("Welcome Student")


class Faculty(User):
    def greet(self):
        print("Welcome Faculty")


student = Student()
faculty = Faculty()

student.greet()
faculty.greet()

# ---------------- TASK 4: METHOD CHAINING ----------------

class User:
    def login(self):
        print("logined")
        return self

    def greet(self):
        print("enjoy everyone")
        return self

    def register(self):
        print("registered")
        return self


user = User()
user.login().greet().register()

 #---------------- TASK 5: COMBINED TASK ----------------

class User:
    users_count = 0

    def __init__(self, name):
        self.__name = name
        User.users_count += 1

    def login(self):
        print(self.__name, "logged in")
        return self

    def greet(self):
        print("Welcome User")
        return self

    def register(self):
        print(self.__name, "registered")
        return self


class Student(User):
    def greet(self):
        print("Welcome Student")
        return self


class Faculty(User):
    def greet(self):
        print("Welcome Faculty")
        return self


stu = Student("Ravi")
fac = Faculty("Meena")

stu.login().greet().register()
fac.login().greet().register()

print("Total users:", User.users_count)