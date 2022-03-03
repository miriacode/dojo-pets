class Ninja():

    def __init__(self, name, last_name, prizes, pet_food, pet):
        self.name = name
        self.last_name = last_name
        self.prizes = prizes
        self.pet_food = pet_food
        self.pet = pet
    

    def walk(self):
        self.pet.play()

    def feed(self):
        self.pet.eat()

    def shower(self):
        self.pet.make_sound()