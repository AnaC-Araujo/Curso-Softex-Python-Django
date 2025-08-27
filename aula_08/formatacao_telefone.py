contato = input("Digite seu número para contato: ")

if len(contato) != 11 and not contato.isdigit():
    print("O número precisa ter 11 dígitos númericos.")

valido = True
for numero in contato:
    repetido = 0
    for numero_2 in contato:
        if numero == numero_2:
            repetido += 1
        if repetido >= 3:
            valido = False
          #  print("Número inválido!")
            break
if not valido:
    print("Número inválido!")
else:
    ddd = contato[:2]
    inicial = contato[2:7]
    final = contato[7:]
    print(f"({ddd}) {inicial}-{final}")