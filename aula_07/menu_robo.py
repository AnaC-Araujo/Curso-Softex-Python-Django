posicao = 0

while True:
    escolha_posicao = input("Escolha uma das opções a seguir: 1-Avançar 2-Recuar 3-Status 4-Desligar ")
    if escolha_posicao == "1":
        posicao += 1
    elif escolha_posicao == "2":
        posicao -= 1
    elif escolha_posicao == "3":
        print(f"Sua posição atual é: {posicao}")
    elif escolha_posicao == "4":
        print("Desligando")
        break
    else:
        print("Erro! Escolha uma opção válida.")