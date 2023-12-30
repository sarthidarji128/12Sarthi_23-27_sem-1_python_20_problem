class Shoe:
    def __init__(self,color, brand):
        self.color = color
        self.brand = brand
        
    def add_shoe(self, shoeType):
        print(f"{shoeType.color} {shoeType.brand} shoes added to store!")
    

class Converse(Shoe):
    def __init__(self, color,lowOrHighTop,tongueColor):
        super().__init__(color, brand="Converse")
        self.lowOrHighTop = lowOrHighTop
        self.tongueColor = tongueColor
    

    def add_shoe(self, shoeType):
        print(f"{shoeType.color} {shoeType.lowOrHighTop}-top {shoeType.tongueColor} tongue-color {self.brand} added to store!")


class CombatShoe(Shoe):
    def __init__(self, color, brand, militiaryBranch, jungleOrDesert):
        super().__init__(color, brand)
        self.militiaryBranch = militiaryBranch
        self.jungleOrDesert = jungleOrDesert

    def add_shoe(self, shoeType):
        print(f"{shoeType.color} {shoeType.brand} {self.militiaryBranch} {self.jungleOrDesert}-camo combat boots added to store")


class Sandal(Shoe):
    def __init__(self, color, brand, openOrClosedToe, waterproof):
        super().__init__(color, brand)
        self.openOrClosedToe = openOrClosedToe
        self.waterproof = waterproof
    
    def add_shoe(self, shoeType):
        print(f"{shoeType.color} {shoeType.brand} {self.openOrClosedToe}-toe {self.waterproof} sandals added to store!")

print("----WELCOME TO THE SHOE-STOP(Admin Side)----")

while True:
    print("\n\n1)Regular Shoes")
    print("2)Converse Shoes")
    print("3)Combat Shoes")
    print("4)Sandals")
    choice = int(input("\nWhat do you want to add: "))

    if choice == 1:
        color = input("\nEnter color of shoe: ").capitalize()
        brand = input("Enter brand: ").capitalize()
        shoe = Shoe(color, brand)
        shoe.add_shoe(shoe)
    
    elif choice==2:
        print("\nWelcome to the Converse section!\n")
        color = input("Enter color of converse: ").capitalize()
        low_or_high = input("Is it Low or High Top? (Type 'Low' or 'High'): ").capitalize()
        tongue_col = input("What is the color of Tongue? (Type 'Blue', 'Green', 'Red', 'Yellow', 'Black': ").capitalize()
        converse = Converse(color, low_or_high, tongue_col)
        converse.add_shoe(converse)
        
    
    elif choice==3:
        print("\nWelcome to Combat Shoes Section!\n")
        color = input("Enter color of combat shoe: ").capitalize()
        brand = input("Enter brand of shoe: ").capitalize()
        military_branch = input("Which branch does this belong to?(USAF/USMC/USN/USCG/USAR): ").capitalize()
        jd = input("Does it have Jungle or Desert camouflage? (Jungle/Desert): ").capitalize()
        combat_shoe = CombatShoe(color, brand, military_branch, jd)
        combat_shoe.add_shoe(combat_shoe)
    

    elif choice == 4:
        print("\nWelcome to the Sandals Section\n")
        color = input("Enter color of sandals: ").capitalize()
        brand = input("Enter brand of sandals: ").capitalize()
        openOrClosed = input("Open or closed toe? 'open' / 'closed' : ").lower()
        waterProof = input("Is it Waterproof? Type 'Yes'/'No': ").lower()
        if waterProof == 'yes':
            waterProof = 'Waterproof'
        elif waterProof == "no":
            waterProof = "Non waterproof"
        else:
            print("Invalid choice")
        sandal = Sandal(color, brand, openOrClosed, waterProof)
        sandal.add_shoe(sandal)

