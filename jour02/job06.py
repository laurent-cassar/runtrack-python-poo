class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut = 'en cours'

    def ajouter_plat(self, nom_plat, prix):
        self.__plats_commandes[nom_plat] = {'prix': prix, 'statut': 'en cours'}

    def annuler_commande(self):
        self.__statut = 'annulée'
        for plat in self.__plats_commandes:
            self.__plats_commandes[plat]['statut'] = 'annulé'

    def calculer_total(self):
        total = sum(plat['prix'] for plat in self.__plats_commandes.values())
        return total

    def afficher_commande(self):
        print(f"Commande {self.__numero_commande}:")
        for plat, details in self.__plats_commandes.items():
            print(f"{plat} - {details['prix']} EUR - Statut: {details['statut']}")
        print(f"Total à payer: {self.calculer_total()} EUR")

    def calculer_tva(self, taux_tva):
        total_ht = self.calculer_total()
        tva = total_ht * taux_tva
        return tva

    def get_statut(self):
        return self.__statut
