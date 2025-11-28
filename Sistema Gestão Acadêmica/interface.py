# interface.py
from sistema_academico import SistemaAcademico

sistema = SistemaAcademico()

while True:
    print("\n1-Cadastrar Aluno\n2-Cadastrar Disciplina\n3-Matricular\n4-Lançar Nota\n5-Boletim\n0-Sair")
    op = input("Opção: ")
    
    if op == '1':
        nome = input("Nome: ")
        matricula = input("Matrícula: ")
        print(sistema.cadastrar_aluno(nome, matricula))
    elif op == '2':
        nome = input("Nome: ")
        codigo = input("Código: ")
        print(sistema.cadastrar_disciplina(nome, codigo))
    elif op == '3':
        matricula = input("Matrícula: ")
        codigo = input("Código: ")
        print(sistema.matricular_aluno(matricula, codigo))
    elif op == '4':
        matricula = input("Matrícula: ")
        codigo = input("Código: ")
        nota = float(input("Nota: "))
        print(sistema.lancar_nota(matricula, codigo, nota))
    elif op == '5':
        matricula = input("Matrícula: ")
        sistema.boletim(matricula)
    elif op == '0':
        break