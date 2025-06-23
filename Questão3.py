# Mensagem de boas-vindas
print("Seja bem-vindo a copiadora do Gean Rodrigues")

# Escolhendo o serviço desejado
def escolha_servico():
    while True:
        print("serviços disponíveis")
        print("DIG - Digitalização (R$1.10 por página)")
        print("ICO - Impressão Colorida (R$1.00 por página)")
        print("IPB - Impressão Preto e Branco (R$0.40 por página)")
        print("FOT - Fotocópia (R$0.20 por página)")
        servico = input("Escolha o serviço desejado (DIG/ICO/IPB/FOT): ").lower()
        if servico == "dig":
            return 1.10
        elif servico == "ico":
            return 1.00
        elif servico == "ipb":
            return 0.40
        elif servico == "fot":
            return 0.20
        else:
            print("Escolha inválida, entre com o tipo do serviço novamente")

# Perguntar o número de páginas
def num_pagina():
    while True:
        try:
            paginas = int(input("Digite o número de páginas: "))
            # Aplicação de desconto
            if paginas < 20:
                return paginas
            elif paginas < 200:
                return paginas * 0.85  # 15% de desconto
            elif paginas < 2000:
                return paginas * 0.80  # 20% de desconto
            elif paginas < 20000:
                return paginas * 0.75  # 25% de desconto
            else:
                print("Não aceitamos tantas páginas de uma vez.")
                print("Por favor, entre com o número de páginas novamente.")
                continue
        except ValueError:
            print("Digite um número inteiro válido.")

# Função para escolher o serviço adicional (encadernação)
def servico_extra():
    while True:
        print("Serviço adicional:")
        print("0 - Não quero encadernação (R$0.00)")
        print("1 - Encadernação simples (R$15.00)")
        print("2 - Encadernação capa dura (R$40.00)")
        extra = input("Escolha o adicional (0/1/2): ")
        if extra == "0":
            return 0
        elif extra == "1":
            return 15
        elif extra == "2":
            return 40
        else:
            print("Opção inválida! Escolha apenas 0, 1 ou 2.")

# Parte principal do programa
try:
    valor_servico = escolha_servico()
    paginas_com_desconto = num_pagina()
    valor_extra = servico_extra()
    total = (valor_servico * paginas_com_desconto) + valor_extra

    # Exibição final
    print("Resumo do pedido")
    print(f"Valor por página do serviço: R$ {valor_servico}")
    print(f"Número de páginas (com desconto aplicado): R$ {paginas_com_desconto}")
    print(f"Valor do serviço adicional: R$ {valor_extra}")
    print(f"Total: R$ {total} (serviço: {valor_servico} • páginas: {paginas_com_desconto} • extra: {valor_extra})")
except:
    print("Ocorreu um erro inesperado. Tente novamente.")
