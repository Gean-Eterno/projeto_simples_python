# Mensagem de boas-vindas
print("Seja bem-vindo à loja de gelados do Gean Rodrigues")

# Variável para acumular o total
total = 0

# Início do laço principal
while True:
    # Solicita o sabor e converte para minúsculo
    sabor = input("Escolha o sabor desejado (cp = Cupuaçu, ac = Açaí): ").lower()

    # Valida o sabor
    if sabor == "cp" or sabor == "ac":
        print("Sabor válido.")
    else:
        print("Sabor inválido. Tente novamente.")
        continue  # volta pro início

    # Solicita o tamanho e converte para minúsculo
    tamanho = input("Escolha o tamanho desejado (p/m/g): ").lower()

    # Valida o tamanho
    if tamanho == "p" or tamanho == "m" or tamanho == "g":
        print("Tamanho válido.")
    else:
        print("Tamanho inválido. Tente novamente.")
        continue  # volta pro início

    # Verifica os preços com estrutura aninhada
    if sabor == "cp":
        if tamanho == "p":
            print("Você pediu um Cupuaçu no tamanho p: R$ 9.00")
            total += 9
        elif tamanho == "m":
            print("Você pediu um Cupuaçu no tamanho m: R$ 14.00")
            total += 14
        elif tamanho == "g":
            print("Você pediu um Cupuaçu no tamanho g: R$ 18.00")
            total += 18

    elif sabor == "ac":
        if tamanho == "p":
            print("Você pediu um Açaí no tamanho p: R$ 11.00")
            total += 11
        elif tamanho == "m":
            print("Você pediu um Açaí no tamanho m: R$ 16.00")
            total += 16
        elif tamanho == "g":
            print("Você pediu um Açaí no tamanho g: R$ 20.00")
            total += 20

    # Pergunta se deseja continuar
    continuar = input("Deseja pedir mais alguma coisa? (s/n): ").lower()
    if continuar == "n":
        break  # sai do laço

# Exibe o total no final
print(f"O total a pagar é R$ {total}")
