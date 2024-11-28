# JOB 5 #

# def calcule():
#     num1 = input("Premier numéro : ")
#     operator = input("Type d'operateur : ")
#     num2 = input("Second numéro : ")

#     add = int(num1) + int(num2)
#     print(add)
# (calcule())

# def calcule(num1, operator, num2):
#     int(num1)
#     int(num2)
#     operator = "+"

#     elif operator == "+":
#         print(num1 + num2)

# calcule(5 + 5)

def calcule(num1, operator, num2):
    num1 = int(num1)
    num2 = int(num2)

    if operator == "+":
        return(num1 + num2)
    
    elif operator == "-":
        return(num1 - num2)
    
    elif operator == "*":
        return(num1 * num2)
    
    elif operator == "/":
        return(num1 / num2)
    
    elif operator == "%":
        return(num1 % num2)

print(calcule(5, "+",45))
print(calcule(50, "-",45))
print(calcule(50, "*",45))
print(calcule(50, "/",45))
print(calcule(50, "%",45))


    
