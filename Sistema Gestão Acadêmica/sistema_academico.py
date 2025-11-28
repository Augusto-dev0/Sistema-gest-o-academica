# sistema_academico.py
import json

class Aluno:
    def _init_(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = {}

class Disciplina:
    def _init_(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.alunos = []

class SistemaAcademico:
    def _init_(self):
        self.alunos = []
        self.disciplinas = []
        self.carregar_dados()
    
    def cadastrar_aluno(self, nome, matricula):
        self.alunos.append(Aluno(nome, matricula))
        self.salvar_dados()
        return f"Aluno {nome} cadastrado!"
    
    def cadastrar_disciplina(self, nome, codigo):
        self.disciplinas.append(Disciplina(nome, codigo))
        self.salvar_dados()
        return f"Disciplina {nome} cadastrada!"
    
    def matricular_aluno(self, matricula, codigo):
        aluno = next((a for a in self.alunos if a.matricula == matricula), None)
        disciplina = next((d for d in self.disciplinas if d.codigo == codigo), None)
        if aluno and disciplina:
            disciplina.alunos.append(aluno)
            self.salvar_dados()
            return f"Aluno matriculado em {disciplina.nome}!"
        return "Aluno ou disciplina não encontrado!"
    
    def lancar_nota(self, matricula, codigo, nota):
        aluno = next((a for a in self.alunos if a.matricula == matricula), None)
        if aluno:
            aluno.notas[codigo] = nota
            self.salvar_dados()
            return f"Nota {nota} lançada!"
        return "Aluno não encontrado!"
    
    def boletim(self, matricula):
        aluno = next((a for a in self.alunos if a.matricula == matricula), None)
        if aluno:
            print(f"\nBoletim - {aluno.nome}")
            for codigo, nota in aluno.notas.items():
                print(f"{codigo}: {nota}")
            return
        print("Aluno não encontrado!")
    
    def salvar_dados(self):
        dados = {
            'alunos': [{'nome': a.nome, 'matricula': a.matricula, 'notas': a.notas} for a in self.alunos],
            'disciplinas': [{'nome': d.nome, 'codigo': d.codigo, 'alunos': [a.matricula for a in d.alunos]} for d in self.disciplinas]
        }
        with open('dados.json', 'w') as f:
            json.dump(dados, f)
    
    def carregar_dados(self):
        try:
            with open('dados.json', 'r') as f:
                dados = json.load(f)
                self.alunos = [Aluno(a['nome'], a['matricula']) for a in dados['alunos']]
                for i, a in enumerate(dados['alunos']):
                    self.alunos[i].notas = a['notas']
                self.disciplinas = [Disciplina(d['nome'], d['codigo']) for d in dados['disciplinas']]
        except:
            pass
