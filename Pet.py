class Pet:

    def __init__(self, pet_name,type_of_sound,candy, health, energy):
        self.pet_name = pet_name
        self.type_of_sound = type_of_sound
        self.candy = candy
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health +=10
        return self

    def play(self):
        self.health +=5
        return self

    def make_sound(self):
        print(f'{self.type_of_sound}')
    
    def print_info(self):
        print(f'Pet name: {self.pet_name}, Pet sound: {self.type_of_sound}, Pet candy: {self.candy}, Pet health: {self.health}, Pet energy: {self.energy}')