# Class Ville (City)
class Ville:
    def __init__(self, nom, habitants):
        self.__nom = nom  # Private attribute for city name
        self.__habitants = habitants  # Private attribute for the number of inhabitants
    
    def get_habitants(self):
        # Getter to access the number of inhabitants
        return self.__habitants
    
    def ajouter_population(self):
        # Method to increase the population of the city by 1
        self.__habitants += 1

# Class Personne (Person)
class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom  # Private attribute for person's name
        self.__age = age  # Private attribute for person's age
        self.__ville = ville  # Link to the city object where the person lives
        
    def ajouter_population(self):
        # Method to increase the city's population when a new person arrives
        self.__ville.ajouter_population()

# Creating Ville objects (cities)
paris = Ville("Paris", 1000000)  # Paris with 1,000,000 inhabitants
marseille = Ville("Marseille", 861635)  # Marseille with 861,635 inhabitants

# Display the initial number of inhabitants in each city
print(f"Nombre d'habitants à Paris : {paris.get_habitants()}")
print(f"Nombre d'habitants à Marseille : {marseille.get_habitants()}")

# Creating Personne objects (people)
john = Personne("John", 45, paris)  # John, 45 years old, living in Paris
myrtille = Personne("Myrtille", 4, paris)  # Myrtille, 4 years old, living in Paris
chloe = Personne("Chloé", 18, marseille)  # Chloé, 18 years old, living in Marseille

# Adding the people to the respective cities, increasing their populations
john.ajouter_population()  # John arrives in Paris
myrtille.ajouter_population()  # Myrtille arrives in Paris
chloe.ajouter_population()  # Chloé arrives in Marseille

# Display the number of inhabitants after the new arrivals
print(f"Nombre d'habitants à Paris après l'arrivée de John et Myrtille : {paris.get_habitants()}")
print(f"Nombre d'habitants à Marseille après l'arrivée de Chloé : {marseille.get_habitants()}")