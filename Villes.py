class Villes:

    def __init__(self,Nom,nbHabitants = 0):
        self.nom = Nom
        self.nbHabitants = nbHabitants

    def get__Nom(self):
        return self.nom
    def get__nbHabitants(self):
        return self.nbHabitants

    def set__Nom(self,Nom):
        self.nom = Nom
    def set__nbHabitants(self,nbHabitants):
        self.nbHabitants = nbHabitants

    def nbHabitantsConnu(self):
        if self.nbHabitants != 0:
            return 'vrai'
        else:
            return 'faux'

    def Catégorie(self):
        if self.nbHabitants == 0:
            return "?"
        if self.nbHabitants < 500000:
            return "A"
        if self.nbHabitants >= 500000:
            return "B"

    def __str__(self) :
        if self.nbHabitantsConnu() == 'vrai':
            return "Ville de " + self.nom + " ; " + str(self.nbHabitants) + " habitants."
        else:
            return "Ville de " + self.nom