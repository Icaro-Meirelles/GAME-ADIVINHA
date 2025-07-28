
# JOGO DE ADINHA EM PYTHON

from ASCII_Art import ascii_art
import random




def gerador():

    ascii_art()



    
    num_aleatorio = random.randint(1, 10)
    print(f"     Número Gerado!")




    while True:
        escolha = int(input("    Digite um valor: "))
        
        if escolha == num_aleatorio:
            print ("VOCÊ ACERTOU!!! PARABÉNS!")
            break
            
        elif escolha < num_aleatorio:
            print("   Pense mais alto!")
            
        elif escolha > num_aleatorio:
            print("   Pense mais baixo!")



if __name__ == "__main__":
    gerador()