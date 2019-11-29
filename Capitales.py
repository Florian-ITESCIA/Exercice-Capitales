from Villes import Villes

class Capitales(Villes) :

    def __init__(self,Nom,Pays,nbHabitants = 0):
        Villes.__init__(self,Nom,nbHabitants)
        self.pays = Pays

    def get__Pays(self):
        return self.pays

    def set__Pays(self,Pays):
        self.pays = Pays

    def Catégorie(self):
        if self.pays != "":
            return "C"

    def __str__(self):
        return Villes.__str__(self) + " Capitale de " + self.pays