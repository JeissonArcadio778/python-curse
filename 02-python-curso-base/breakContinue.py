# def run():
#     # for i in range(1000):
#     #     if i % 2 != 0:
#     #         continue
#     #     print(i)

#     for i in range(400):
#         if i == 220:
#             break
#         print(i)
#     frase = input("digite una frase: ")
#     for i in frase: 
#         if i == "o":
#             break
#         print(i)

#     numero = list(input())
#     for i in numero:
#         if i == '1':
#             continue
#         print(i)

# if __name__ == '__main__':
#     run()

#Juego: 

def juego(vidas):
    num_a = 5

    num = int(input("Ingresa un numero:"))

    if num < 0 or num > 10:
        vidas -= 1
        print("Numero invalido, pierdes una vida.")
        return vidas
    elif num_a > num:
        vidas -= 1
        print("El numero ingresado es menor al del sistema, pierdes una vida.")
        return vidas
    elif(num_a == num):
        print("Vaya, es un empate!")
    else:
        print("Genial, le ganaste al sistema!")


def main():
    print("""
    El juego consiste en escribir un numero mayor al que genera el sistema en un rango del 1 al 10,
    tienes hasta 3 oportunidades de fallar al inicio.
    Suerte!""")

    vidas= 3

    while(True):
        if vidas == 0:
            print("Fin del juego.")
            break

        vidas = juego(vidas)
        print("Te quedan: " + str(vidas) + " vidas.")
    






if __name__ == "__main__":
    main()