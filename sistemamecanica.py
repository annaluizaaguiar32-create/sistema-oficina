carros = [
    ['fiat uno', 'troca de oleo', 150 , 'concluido' ],
    ['Honda civic', 'troca de pneus', 800, 'em andamento'],
    ['toyota corolla','revisao', 500 , 'aguardando']
]
while True:
    print("-"*20)
    print("OFICINA MECANICA")
    print("-"*20)
    print("1-Listar carros")
    print("2-Procurar carro")
    print("3-Mostrar valor total")
    print("4-Mostrar serviços concluidos")
    print("5-Sair")

    opção= input("Escolha uma opção:")
    print()

    if opção == "1":
        for c in carros:
            print(c[0])

    elif opção == "2":
        carro = input("Digite o modelo do carro que deseja procurar:")
        encontrado = False
        for c in carros:
            if carro.lower() == (c[0]).lower():
                print("carro encontrado")
                encontrado = True
        if encontrado == False:
                print("carro nao encontrado")
    elif opção == "3":
        total = 0

        for c in carros:
            total = total +c[2]

        print(f"Valor total das serviços: {total}")

    elif opção == "4":
        concluido = 0
        for c in carros:
            if c[3] == "concluido":
                concluido = concluido +1
        print(f"Serviços concluidos: {concluido}")

    else:
        print("saindo...")
        break