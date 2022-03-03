from Ninja import Ninja
from Pet import Pet
from Dog import Dog

doki = Pet("Doki","bark","none",0,0)
miriam = Ninja("Miriam", "Acuna",1, "Pedigree high protein", doki)

miriam.feed()
doki.print_info()
doki.print_info()
miriam.walk()
doki.print_info()
miriam.shower()


#Bonus sensei
lula = Dog("Lula","bark","none",0,0,"labrador")
elissa = Ninja("Elissa", "Espinoza",1,"Pedigree high protein", lula)
lula.print_dog_info()