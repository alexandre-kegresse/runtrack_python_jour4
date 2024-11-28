# JOB 7 #
def which_langage(langage):

    if langage == "js":
        return(f"Tu es un développeur web !")

    elif langage ==  "python":
        return(f"Tu es un développeur IA")

    elif langage == "java":
        return(f"Tu es un développeur logiciel")

    elif langage == "react":
        return(f"Tu es un développeur mobile")

    else:
        return(f"Un jour je serais développeur")

print(which_langage(input("Quel language ? : ")))

    


