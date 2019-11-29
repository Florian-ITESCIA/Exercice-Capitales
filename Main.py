from Villes import Villes
from Capitales import Capitales

v1 = Villes("Toulouse")
v2 = Villes("Strasbourg", 272975)

print(v1)
print(v2)

c1 = Capitales("Paris", "France")
c2 = Capitales("Rome", "Italie", 2700000)

c1.set__nbHabitants(2181371)

print(c1)
print(c2)

print("catégorie de la ville de " + v1.get__Nom() + " : " + v1.Catégorie())
print("catégorie de la ville de " + v2.get__Nom() + " : " + v2.Catégorie())
print("catégorie de la ville de " + c1.get__Nom() + " : " + c1.Catégorie())