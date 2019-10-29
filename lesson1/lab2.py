# Napisz program, który zapyta użytkownika o login i hasło i sprawdzi ich poprawność. 
# Zestaw nazw uzytkownika i hasel przechowuj w dwóch listach. 
# Jeżeli logowanie się udało poinformuj o tym użytkownika.

# Dodaj do swojego programu menu. Użytkownik będzie miał do wyboru dwie opcje 
# (1 - zaloguj, 2 - zarejestruj się). 
# W przypadku rejestracji nazwa użytkownika i hasło zostaną dodane do odpowiednich list.

# Dodaj zabezpieczenia. W polu wyboru opcji możliwe powinno być tylko i wyłącznie 
# podanie wartości '1' lub '2'. Loginy nie mogą się powtarzać w tworzonych strukturach danych. 
# Wartości nie mogą być puste.

#starting lists
login_list = ["kacper", "dupa", "123456"]
password_list = ["acper", "dupa", "654321"]

#user inputs
userInput_option = ""
userInput_login = ""
userInput_password = ""


while True:

    while True: #Menu
        userInput_option = input("Welcome\nPlease select one option:\n\n" + 
        "\t1 - Login\n" + "\t2 - Create new account\n" + 
        "\nInput number and press enter\n")
        if userInput_option == "1" or userInput_option == "2":
            break
        print("You can only select 1 or 2. Please try again.")

    #excluding failed iterations variable - not woring as expected
    isUserLoggedIn = False

    while True: #Logging in
        if userInput_option == "1":
            userInput_login = input("Please enter your login:\n")
            userInput_password = input("Please enter your password:\n")
            for i in range(0, len(login_list)):
                if login_list[i] == userInput_login and password_list[i] == userInput_password:
                    print("You have been logged in succesfully")
                    isUserLoggedIn = True    
            if isUserLoggedIn:        
                break
            else:
                print("User does not exist. Please try again.")

        elif userInput_option == "2":
            print("\nTo create new account please enter requested data:\n")
            while True:
                userInput_login = input("Please enter new login:\n")
                if len(userInput_login) > 0 and userInput_login not in login_list:
                    login_list.append(userInput_login)
                    break
                else:
                    print("Login cannot be empty or it's already in use. Please try again.\n")

            userInput_password = input("Please enter new password:\n")
            password_list.append(userInput_password)
            break
            # how to quit to main loop not at all

    if isUserLoggedIn:
        break