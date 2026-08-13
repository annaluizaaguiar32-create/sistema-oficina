print("INVENTARIO")
print("opção 1: olhar")
print("opção 2: usar")
print("opção 3: sair")
opção = input("escolha uma opção:")

while True:
    if opção == "1":
        print("ESPADA")
        print("ESCUDO")
        print("ARCO E FLECHA")
        print("POÇÃO")
        break
    elif opção == "2":
        item = input("qual item voce deseja?:").lower()

        if "espada" in item:
            print("ESPADA EQUIPADA")
        elif "escudo" in item:
            print("ESCUDO EQUIPADO")
        elif "arco e flecha" in item:
            print("ARCO E FLECHA EQUIPADO")
        elif "poção" in item:
            print("POÇÃO EQUIPADA")
        else:
            print("opção nao identificada")
        break
    elif opção == "3":
        print("saindo...")
        break