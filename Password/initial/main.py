from hashlib import sha256
import json
majuscules = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
minuscules = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
caracteres = "? ! @ # $ % ^ & *"
chiffres = "0 1 2 3 4 5 6 7 8 9"
majuscules = majuscules.split(" ")
minuscules = minuscules.split(" ")
caracteres = caracteres.split(" ")
chiffres = chiffres.split(" ")

def demande():
    print("Pour créer un mot de passe efficace, il doit:\n- contenir au moins 8 caractères; \n- contenir au moins une lettre majuscule; \n- contenir au moins une lettre minuscule; \n- contenir au moins un chiffre; \n- contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).\nChoisissez un mot de passe:")
    return verification()

def verification():
    longueur = False
    maj = False
    min = False
    car = False
    chiffre = False
    x = input()
    y = ""
    for i in x:
        if len(x) >= 8:
            longueur = True
        if i in majuscules:
            maj = True
        if i in minuscules:
            min = True
        if i in caracteres:
            car = True
        if i in chiffres:
            chiffre = True
    valide = longueur and maj and min and car and chiffre
    if valide:
        print("mot de passe valide")
        return x
    else:
        print("mot de passe invalide")
        return verification()

resultats = []

while True:
    mot_de_passe = demande()
    resultat = sha256(mot_de_passe.encode("utf-8")).hexdigest()
    resultats.append(resultat)
    choix = input("Voulez-vous ajouter un autre mot de passe? (O/N) ")
    if choix.lower() == "n":
        break

with open("resultats.json", "w") as f:
    json.dump(resultats, f)

def ouvrir():
    choix = input("voulez-vous ouvrir votre dossier ? (O/N) ")
    if choix.lower() == "o":
        with open("resultats.json") as x:
            resultats = json.load(x)
            print(resultats)

def doublons():
    with open("resultats.json") as f:
        resultats = json.load(f)
    double = set(resultats)
    if len(double) != len(resultats):
        print("Des doublons sont présents")
        resultats = double
        print(resultats)
        return resultats
    else:
        print("Aucun doublon présent")
        return resultats


ouvrir()
doublons()