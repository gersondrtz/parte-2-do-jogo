import random

tabuleiro = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
historicoTab = []
ganhadores = []
jogador1 = "X"
jogador2 = "O"

def escolherOpcaoEOrientar():
    print()
    print('PARA JOGAR CONTRA A MÁQUINA DIGITE 1')
    print('PARA JOGAR COM DOIS JOGADORES DIGITE 2')
    print('PARA VER O HISTÓRICO DIGITE 3')
    print("PARA ENCERRAR DIGITE 4")
    print()
    opcao = int(input("Digite sua opção: "))

    while opcao != 4:
        if opcao == 1:
            limparTabuleiro()
            jogarContraMaquina()
        elif opcao == 2:
            limparTabuleiro()
            jogarDoisJogadores()
        elif opcao == 3:
            mostrarHistorico()
        elif opcao == 4:
            print("Fim do jogo!")
        else:
            print("Opção inválida. Tente novamente.")

        print()
        print('PARA JOGAR CONTRA A MÁQUINA DIGITE 1')
        print('PARA JOGAR COM DOIS JOGADORES DIGITE 2')
        print('PARA VER O HISTÓRICO DIGITE 3')
        print("PARA ENCERRAR DIGITE 4")
        opcao = int(input("Digite sua opção: "))

def jogarContraMaquina():
    while True:
        mostrarTabuleiro()
        inserirLinhaColuna(jogador1)  # Jogador humano joga
        if checarSeGanhou(jogador1):
            break
        
        mostrarTabuleiro()
        inserirJogadaMaquina()  # Máquina joga
        if checarSeGanhou(jogador2):
            break

def jogarDoisJogadores():
    while True:
        mostrarTabuleiro()
        inserirLinhaColuna(jogador1)  # Jogador 1 joga
        if checarSeGanhou(jogador1):
            break
        
        mostrarTabuleiro()
        inserirLinhaColuna(jogador2)  # Jogador 2 joga
        if checarSeGanhou(jogador2):
            break

def mostrarTabuleiro():
    print('-------------------------JOGO DA VELHA-------------------------')
    for i in range(3):
        print('                         ', tabuleiro[i][0], '|', tabuleiro[i][1], '|', tabuleiro[i][2])
    print()

def inserirLinhaColuna(jogador):
    while True:
        try:
            linha = int(input(f'JOGADOR {jogador} | DIGITE A LINHA (1 a 3): '))
            coluna = int(input(f'JOGADOR {jogador} | DIGITE A COLUNA (1 a 3): '))
            if 1 <= linha <= 3 and 1 <= coluna <= 3 and tabuleiro[linha - 1][coluna - 1] == '_':
                tabuleiro[linha - 1][coluna - 1] = jogador
                break
            else:
                print("Posição inválida ou já ocupada. Tente novamente.")
        except ValueError:
            print("Entrada inválida! Por favor, insira números inteiros.")

def inserirJogadaMaquina():
    print("Vez da máquina...")
    while True:
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)
        if tabuleiro[linha][coluna] == '_':
            tabuleiro[linha][coluna] = jogador2
            break

def limparTabuleiro():
    for i in range(3):
        for j in range(3):
            tabuleiro[i][j] = '_'

def mostrarHistorico():
    numeroDePartidas = len(historicoTab)
    for i, partida in enumerate(historicoTab, 1):
        print(f'-------------------------PARTIDA {i}-------------------------')
        print(ganhadores[i - 1])
        for linha in partida:
            print('                         ', ' | '.join(linha))
        print()

def checarSeGanhou(jogador):
    if ganharEmLinha(jogador) or ganharEmColuna(jogador) or ganharEmDiagonal(jogador):
        mostrarTabuleiro()
        historicoTab.append([row[:] for row in tabuleiro])  # Salva o estado atual do tabuleiro
        ganhadores.append(f"Jogador {jogador} ganhou!")
        print(f"Jogador {jogador} ganhou!")
        return True
    if darVelha():
        mostrarTabuleiro()
        historicoTab.append([row[:] for row in tabuleiro])  # Salva o estado atual do tabuleiro
        ganhadores.append("Velha")
        print("Deu velha!")
        return True
    return False

def ganharEmLinha(jogador):
    for linha in tabuleiro:
        if all(celula == jogador for celula in linha):
            return True
    return False

def ganharEmColuna(jogador):
    for col in range(3):
        if all(tabuleiro[linha][col] == jogador for linha in range(3)):
            return True
    return False

def ganharEmDiagonal(jogador):
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

def darVelha():
    return all(celula != '_' for linha in tabuleiro for celula in linha)

escolherOpcaoEOrientar()
