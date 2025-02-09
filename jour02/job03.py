class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        if nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            self.__nb_pages = 0
        self.__disponible = True

    def get_titre(self):
        return self.__titre

    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nb_pages(self):
        return self.__nb_pages

    def set_nb_pages(self, nb_pages):
        if nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")
    
    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():
            self.__disponible = False
        else:
            print("Erreur : Le livre n'est pas disponible.")

    def rendre(self):
        if not self.__disponible:
            self.__disponible = True
        else:
            print("Erreur : Le livre n'a pas été emprunté.")
