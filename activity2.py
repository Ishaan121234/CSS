class Parrot:
    species = "bird"

    def __init__(self,name,age):
        """Runs by itself every time a Parrot is made: Parrot("Blu", 10)"""
        self.name = name
        if age < 0:
            age = 0
        self.age = age


parrot_name = input("Name of the first Parrot??")
blu = Parrot(parrot_name, 10)
woo = Parrot("Woo", 15)
print(blu.name, "is a ", blu.species)
print(woo.name, "is also a ", Parrot.species)
print(blu.name, "is", blu.age, "years old")
print(woo.name, "is", woo.age, "years old")


ghost = Parrot("Ghost", -3)
print(ghost.name, "is" ,ghost.age, "years old")