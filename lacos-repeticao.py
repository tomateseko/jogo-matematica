# Lista com os dias da semana
dias_da_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]

print("Contagem até o fim de semana:\n")

# Loop for para percorrer os dias úteis
for dia in dias_da_semana:
    print(f"Mais um dia vencido: {dia} ✅")

print("\nFinalmente! O fim de semana chegou! 🎉")


# Lista de preços dos itens
precos = [5.50, 3.20, 8.90, 12.00, 2.75]

# Variável para armazenar o total
total = 0

# Loop for para somar os preços
for preco in precos:
    total += preco

print(f"O total da sua compra é: R${total:.2f}")


# Número inicial de mensagens não lidas
mensagens_nao_lidas = 5

# Enquanto ainda houver mensagens, continue lendo
while mensagens_nao_lidas > 0:
    print(f"📨 Você leu uma mensagem. Faltam {mensagens_nao_lidas - 1} mensagens.")
    mensagens_nao_lidas -= 1  # Diminui uma mensagem a cada leitura

print("✅ Todas as mensagens foram lidas!")


# Valor do item
meta = 100

# Valor economizado por semana
por_semana = 10

# Valor atual economizado
total = 0

# Contador de semanas
semanas = 0

# Loop while: continua até atingir a meta
while total < meta:
    semanas += 1
    total += por_semana
    print(f"📅 Semana {semanas}: você tem R${total:.2f} guardados.")

print(f"\n🎉 Você atingiu a meta de R${meta:.2f} em {semanas} semanas!")


# Lista de alunos presentes
alunos = ["Ana", "Bruno", "Carla", "Diego", "Fernanda"]

# Nome do aluno que o professor quer verificar
aluno_procurado = "Diego"

# Loop for para percorrer a lista de alunos
encontrado = False
for aluno in alunos:
    if aluno == aluno_procurado:
        print(f"✅ O aluno {aluno_procurado} está presente.")
        encontrado = True
        break  # Para o loop assim que encontrar o aluno

# Caso o aluno não esteja na lista
if not encontrado:
    print(f"❌ O aluno {aluno_procurado} não está na lista de presença.")

