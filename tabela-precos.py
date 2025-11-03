# Preços de produtos em diferentes lojas
lojas = ["Loja Sol", "Loja Lua", "Loja Estrela"]
precos = [
    [10.99, 12.50, 9.75],
    [8.99, 11.20, 10.00],
    [9.50, 10.75, 12.30]
]

for i in range(len(lojas)):
    print(f"{lojas[i]}:")
    for preco in precos[i]:
        print(f"  R$ {preco:.2f}")
    print()
