import mysql.connector
#conexão com banco
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password= "",
    database= "gerenciadortarefas"
)
cursor = conexao.cursor()

while True:
    print("\n======GERENCIADOR DE TAREFAS=====")
    print("1- Cadastar uma tarefa")
    print("2- Listar tarefas")
    print("3- Buscar tarefa pelo nome")
    print("4- Excluir tarefas")
    print("5- Sair")

    opção = input("ESCOLHA UMA OPÇÃO:")

    #CADASTRAR
    if opção == "1":
        titulo= input("Digite o titulo da tarefa:")
        status= input("Digite o status da tarefa (Concluido/pendente):")

        sql = "INSERT INTO tarefas (titulo, status) VALUES(%s,%s)"
        valores = (titulo,status)

        cursor.execute(sql,valores)
        conexao.commit()

        print("TAREFA CADASTRADA COM SUCESSO")

    #listar
    elif opção == "2":
        cursor.execute ("SELECT *FROM tarefas")
        tarefas = cursor.fetchall()
        print("\n-----lista de tarefas-----")
        if len (tarefas)== 0 :
            print("nenhuma atividade cadastrada")
        else:
            for tarefa in tarefas:
                print(f"ID: {tarefa [0]}")
                print(f"titulo: {tarefa [1]}")
                print(f"status: {tarefa [2]}")
                print ("-"*25)
#buscar
    elif opção == "3":
        nome = input("Busque uma tarefa:")
        sql = "SELECT*FROM tarefas WHERE titulo LIKE %s"
        valor = ("%"+ nome +"%",)

        cursor.execute(sql,valor)
        resultado = cursor.fetchall()

        if len (resultado)== 0:
            print("Nenhuma tarefa encontrada")
        else:
            print("\n----RESULTADO BUSCA----")
            for tarefa in resultado:
                print(f"ID:{tarefa[0]}")
                print(f"titulo:{tarefa[1]}")
                print(f"status:{tarefa[2]}")
                print("-"*25)
#exluir 
    elif opção == "4":
        id_tarefa = input("Digite o ID da tarefa que deseja excluir:")
        sql = "DELETE FROM tarefas WHERE ID = %s"
        valor = (id_tarefa,)
        cursor.execute(sql,valor)
        conexao.commit()
        if cursor.rowcount >0:
            print("TAREFA EXCLUIDA COM SUCESSO!")
        else:
            print("ID NAO ENCONTRADO")
#sair
    elif opção == "5":
        print ("saindo...")
        break
    else:
        print("opção nao encontrada")
        cursor.close()
        conexao.close()

                