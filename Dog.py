from Pet import Pet
class Dog(Pet):
    def __init__(self,pet_name,type_of_sound,candy, health, energy, breed):
        super().__init__(pet_name,type_of_sound,candy, health, energy)
        self.breed = breed

    def print_dog_info(self):
        print(f'Pet name: {self.pet_name}, Pet sound: {self.type_of_sound}, Pet candy: {self.candy}, Pet health: {self.health}, Pet energy: {self.energy}, Dog breed: {self.breed}')
