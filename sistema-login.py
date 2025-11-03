import time

# Senha fixa
senha_correta = "Xiao"

# Número máximo de tentativas
tentativas = 3

# Tempo máximo (em segundos)
tempo_limite = 30

# Marca o tempo de início
inicio = time.time()

# Loop enquanto ainda houver tentativas e o tempo não tiver acabado
while tentativas > 0 and (time.time() - inicio) < tempo_limite:
    senha = input("Digite a senha: ")

    # Verifica se a senha está correta
    if senha == senha_correta:
        print("✅ Acesso concedido! Bem-vindo, Xiao 💫")
        break
    else:
        tentativas -= 1
        print(f"❌ Senha incorreta. Tentativas restantes: {tentativas}")

# Após o loop, verifica motivo do encerramento
tempo_decorrido = time.time() - inicio

if senha != senha_correta:
    if tempo_decorrido >= tempo_limite:
        print("\n⏰ Tempo esgotado! Acesso negado.")
    else:
        print("\n🚫 Número máximo de tentativas atingido. Acesso negado.")
