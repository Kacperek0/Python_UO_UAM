def read_file(path):
    data = {}
    file = open(path)
    lines = file.readlines()
    file.close()
    for line in lines:
        tab = line.strip().split("\t")
        data[tab[0]] = (tab[1], tab[2], tab[3])
    return data

def modify_or_add_id(p_id, dictionary, new_data):
    dictionary[p_id] = new_data
    return dictionary

def delete_p_id(p_id, dictionary):
    del dictionary[p_id]
    return dictionary

def save_to_file(path, dictionary):
    file = open(path, "w")
    for key, value in dictionary.items():
        file.write("{}\t{}\t{}\t{}".format(key, value[0], value[1], value[2]))
    file.close()
    
def run():
    dictionary = read_file("osoby.txt")
    while True:
        option = input("Menu:\n1 - Pokaż zawartość bazy\n2 - Modyfikuj po ID\n3 - Usun po ID\n4 - Dodaj\n5 - Zapisz\n6 - Zamknij\n")
        if (option == "1"):
            for key, value in dictionary.items():
                print("{} {} {} {}".format(key, value[0], value[1], value[2]))
        elif (option == "2"):
            current_id = input("Podaj id do modyfikacji")
            while current_id not in dictionary.keys():
                current_id = input("Podaj POPRAWNE id do modyfikacji")
            name = input("Podaj imie")
            surname = input("Podaj nazwisko")
            date = input("Podaj date urodzenia")
            dictionary = modify_or_add_id(current_id, dictionary,  (name, surname, date))
        elif (option == "3"):
            current_id = input("Podaj id do usuniecia")
            while current_id not in dictionary.keys():
                current_id = input("Podaj POPRAWNE id do usuniecia")
            dictionary = delete_p_id(current_id, dictionary)
        elif (option == "4"):
            new_id = input("Podaj id")
            name = input("Podaj imie")
            surname = input("Podaj nazwisko")
            date = input("Podaj date urodzenia")
            dictionary = modify_or_add_id(current_id, dictionary,  (name, surname, date))
        elif (option == "5"):
            save_to_file("osoby.txt", dictionary)
        elif (option == "6"):
            break

run()