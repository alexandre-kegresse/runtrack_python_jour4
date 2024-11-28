# JOB 9 #
def moyenne():
    note1 = int(input("Saisir une première note : "))
    note2 = int(input("Saisir une seconde note : "))
    note3 = int(input("Saisir une troisième note : "))

    moyenne_etudiant = (note1 + note2 + note3) / 3
    print(f"La moyenne est de {int(moyenne_etudiant)}")

    if 20 >= moyenne_etudiant >= 15:
        return(f"Très bon élève")

    elif 14 >= moyenne_etudiant <= 11:
        return(f"Bon élève")

    elif 10 >= moyenne_etudiant <= 8:
        return(f"Élève moyen")
    
    else:
        return(f"Élève devant faire des efforts")

print(moyenne())