class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        return f"Je m'appelle {self.prenom} {self.nom}."

personne1 = Personne("Dupont", "Pierre")
personne2 = Personne("Martin", "Claire")
personne3 = Personne("Lemoine", "Paul")

print(personne1.SePresenter())
print(personne2.SePresenter())
print(personne3.SePresenter())
