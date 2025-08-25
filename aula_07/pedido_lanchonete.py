produto = "mini pizza queijuda"
valor = 18.00
cupom = "abracadabra"
cupom_desconto = 5.00

while True:
    escolha_cliente = input("Olá, seja bem vindo (a)! Qual o lanche deseja? ").lower()
    if escolha_cliente == produto:
        cupom_cliente = input("Você possui cupom de desconto? 1- sim ou 2- não:  ")
        if cupom_cliente == "1":
            cupom_inserido = input("Digite o cupom de desconto: ")
            if cupom_inserido == cupom:
                valor_cupom = valor - cupom_desconto
                print(f"O valor a ser pago com desconto é R$ {valor_cupom}.")
                break
            else:
                print("Digite um cupom de desconto válido.")
        elif cupom_cliente == "2":
            print(f"Não há desconto. O valor a ser pago é de R$ {valor}.")
            break