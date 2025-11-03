# Jogo da Forca
palavra = "python"
letras_descobertas = ["_"] * len(palavra)
tentativas = 6
letras_usadas = []

print("🎯 Jogo da Forca! Adivinhe a palavra letra por letra.")

while tentativas > 0:
    print("\nPalavra:", " ".join(letras_descobertas))
    letra = input("Digite uma letra (ou 'sair' para desistir): ").lower()

    if letra == "sair":
        print("Você desistiu do jogo.")
        break  # Interrompe o loop

    if not letra.isalpha() or len(letra) != 1:
        print("Entrada inválida. Digite apenas uma letra.")
        continue  # Pula para a próxima iteração

    if letra in letras_usadas:
        print("Você já tentou essa letra.")
        pass  # Não faz nada, apenas segue o fluxo
