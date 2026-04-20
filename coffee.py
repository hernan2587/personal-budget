"""

Course ADD_100
Hernan Ramoz 
ASSIGNMENT 13A: Object practice
1. Header Docstring included.
2. Define a class for a part of your project using PascalCase.
3. Use _init_ to set private attributes (__variable).
4. Write Setters and Getters for the attributes.
5. Write a summary function that returns a formatted description.
6. Instantiate two distinct objects and print their summaries.
This program defines a Coffee class that stores and displays coffee order details such as type, size, and milk using objects.

"""

class Coffee:
    def __init__(self, coffee_type, size, milk):
        # Atributos privados con doble guion bajo
        self.__coffee_type = coffee_type
        self.__size = size
        self.__milk = milk

    # --- Getters (Para obtener los valores) ---
    def get_coffee_type(self):
        return self.__coffee_type

    def get_size(self):
        return self.__size

    def get_milk(self):
        return self.__milk

    # --- Setters (Para modificar los valores) ---
    def set_size(self, new_size):
        self.__size = new_size

    # --- Summary Method ---
    def get_summary(self):
        return f"Order Summary: {self.__size} {self.__coffee_type} with {self.__milk} milk."

# --- Instanciando dos objetos distintos ---
coffee1 = Coffee("Latte", "Large", "Whole")
coffee2 = Coffee("Espresso", "Small", "No")

# Imprimir los resúmenes
print(coffee1.get_summary())
print(coffee2.get_summary())