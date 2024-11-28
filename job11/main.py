# JOB 11 #

def time_to_text():
    user = int(input("Saisir un nombre entier : "))
    X = user // 60
    Y = user % 60

    print(f"{X} heures et {Y} minutes" )

time_to_text()
    
