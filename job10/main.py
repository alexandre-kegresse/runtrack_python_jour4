# JOB 10 #

def is_pair_or():
    n = int(input("Saisir un nombre : "))

    if n % 2 == 0 and n > 0:
        return(f"{n} est pair et positif")
    
    elif n % 2 == 0 and n < 0:
        return(f"{n} est pair et negatif")

    elif n % 2 > 0 and n > 0:
        return(f"{n} est impair et positif")

    elif n % 2 > 0 and n < 0: 
        return(f"{n} est impair et negatif")
    
print(is_pair_or())