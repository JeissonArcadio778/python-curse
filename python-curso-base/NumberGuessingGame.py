
from random import randrange

def numberGame():
    print("The function is avalaible")
    IAnum = randrange(0,100)
    IABonus = randrange(0,100)
    
    print(IABonus)

    Menu = """

    Trata de adivinar un numero de 0 a 100
    
    """

    cont = 0
    userVidas = 7
    
    while(UserNum!= IAnum):

        UserNum = int(input("Ingrese un numero: "))
        
        if IAnum < UserNum: 
            cont += 1
            print("Tu numero es mayor al de la maquina")
        elif IAnum == UserNum: 
            print("Lo conseguiste! Máquina")
            break
        elif IABonus == UserNum: 
            print("Conseguiste una vida extra, continua")
            userVidas + 1
        else:
            print("tu numero es menor al de la maquina")
        
        if cont == userVidas:
            print("Ya no te quedan más vidas")
            break

        
            

if __name__== '__main__':
    numberGame()

