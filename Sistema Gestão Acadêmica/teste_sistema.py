# teste_sistema.py
from sistema_academico import SistemaAcademico

sistema = SistemaAcademico()

# Teste rápido
print(sistema.cadastrar_aluno("João Silva", "20240001"))
print(sistema.cadastrar_disciplina("Programação", "COMP101"))
print(sistema.matricular_aluno("20240001", "COMP101"))
print(sistema.lancar_nota("20240001", "COMP101", 9.5))
print("\n--- Boletim ---")
sistema.boletim("20240001")

print("\n--- Todos os alunos ---")
for aluno in sistema.alunos:
    print(f"{aluno.nome} - {aluno.matricula}")

print("\n--- Todas as disciplinas ---")
for disciplina in sistema.disciplinas:
    print(f"{disciplina.nome} - {disciplina.codigo}")