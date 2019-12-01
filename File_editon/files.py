"""Zadanie 1
Utwórz plik tekstowy zawierający informację o uczestnikach danego wydarzenia, 
składający się z czterech kolumn: unikalny identyfikator, Imię, Nazwisko, Data urodzenia. 
Użytkownik po uruchomieniu programu powinien mieć możliwość dodawania, 
usuwania oraz modyfikowania rekordów. Zmodyfikowana baza danych powinna byc wczytywana do 
tego samego pliku, z którego została wczytana.
Dla chętnych:
Zapisuj w obrębie pliku z bazą także poprzednie jej wersje, pozwól 
użytkownikowi wczytać wersję z konkretnego dnia lub poinformuj że taka wersja nie istnieje. 
Dodaj dodatkową opcję - sprawdzanie pełnoletności dla danego użytkownika (użyj modułu datetime)."""

def OpenFile(path):
    fl = open(path, "w+")
    fl.write("UID;Name;Surname;Birthdate")
    fl.close()

def ViewFile(path):
    fl = open(path)
    for lines in fl:
        print(lines + "\n")


def AddRecord(path):
    fl = open(path, "a")
    uid = str(input("Please enter UID: "))
    name = str(input("Please enter Name: "))
    surname = str(input("Please inter Surname: "))
    birthdate = str(input("Please input birthdate: "))
    fl.writelines("{};{};{};{};\n".format(uid,name,surname,birthdate))
    fl.close()

def DeleteRecord(path):
    fl = open(path, "w+")
    uid = int(input("Please enter UID of a record you'd like to delete: "))
    for lines in fl:
        if (lines[0:2] == uid):
            print(lines)
    



path = "/Users/Kacper/Documents/Repos/Python_UO_UAM/File_editon/test.csv"

OpenFile(path)
ViewFile(path)
AddRecord(path)
ViewFile(path)
DeleteRecord(path)



