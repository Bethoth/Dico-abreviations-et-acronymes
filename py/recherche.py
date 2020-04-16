from os.path import exists, isdir, join, split
from os import listdir, system
from time import sleep

dicoPath = join(split(__file__)[0], "..", "Dico")

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
        path = dicoPath + "/" + searched[0].upper() + "/" + searched.lower() + ".md"

        # Verifie que le chemin cree existe dans le dictionnaire
        if exists(path):
            print("Le fichier existe !")
        else:
            print("Le fichier n'existe pas.")

        sleep(1)

    if choix == "2":
        clear()

        dirs = listdir(dicoPath)

        files_list = []
        for dir_ in dirs:
            files_list.append(listdir(dicoPath + "/" + dir_))

        files = []
        for list_ in files_list:
            for i in range(len(list_)):
                files.append(list_[i])

        print("Vous avez choisi de " + options[1].lower() + ".\n")

        print("Quel domaine souhaitez-vous rechercher ?")

        domains = []
        for file in files:
            domains.append(get_domains(dicoPath + "/" + file[0].upper() + "/" + file))

        searched = input()
        searched = searched.capitalize()

        matching_files = []

        for domain in domains:
            for i in range(len(domain[0][0])):
                if domain[0][0][i] == searched or domain[0][0][i] == searched + "\n":
                    matching_files.append(domain[1])

        if len(matching_files) != 0:
            print("Les fichiers suivant matchent avec le domaine que vous avez entre :\n")

            for file in matching_files:
                file = file[75:]
                print(file, end=" ; ")

        else:
            print("Aucun fichier ne matche avec le domaine que vous avez entre.")
        
        print("\n\nAppuyez sur Entree une fois avoir lu ce que vous vouliez lire.")
        input()
    
    clear()
    print("Voulez-vous effectuer une autre action ? (entrez 'o' pour oui et 'n' pour non)")
    restart = input()