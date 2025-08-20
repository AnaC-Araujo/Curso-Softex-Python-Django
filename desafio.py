'''
Comércio Padaria
1- OK O programa tem que rodar em loop infinito até ser parado;
2- OK Cliente pedir um tipo de pão (francês. doce, forma e australiano);
3- OK Cada pão terá uma quantidade;
4- OK Valor do pão; 
5- OK Forma de pagamento (dinheiro, cartão);
6- OK Forma de entrega (retirada ou delivery);
7- OK Dados do cliente (se for entregar);
8- OK Valor do frete por bairro;
9- OK Nome do atendente e
10- OK Código da entrega.
'''


# Tipos de pães
pao_frances = "Frances"
pao_doce = "Doce"
pao_forma = "Forma"

#Valor do pães
valor_frances = 0.50
valor_doce = 5.00
valor_forma = 5.99

#Quantidade dos pães
quantidade_frances = 15
quantidade_doce = 20
quantidade_forma = 18

#Funcionário
nome_atendente = Josefina

#Entregas por bairro
bairro_barroco = "barroco"
bairro_sao_jose = "sao jose"

#Valores da entrega
frete_barroco = 5.00
frete_sao_jose = 15.00

#Código de venda
codigo_venda = 98568

while True:
    print(f"** Bem vindo a padaria, Pãozinho de Deus! Sou a atendente {nome_atendente} **")
    escolha = input(f"Temos os pães: {pao_frances}, {pao_forma} e {pao_doce}. Qual o pão você deseja? ")
    if escolha == pao_frances:
        quantidade = int(input("Qual a quantidade? "))
        if quantidade <= quantidade_frances:
            quantidade_frances -= quantidade
            pedido_de_paes = quantidade
            valor_compra = quantidade * valor_frances
            print(f"Seu pedido ficou em R$ {valor_compra}.")
        else:
            print(f"Infelizmente, só temos disponível {quantidade_frances} pães no momento.")
            break
    
    forma_retirada = input("É para 1: retirar ou 2: entregar? ")
    if forma_retirada == "2":
        bairro_entrega = input(f"Qual o bairro? (1: {bairro_barroco}, 2:{bairro_sao_jose})")
        if bairro_entrega == "1":
            valor_entrega = frete_barroco
            print(f"Valor da entrega: R$ {valor_entrega}.")
        elif bairro_entrega == "2":
            valor_entrega == frete_sao_jose
            print(f"Valor da entrega: R${valor_entrega}.")
        else:
            print("Fora da área de entregas!")
            break
    elif forma_retirada == "1":
        valor_entrega = 0.00
    else:
        break

    dados_cliente = input("Informe seu nome: ")
    forma_pagamento = input("Escolha a forma de pagamento (1: dinheiro, 2: cartão): ")
    if forma_pagamento == "1":
        forma_pagamento = "Dinheiro"
    else:
        forma_pagamento = "Cartão"
    
    codigo_atual = codigo_venda + 1

    print(f"O valor total da sua compra foi de R$ {valor_compra + valor_entrega}")
    break