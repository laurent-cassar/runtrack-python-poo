import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficherInfos(self):
        print(f"Cercle avec un rayon de {self.rayon} unités.")

    def circonference(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * self.rayon**2

    def diametre(self):
        return 2 * self.rayon

cercle1 = Cercle(4)
cercle2 = Cercle(7)

print("Cercle 1:")
cercle1.afficherInfos()
print(f"Circonférence : {cercle1.circonference():.2f}")
print(f"Diamètre : {cercle1.diametre()}")
print(f"Aire : {cercle1.aire():.2f}\n")

print("Cercle 2:")
cercle2.afficherInfos()
print(f"Circonférence : {cercle2.circonference():.2f}")
print(f"Diamètre : {cercle2.diametre()}")
print(f"Aire : {cercle2.aire():.2f}")
