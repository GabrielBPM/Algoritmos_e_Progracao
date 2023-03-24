#Código de Gabriel Barcelos Palhoni Machado
from random import *

pedra = 0
papel = 1
tesoura = 2

escolha = int(input("Escolha 0 para pedra, 1 para papel ou 2 para tesoura: "))

if escolha > 2 or escolha < 0:
    print("Jogada não reconhecida!")
else:
    if escolha == pedra:
        print("A escolha do jogador foi Pedra!")
    else:
        if escolha == papel:
            print("A escolha do jogador foi Papel!")
        else:
            print("A escolha do jogador foi Tesoura!")
    computador = randint(0,2)
    if computador == pedra:
        print("A escolha do computador foi Pedra!")
    else:
        if computador == papel:
            print("A escolha do computador foi Papel!")
        else:
            print("A escolha do computador foi Tesoura!")

    if escolha == computador:
        print("Empate!")
    else:
        if escolha == pedra and computador == tesoura:
                print("Vitória!")
        else:
            if escolha == papel and computador == pedra:
                print("Vitória!")
            else:
                if escolha == tesoura and computador == papel:
                    print("Vitória")
                else:
                    print("Derrota!")