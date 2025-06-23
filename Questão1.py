# Mensagem de boas vindas
print("Seja bem-vindo à loja do Gean Rodrigues")

# Entrada dos dados (valor e quantidade)
valor_unitario = float(input("Digite o valor do produto:"))
quantidade = int(input("Digite a quantidade do produto:"))

# Cálculo do valor total
valor_total = valor_unitario * quantidade

# Verificação do desconto com base no valor total
if valor_total < 2500:
    desconto_percentual = 0
elif valor_total >= 2500 and valor_total < 6000:
    desconto_percentual = 0.04
elif valor_total >= 6000 and valor_total < 10000:
    desconto_percentual = 0.07
else:
    desconto_percentual = 0.11

# Cálculo do valor com desconto
valor_com_desconto = valor_total - (valor_total * desconto_percentual)

# Exibição dos resultados
print(f"Valor total sem desconto R$: {valor_total}")
print(f"Desconto aplicado: {desconto_percentual * 100}%")
print(f"Valor total com desconto R$: {valor_com_desconto}")
