class Student:
    def __init__(self, first_name, last_name, student_id):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_id = student_id
        self.__credits = 0
        self.__level = self.__student_eval()

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__student_eval()  # Mise à jour du niveau après chaque ajout de crédits
        else:
            print("Le nombre de crédits doit être supérieur à zéro.")

    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        print(f"Nom : {self.__last_name}")
        print(f"Prénom : {self.__first_name}")
        print(f"Numéro d'étudiant : {self.__student_id}")
        print(f"Nombre de crédits : {self.__credits}")
        print(f"Niveau : {self.__level}")

# Instanciation d'un objet Student
john_doe = Student("John", "Doe", 145)

# Ajout de crédits
john_doe.add_credits(30)
john_doe.add_credits(25)
john_doe.add_credits(40)

# Affichage des informations de l'étudiant
john_doe.student_info()
