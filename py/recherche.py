from os.path import exists, isdir
from os import listdir, system
from time import sleep

def get_domains(filename):
    domains = []
    
    with open(filename, encoding="utf8", errors="ignore") as f:
        datafile = f.readlines()

    for line in datafile:
        if "**Domaine(s)**" in line:
            domains.append(line[17:].split(" / "))
    
    return domains, filename

def clear():
    system("cls")

options = ["Verifier qu'un fichier existe", "Faire une recherche par domaine"]

dirs = listdir("C:\\Users\\ROMAIN\\OneDrive\\Projets\\Dico-abreviations-et-acronymes\\Dico")

files_list = []
for dir_ in dirs:
    files_list.append(listdir("C:\\Users\\ROMAIN\\OneDrive\\Projets\\Dico-abreviations-et-acronymes\\Dico\\" + dir_))

files = []
for list_ in files_list:
    for i in range(len(list_)):
        files.append(list_[i])

print("Bonjour. Bienvenue dans ce programme.")

restart = "o"

while restart == "o":
    clear()

    print("Que voulez-vous faire ?")

    for i in range(len(options)):
        print(str(i + 1) + ". " + options[i])

    choix = input()

    if choix == "1":
        clear()

        print("Vous avez choisi de " + options[0].lower() + ".\n")
    
        print("Quelle est l'abreviation ou acronyme dont vous voulez verifier l'existence ?")

        searched = input()

        # Cree le chemin a partir de l'abreviation entree
        path = "C:\\Users\\ROMAIN\\OneDrive\\Projets\\Dico-abreviations-et-acronymes\\Dico\\" + searched[0].upper() + "\\" + searched.lower() + ".md"

        # Verifie que le chemin cree existe dans le dictionnaire
        if exists(path):
            print("Le fichier existe !")
        else:
            print("Le fichier n'existe pas.")

    if choix == "2":
        clear()

        dirs = listdir("C:\\Users\\ROMAIN\\OneDrive\\Projets\\Dico-abreviations-et-acronymes\\Dico")

        files_list = []
        for dir_ in dirs:
            files_list.append(listdir("C:\\Users\\ROMAIN\\OneDrive\\Projets\\Dico-abreviations-et-acronymes\\Dico\\" + dir_))

        files = []
        for list_ in files_list:
            for i in range(len(list_)):
                files.append(list_[i])

        print("Vous avez choisi de " + options[1].lower() + ".\n")

        print("Quel domaine souhaitez-vous rechercher ?")

        domains = []
        for file in files:
            domains.append(get_domains("C:\\Users\\ROMAIN\\OneDrive\\Projets\\Dico-abreviations-et-acronymes\\Dico\\" + file[0].upper() + "\\" + file))

        searched = input()
        searched = searched.capitalize()

        matching_files = []

        for domain in domains:
            for i in range(len(domain[0][0])):
                if domain[0][0][i] == searched or domain[0][0][i] == searched + "\n":
                    matching_files.append(domain[1])

        print("Les fichiers suivant matchent avec le domaine que vous avez entre :\n")

        for file in matching_files:
            file = file[71:]
            print(file, end=" ; ")

    print("")
    sleep(5)
    clear()
    print("Voulez-vous effectuer une autre action ? (entrez 'o' pour oui et 'n' pour non)")
    restart = input()