from partial import show_subtitle, return_to_menu, format_restaurant
import docbr as dbr
import random

class Restaurant:
    """ representa um restaurante """
    def __init__(self, registration_number, restaurant_name, cuisine_type, document):
        """ Inicializa um restaurante e suas caracteristicas esperadas"""
        self.registration_number = registration_number
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.document = document
        self.valid = 'Inactive'

    @classmethod
    def register_restaurant(cls):
        """ registra um restaurante em um arquivo txt a partir das informações fornecidas pelo usuário,
        com um número de regristo único e aleátorio."""
        show_subtitle("Restaurants Registration")
        registration_number = random.randint(100000, 999999)
        restaurant_name = input("Enter the name of the restaurant: ").title()
        cuisine_type = input("Enter the type of cuisine: ").title()
        document = dbr.parse(input("Enter the CNPJ of the restaurant: "), doctype='cnpj', mask=True)

        with open("restaurant.txt", "r") as file:
            while registration_number in file:
                registration_number = random.randint(100000, 999999)

        restaurant = Restaurant(registration_number, restaurant_name, cuisine_type, document)
        with open("restaurant.txt", "a") as file:
            file.write(f'{registration_number};{restaurant.restaurant_name}; {restaurant.cuisine_type};'
                       f'{restaurant.document};{restaurant.valid}\n')
            print("Restaurant added to the file successfully!")

            return_to_menu()
            return [restaurant]

    @classmethod
    def list_restaurants(cls):
        """ Cria uma lista de restaurantes registrado a partir de um arquivo txt"""
        show_subtitle("Restaurants")

        with open("restaurant.txt", "r") as file:
            restaurant_list = []
            for restaurant in file:
                formatted_restaurant = format_restaurant(restaurant)
                restaurant_list.append(formatted_restaurant)
                print(formatted_restaurant)
        return_to_menu()
        return restaurant_list
