# Jogo da Velha em Python

# Cria o tabuleiro 3x3 como uma matriz (lista de listas)
tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

# Função para mostrar o tabuleiro
def mostrar_tabuleiro():
    print("\n  0   1   2")
    for i in range(3):
        print(i, end=" ")
        for j in range(3):
            print(tabuleiro[i][j], end="")
            if j < 2:
                print(" | ", end="")
        print()
        if i < 2:
            print(" ---+---+---")

# Função para verificar se alguém venceu
def verificar_vitoria(simbolo):
    # Verifica linhas e colunas
    for i in range(3):
        if all(tabuleiro[i][j] == simbolo for j in range(3)) or \
           all(tabuleiro[j][i] == simbolo for j in range(3)):
            return True
    # Verifica diagonais
    if all(tabuleiro[i][i] == simbolo for i in range(3)) or \
       all(tabuleiro[i][2 - i] == simbolo for i in range(3)):
        return True
    return False

# Função para verificar empate
def verificar_empate():
    return all(tabuleiro[i][j] != " " for i in range(3) for j in range(3))

# Função principal do jogo
def jogar():
    jogador_atual = "X"
    while True:
        mostrar_tabuleiro()
        print(f"\nVez do jogador {jogador_atual}")

        # Recebe a linha e a coluna da jogada
        try:
            linha = int(input("Escolha a linha (0, 1, 2): "))
            coluna = int(input("Escolha a coluna (0, 1, 2): "))
        except ValueError:
            print("Digite apenas números!")
            continue

        # Valida posição
        if linha not in [0, 1, 2] or coluna not in [0, 1, 2]:
            print("Posição inválida. Tente novamente.")
            continue
        if tabuleiro[linha][coluna] != " ":
            print("Essa posição já está ocupada. Tente outra.")
            continue

        # Faz a jogada
        tabuleiro[linha][coluna] = jogador_atual

        # Verifica vitória
        if verificar_vitoria(jogador_atual):
            mostrar_tabuleiro()
            print(f"\n🎉 Jogador {jogador_atual} venceu! 🎉")
            break

        # Verifica empate
        if verificar_empate():
            mostrar_tabuleiro()
            print("\nEmpate! 😐")
            break

        # Alterna jogador
        jogador_atual = "O" if jogador_atual == "X" else "X"

# Inicia o jogo
jogar()
