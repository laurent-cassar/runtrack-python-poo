class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
    
    def afficher(self):
        print(f"Compte n°: {self.__numero_compte}")
        print(f"Nom: {self.__nom} {self.__prenom}")
        print(f"Solde: {self.__solde} EUR")
        print(f"Découvert autorisé: {'Oui' if self.__decouvert else 'Non'}")
    
    def afficherSolde(self):
        print(f"Le solde du compte est de {self.__solde} EUR.")
    
    def versement(self, montant):
        if montant > 0:
            self.__solde += montant
            print(f"Versement de {montant} EUR effectué. Nouveau solde: {self.__solde} EUR.")
        else:
            print("Le montant du versement doit être positif.")
    
    def retrait(self, montant):
        if montant > 0:
            if self.__solde - montant < 0 and not self.__decouvert:
                print("Erreur : Solde insuffisant et découvert non autorisé.")
            else:
                self.__solde -= montant
                print(f"Retrait de {montant} EUR effectué. Nouveau solde: {self.__solde} EUR.")
        else:
            print("Le montant du retrait doit être positif.")
    
    def agios(self):
        if self.__solde < 0:
            agios_montant = abs(self.__solde) * 0.1
            self.__solde -= agios_montant
            print(f"Agios de {agios_montant} EUR appliqués. Nouveau solde: {self.__solde} EUR.")
    
    def virement(self, montant, compte_destinataire):
        if montant > 0:
            if self.__solde - montant < 0 and not self.__decouvert:
                print("Erreur : Solde insuffisant pour effectuer le virement.")
            else:
                self.__solde -= montant
                compte_destinataire.versement(montant)
                print(f"Virement de {montant} EUR effectué vers le compte {compte_destinataire.__numero_compte}.")
        else:
            print("Le montant du virement doit être positif.")

compte1 = CompteBancaire(numero_compte="12345", nom="Dupont", prenom="Jean", solde=1000)
compte2 = CompteBancaire(numero_compte="67890", nom="Martin", prenom="Paul", solde=-200, decouvert=True)

compte1.afficher()
compte2.afficher()

compte1.versement(500)
compte1.retrait(300)
compte2.agios()

compte1.virement(700, compte2)

compte1.afficherSolde()
compte2.afficherSolde()
