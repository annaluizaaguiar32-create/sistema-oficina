saldo = 1000
while True:
    print("opção 1:VER SALDO")
    print("opção 2:SACAR")
    print("opção 3:DEPOSITAR")
    opção = input("escolha sua opção:")
    if opção == "1":
        print(f"{saldo}")
        break
    elif opção == "2":
        print(f"seu saldo atual é de {saldo},quanto voce deseja sacar? ")
        saque= float(input("digite o valor do saque:"))
        saldo= saldo - saque
        print(f"seu saldo agora é: {saldo}")
        break
    elif opção == "3":
        deposito = float(input("quanto voce quer depositar?:"))
        saldo = saldo + deposito
        print(f"seu saldo agora é:{saldo}")
        break
