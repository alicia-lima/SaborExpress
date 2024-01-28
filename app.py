import os
import docbr as dbr
from partial import show_subtitle, return_to_menu, format_restaurant
from restaurant import Restaurant

def app_name():
    os.system('cls')
    return """
         ┏━━━┓╋╋┏┓╋╋╋╋╋╋╋┏━━━┓
         ┃┏━┓┃╋╋┃┃╋╋╋╋╋╋╋┃┏━━┛
         ┃┗━━┳━━┫┗━┳━━┳━┓┃┗━━┳┓┏┳━━┳━┳━━┳━━┳━━┓
         ┗━━┓┃┏┓┃┏┓┃┏┓┃┏┛┃┏━━┻╋╋┫┏┓┃┏┫┃━┫━━┫━━┫
         ┃┗━┛┃┏┓┃┗┛┃┗┛┃┃╋┃┗━━┳╋╋┫┗┛┃┃┃┃━╋━━┣━━┃
         ┗━━━┻┛┗┻━━┻━━┻┛╋┗━━━┻┛┗┫┏━┻┛┗━━┻━━┻━━┛
         ╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┃┃
         ╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗┛
             """


def main_menu_option():
    return ("\n"
            "          *** Main Menu ***\n"
            "\n"
            "         1. Register restaurant  \n"
            "         2. List restaurants\n"
            "         3. Modify Status restaurant\n"
            "         4. Modify your registration\n"
            "         5. Exit the program\n"
            "\n"
            "     ")


def modify_menu_option():
    return ("\n"
            "          *** Modify Menu ***\n"
            "\n"
            "         1. Modify Name Restaurant  \n"
            "         2. Modify type of cuisine\n"
            "         3. Modify CNPJ\n"
            "         4. Exit the Modify Menu\n"
            "\n"
            "     ")

def registration_number():
    """ recebe o numero de registro do usuário e o retorna para abrir o restaurante específico para atualizar as
    informações"""
    registration_number = None

    while registration_number is None:
        try:
            registration_number = int(input("What is your registration number? : "))
        except ValueError:
            os.system('cls')
            print("Invalid input. Please enter a number.")
    return registration_number

def choice_option():
    """ recebe a escolha do usuário em ambos os menus do programa"""
    choice = None
    while choice is None:
        try:
            choice = int(input("What would you like to : "))
        except ValueError:
            os.system('cls')
            print("Invalid input. Please enter a number.")
    return choice


"""
para uma validação completa seria necessário uma validação por API cnpj e mais informações de cadastro!
no momento só verifica se um cnpj está incorreto...    
"""


def validate():
    """ recebe o cnpj e valida ele a partir de uma biblioteca para validar documentos brazileiros a docbr e
     modifica o estatus do restaurante no arquivo txt caso o cnpj seja valido """
    show_subtitle("Activation")

    cnpj = dbr.parse(input("Enter the CNPJ of the restaurant: "), doctype='cnpj', mask=True)

    if dbr.validate(cnpj, doctype='cnpj', lazy=False):
        with (open("restaurant.txt", "r") as file):
            linhas = file.readlines()
            find_cnpj = False
            try:
                for i, linha in enumerate(linhas):
                    if cnpj in linha:
                        linhas[i] = linha.replace('Active', 'Inactive'
                                                  )if linha.count('Active'
                                                                  ) > 0 else linha.replace('Inactive', 'Active')
                        print(format_restaurant(linhas[i]))
                        find_cnpj = True
                        break
                if find_cnpj:
                    with open("restaurant.txt", "w") as file:
                        file.writelines(linhas)
                    print("The restaurant has been successfully validated!")
                else:
                    print("The restaurant is not valid! Check your CNPJ and try "
                          "again or modify your registration with a valid CNPJ.")
            except:
                    print("The restaurant is not valid! Check your CNPJ and try "
                          "again or modify your registration with a valid CNPJ.")
            return_to_menu()
    else:
        print("The restaurant is not valid! Check your CNPJ and try "
              "again or modify your registration with a valid CNPJ.")
        return_to_menu()


def access_restaurant(choice):
    """ cria uma string com as informações do restaurante específico escolhido na def registration_number() e inicia
    a modifly_registration() com a escolha do menu de modificações"""
    show_subtitle("Modify your registration")
    info_code = str(registration_number())

    with open("restaurant.txt", "r") as file:
        linhas = file.readlines()
        find_code = False
        not_found_number = False
        for i, restaurant_access in enumerate(linhas):
            restaurant_access = restaurant_access.rstrip()
            if info_code in restaurant_access:
                linhas[i] = restaurant_access
                find_code = True
                break
            elif i == len(linhas) - 1: # FAZ COM O QUE PARE QUANDO CHEGAR NO FIM DO ARQUIVO
                not_found_number = True

    if find_code:
        modify_registration(restaurant_access, choice)

    if not_found_number:
        print("Restaurant not found!")
        return_to_menu()


def modify_registration(restaurant_access, choice):
    """ Modifica o registro da string enviada pela def acess_restaurant e abri o arquivo restaurant.txt  para reescrever
    o arquivo do restaurante específico de acordo com as novas informações fornecidas pelo usuário"""
    if ";" in restaurant_access:
        parts = restaurant_access.split(";")
        if len(parts) == 5:
            number, name, cuisine_type, cnpj, valid = restaurant_access.strip().split(";")
    if choice == 1:
        new_name = input("Please enter with the new restaurant name: ")
        with open("restaurant.txt", "r+") as file:
            content = file.read()
            content = content.replace(f'{name}', f'{new_name}')
            file.seek(0) #MOVE O PONTEIRO DE LEITURA PARA O INICIO DO ARQUIVO
            file.write(content)
            file.truncate() #GARANTE QUE O ARQUIVO TENHA APENAS AS INFORMAÇÕES NOVAS
    if choice == 2:
        new_cuisine = input("Please enter with the new cuisine type: ")
        with open("restaurant.txt", "r+") as file:
            content = file.read()
            content = content.replace(f'{cuisine_type}', f'{new_cuisine}')
            file.seek(0)
            file.write(content)
            file.truncate()
    if choice == 3:
        new_cnpj = input("Please enter with the new CNPJ: ")
        with open("restaurant.txt", "r+") as file:
            content = file.read()
            content = content.replace(f'{cnpj}', f'{new_cnpj}')
            file.seek(0)
            file.write(content)
            file.truncate()

def close_app():
    show_subtitle("Exit the program")

def main_menu():
    """ Menu principal, que direciona para as def de acordo com a escolha do usuário"""
    while True:
        print(app_name())
        print(main_menu_option())
        choice = choice_option()

        if choice == 1:
            Restaurant.register_restaurant()

        elif choice == 2:
            Restaurant.list_restaurants()

        elif choice == 3:
            validate()

        elif choice == 4:
            modify_menu()

        elif choice == 5:
            close_app()
            break

        else:
            show_subtitle("Invalid choice. Please choose a valid option.")
            return_to_menu()


def modify_menu():
    """ Menu de modificações, que direciona para as def de acordo com a escolha do usuário"""
    while True:
        print(app_name())
        print(modify_menu_option())
        choice = choice_option()

        if choice == 1:
            access_restaurant(choice=1)

        elif choice == 2:
            access_restaurant(choice=2)

        elif choice == 3:
            access_restaurant(choice=3)

        elif choice == 4:
            main_menu()

        else:
            show_subtitle("Invalid choice. Please choose a valid option.")
            return_to_menu()


if __name__ == "__main__":
    main_menu()
