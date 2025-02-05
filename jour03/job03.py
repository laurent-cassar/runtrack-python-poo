class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut
    
    def __str__(self):
        return f"Tâche: {self.titre}, Description: {self.description}, Statut: {self.statut}"

class ListeDeTaches:
    def __init__(self):
        self.taches = []
    
    def ajouterTache(self, tache):
        self.taches.append(tache)
    
    def supprimerTache(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                self.taches.remove(tache)
                print(f"Tâche '{titre}' supprimée.")
                return
        print(f"Tâche '{titre}' non trouvée.")
    
    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "terminée"
                print(f"Tâche '{titre}' marquée comme terminée.")
                return
        print(f"Tâche '{titre}' non trouvée.")
    
    def afficherListe(self):
        if not self.taches:
            print("Aucune tâche dans la liste.")
        for tache in self.taches:
            print(tache)
    
    def filterListe(self, statut):
        filtered_taches = [tache for tache in self.taches if tache.statut == statut]
        if not filtered_taches:
            print(f"Aucune tâche avec le statut '{statut}'.")
        for tache in filtered_taches:
            print(tache)

tache1 = Tache("Acheter du pain", "Aller au supermarché acheter du pain")
tache2 = Tache("Répondre aux emails", "Répondre à tous les emails urgents")
tache3 = Tache("Faire du sport", "Aller courir pendant 30 minutes", "terminée")

liste = ListeDeTaches()

liste.ajouterTache(tache1)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)

print("Toutes les tâches :")
liste.afficherListe()

print("\nSuppression de la tâche 'Répondre aux emails' :")
liste.supprimerTache("Répondre aux emails")

print("\nListe après suppression :")
liste.afficherListe()

print("\nMarquer la tâche 'Acheter du pain' comme terminée :")
liste.marquerCommeFinie("Acheter du pain")

print("\nListe des tâches à faire :")
liste.filterListe("à faire")

print("\nListe des tâches terminées :")
liste.filterListe("terminée")

print("\nToutes les tâches après modification :")
liste.afficherListe()
