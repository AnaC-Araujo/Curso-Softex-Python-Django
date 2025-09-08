contatos = {}

while True:
    print("***Menu*** \n01: Adicionar Contato \n02: Buscar Contato \n03: Sair")
    escolha_usuario = input("Opção Escolhida: ")
    if escolha_usuario == "01":
        nome = input("Informe o nome do contato: ")
        numero = input("Agora informe o numero: ")
        if numero.isdigit and len(numero) == 11:
            contatos[nome] = numero
        else:
            print("Digite somente 11 números.")
    elif escolha_usuario == "02":
        nome = input("Digite o nome do contato: ").lower
        contatos.get(nome, "Não há esse contato")
    elif escolha_usuario == "03":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida.")