class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def makeSound(self):
        pass

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def makeSound(self):
        return "Woof!"

    def wagTail(self):
        return f"{self.name} is wagging its tail."

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def makeSound(self):
        return "Meow!"

    def purr(self):
        return f"{self.name} is purring."

dogObj = Dog(name="dog", age=3, breed="something")
catObj = Cat(name="cat", age=3, color="xyz")

print(f"{dogObj.name} is a {dogObj.breed}. {dogObj.makeSound()}")
print(dogObj.wagTail())

print(f"{catObj.name} is {catObj.color}. {catObj.makeSound()}")
print(catObj.purr())
