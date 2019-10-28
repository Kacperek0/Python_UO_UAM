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
userInput_option = input("Welcome\nPlease select one option\n" + 
"1 - Login\n" + "2 - Create new account\n" + 
"Input number and press enter\n")
userInput_login = input("Please enter your login:\n")
userInput_password = input("Please enter your password:\n")

while True:
    if userInput_option == "1":

        #excluding failed iterations variable
        loginCheck = False

        # checking if credentials are ok
        for i in range(0, len(login_list)):
            if login_list[i] == userInput_login and password_list[i] == userInput_password:
                print("You has been logged in succesfully")
                loginCheck = True
                break        

        if loginCheck == False:
            print("User does not exist.")
        

    elif userInput_option == "2":
        login_list.append(userInput_login)
        password_list.append(userInput_password)



    


