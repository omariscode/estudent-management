import sqlite3

conn = sqlite3.connect("Database/estudantes.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS estudantes(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT,
               classe INTEGER,
               turma TEXT,
               number INTEGER
               
)

''')
conn.commit()

#----------------------------------------------------------Funções--------------------------------------------------------------------#
def adicionarAluno():
    nome = input("Digite o seu nome: ")
    classe = int(input("Digite a sua classe(10ª-13ª): "))
    turma = input("Digite a sua turma: ")
    number =  int(input("Digite o seu número: "))
    cursor.execute("INSERT INTO estudantes (nome, classe, turma, number) VALUES (?,?,?,?)", (nome, classe, turma, number,))
    conn.commit()
    print("Aluno registrado com sucesso!")

def removerAluno():
    alunoId = int(input("Digite o ID do aluno que deseja remover: "))
    cursor.execute("DELETE FROM estudantes WHERE id = ?", (alunoId,))
    conn.commit()
    print("Aluno removido com sucesso!")

def atualizarAluno():
    alunoId = int(input("Digite o ID do estudante q quer mudar: "))
    nome = input("Digite o nome do aluno a atualizar: ")
    classe =  int(input("Digite a nova classe do aluno: "))
    turma = input("Digite a nova turma do aluno: ")
    number = int(input("Digite o novo número do aluno: "))

    if nome:
        cursor.execute("UPDATE estudantes SET nome = ? WHERE id = ?", (nome, alunoId,))
    if classe:
        cursor.execute("UPDATE estudantes SET classe = ? WHERE id = ?", (classe, alunoId,))
    if turma:
        cursor.execute("UPDATE estudantes SET turma = ? WHERE id =?", (turma, alunoId,))
    if number:
        cursor.execute("UPDATE estudantes SET number = ? WHERE id = ?", (number, alunoId,))
    conn.commit()
    print("Informações do aluno atualizadas com sucesso!")

def listarAlunos():
    classe = int(input("Digite a classe q na qual quer selecionar: "))
    cursor.execute("SELECT * FROM estudantes WHERE classe = ?", (classe,))
    for i in cursor:
        print(i) 
    conn.commit()
    

def menu():
    while True:
        print("\nMenu")
        print("1. Adicionar estudante")
        print("2. Remover estudante")
        print("3. Atualizar informação do estudante")
        print("4. Listar estudantes por classe")
        print("5. Sair")

        escolha = input("Escolha a opção: ")

        if escolha == '1':
            adicionarAluno()
        elif escolha == '2':
            removerAluno()
        elif escolha == '3':
            atualizarAluno()
        elif escolha == '4':
            listarAlunos()
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inaceitavel!")

menu()

conn.close()
