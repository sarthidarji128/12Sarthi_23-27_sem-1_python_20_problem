from datetime import datetime

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob, "%Y-%m-%d")

    def calculate_age(self):
        today = datetime.now()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return age


person1 = Person("Sarthi Sanjay Bhai Darji", "India", "2006-08-12")

print(f"Name: {person1.name}")
print(f"Country: {person1.country}")
print(f"Date of Birth: {person1.dob.strftime('%Y-%m-%d')}")

age = person1.calculate_age()
print(f"Age: {age} years")
