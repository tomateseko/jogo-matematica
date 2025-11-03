# 🎯 Jogo da Forca com boneco visual

# Lista de desenhos do boneco (da forca vazia até o boneco completo)
forca_desenhos = [
    """
     _______
    |/      |
    |
    |
    |
    |
    |_____
    """,
    """
     _______
    |/      |
    |      ( )
    |
    |
    |
    |_____
    """,
    """
     _______
    |/      |
    |      ( )
    |       |
    |       |
    |
    |_____
    """,
    """
     _______
    |/      |
    |      ( )
    |      \\|
    |       |
    |
    |_____
    """,
    """
     _______
    |/      |
    |      ( )
    |      \\|/
    |       |
    |
    |_____
    """,
    """
     _______
    |/      |
    |      ( )
    |      \\|/
    |       |
    |      /
    |_____
    """,
    """
     _______
    |/      |
    |      ( )
    |      \\|/
    |       |
    |      / \\
    |_____
    """
]

# Palavra secreta
palavra_secreta = "python"

# Lista para armazenar as letras acertadas
letras_certas = ["_"] * len(palavra_secreta)

# Número máximo de erros (6, pois o boneco tem 7 estágios contando o inicial)
erros = 0
max_erros = 6

print("🎮 Bem-vindo ao Jogo da Forca!\n")

# Loop principal do jogo
while erros < max_erros and "_" in letras_certas:
    print(forca_desenhos[erros])
    print("\nPalavra:", " ".join(letras_certas))
    tentativa = input("\nDigite uma letra: ").lower()

    # Validação da entrada
    if len(tentativa) != 1 or not tentativa.isalpha():
        print("Digite apenas uma letra!")
        continue

    # Verifica se a letra está na palavra
    if tentativa in palavra_secreta:
        for i, letra in enumerate(palavra_secreta):
            if letra == tentativa:
                letras_certas[i] = tentativa
        print("✅ Acertou uma letra!")
    else:
        erros += 1
        print("❌ Letra incorreta!")

# Exibe o resultado final
if "_" not in letras_certas:
    print(forca_desenhos[erros])
    print("\n🎉 Parabéns! Você venceu! A palavra era:", palavra_secreta)
else:
    print(forca_desenhos[-1])
    print("\n💀 Você perdeu! A palavra era:", palavra_secreta)
