class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee:
    def __init__(self, employee_id, department):
        self.employee_id = employee_id
        self.department = department

    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}, Department: {self.department}")

    def work(self):
        print("Employee is working.")


class Student:
    def __init__(self, student_id, major):
        self.student_id = student_id
        self.major = major

    def display_student_info(self):
        print(f"Student ID: {self.student_id}, Major: {self.major}")

    def study(self):
        print("Student is studying.")


class PersonInfo(Employee, Student):
    def __init__(self, name, age, employee_id, department, student_id, major):
        Employee.__init__(self, employee_id, department)
        Student.__init__(self, student_id, major)
        Person.__init__(self, name, age)

    def display_person_info(self):
        self.display_employee_info()
        self.display_student_info()



person_info = PersonInfo("Sarthi S Darji", 17, "LULU9", "Finance", "S326", "CSE")

person_info.display_person_info()

person_info.work()
person_info.study()
