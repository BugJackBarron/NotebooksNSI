heure=int(input("Entrez l'heure : "))
minutes=int(input("Entrez les minutes : "))
secondes=int(input("Entrez les secondes : "))
if 0<=heure<24 and 0<=minutes<60 and 0<=secondes<60 :
    print(f"{heure}:{minutes}:{secondes}")
else :
    print("L'heure saisie est invalide")