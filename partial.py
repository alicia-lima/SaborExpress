import os

def show_subtitle(txt):
    """ recebe o texto de mensagem e limpa a tela antes de mostrar o texto"""
    os.system('cls')
    linha = '*' * (len(txt) + 8)
    print(linha)
    print(f"*** {txt} ***")
    print(linha + "\n\n")

def return_to_menu():
    return input("\n\nPress Enter to return to the menu... ")

def format_restaurant(restaurant):
    """ Cria uma string com todas as informações do restaurante"""
    if ";" in restaurant:
        parts = restaurant.strip().split(";")
        if len(parts) == 5:
            restaurant_number, restaurant_name, cuisine_type, cnpj, valid = restaurant.strip().split(";")
            formatted_restaurant = (f" \nRegistration number: {restaurant_number} \n"
                                    f"Restaurant Name: {restaurant_name} \n"
                                    f"Cuisine Type: {cuisine_type} \n"
                                    f"CNPJ: {cnpj}\n"
                                    f"Activate: {valid}")
            return formatted_restaurant