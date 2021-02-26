from random import choice

comp_vitorias = 0
jogador_vitorias = 0

def Opcao_Jogador():
    esc_jogador = input("Escolha Pedra, Papel ou Tesoura: ")
    if esc_jogador in ["Pedra", "PEDRA", "pedra"]:
        esc_jogador = "pedra"
    elif esc_jogador in ["Papel", "PAPEL", "papel"]:
        esc_jogador = "papel"
    elif esc_jogador in ["Tesoura", "TESOURA", "tesoura"]:
        esc_jogador = "tesoura"
    else: 
        print ("Opcao invalida. Tente novamente")
        Opcao_Jogador()
    return esc_jogador


def Opcao_Computador():
    esc_computador = choice (["pedra", "papel", "tesoura"])
    return esc_computador


while True:

    print("-----------")

    esc_computador = Opcao_Computador()
    esc_jogador = Opcao_Jogador()
    
    print("-----------")

    if(esc_jogador == "papel") and (esc_computador == "pedra")
        or (esc_jogador == "pedra") and (esc_computador == "tesoura")
        or (esc_jogador == "tesoura") and (esc_computador == "papel"):  
        #Jogador ganha
        print(f"Jogador escolheu {esc_jogador} e a maquina escolheu {esc_computador} resultado: Voce ganhou!")
        jogador_vitorias += 1  

    elif esc_jogador == esc_computador 
    #Jogador empata com o computador    
    print(f"Jogador escolheu {esc_jogador} e a maquina escolheu {esc_computador} resultado: Voce empatou!")

    else: 
    print(f"Jogador escolheu {esc_jogador} e a maquina escolheu {esc_computador} resultado: A maquina venceu!")    
    comp_vitorias += 1 

    print("-------------")

    print(f"Vitorias do Jogador: {jogador_vitorias}")
    print(f"Vitorias do Computador: {comp_vitorias}")

    print("-------------")

    esc_jogador = input("Voce quer jogar novamente (s/n)")
    if esc_jogador in ["SIM", "sim", "Sim", "s", "S"]: 
        pass
    elif esc_jogador in ["Nao", "NAO", "nao", "n", "N"]:
        break
    else:
        break


