class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def afficher(self):
        print(f"nombre1: {self.nombre1}, nombre2: {self.nombre2}")

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(f"Le résultat de l'addition est : {resultat}")

operation = Operation(12,3)

operation.addition()
