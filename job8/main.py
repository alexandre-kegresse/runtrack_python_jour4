# JOB 8 #

def fonction_fruits():

    type = input("Choisir un fruit ou un légume : ")
    saison = input("Quelle saison ? : ")

    if type ==  "fruits" and saison == "hiver":
        return(f"Orange, mandarine et kiwi")

    elif type == "fruits" and saison == "été":
        return(f"Poire, fraise, cassis")
    
    elif type == "légume" and saison == "hiver":
        return(f"carotte, topinambour, endive")

    elif type == "légume" and saison == "été":
        return(f"artichaut, aubergine,navet")

    else:
        return(f"Cette combinaison n'est pas disponible")

print(fonction_fruits())

# def fonction_fruits(type, saison):

#     type = input("Choisir un fruit ou un légume : ")
#     saison = "hiver", "été"
#     fruits = 

#     if type ==  "fruits" and saison == "hiver":
#         print


    