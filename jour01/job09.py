class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        prixTTC = self.prixHT * (1 + self.TVA / 100)
        return prixTTC

    def afficher(self):
        return f"Produit: {self.nom}, Prix HT: {self.prixHT}€, TVA: {self.TVA}%, Prix TTC: {self.CalculerPrixTTC()}€"

    def modifier_nom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifier_prix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def get_nom(self):
        return self.nom

    def get_prixHT(self):
        return self.prixHT

    def get_TVA(self):
        return self.TVA

    def get_prixTTC(self):
        return self.CalculerPrixTTC()


produit1 = Produit("Produit A", 100, 20)
produit2 = Produit("Produit B", 150, 10)

print(produit1.afficher())
print(produit2.afficher())

produit1.modifier_nom("Produit A modifié")
produit1.modifier_prix(120)
produit2.modifier_nom("Produit B modifié")
produit2.modifier_prix(180)

print(produit1.afficher())
print(produit2.afficher())
