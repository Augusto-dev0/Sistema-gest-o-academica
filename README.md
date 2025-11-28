🎓 Sistema de Gestão Acadêmica

Um sistema simples e eficiente para gerenciamento acadêmico desenvolvido em Python.

📋 Funcionalidades

· ✅ Cadastro de alunos
· ✅ Cadastro de disciplinas
· ✅ Matrícula de alunos em disciplinas
· ✅ Lançamento de notas
· ✅ Emissão de boletins
· ✅ Persistência de dados em JSON

🚀 Como Executar

Pré-requisitos

· Python 3.6 ou superior instalado

Passo a Passo:

1. Baixe os arquivos e coloque na mesma pasta:
   · sistema_academico.py
   · teste_sistema.py (opcional - para teste rápido)
   · interface.py (opcional - para uso interativo)  
2. Abra o terminal na pasta dos arquivos
3. Execute o sistema:
   Opção 1 - Teste Rápido:
   bash
   "python teste_sistema.py"
   - Irá executar um teste automático mostrando todas as funcionalidades
   
   Opção 2 - Modo Interativo:
   bash
   "python interface.py"
   - Irá abrir um menu onde você pode usar todas as funcionalidades

🎮 Como Usar
- No Modo Interativo:
- Ao executar python interface.py, você verá este menu:

1-Cadastrar Aluno
2-Cadastrar Disciplina  
3-Matricular
4-Lançar Nota
5-Boletim
0-Sair

Exemplo de uso:

1. Cadastre um aluno: Opção 1 → Nome: "Maria" → Matrícula: "20240001"
2. Cadastre uma disciplina: Opção 2 → Nome: "Matemática" → Código: "MAT101"
3. Matricule o aluno: Opção 3 → Matrícula: "20240001" → Código: "MAT101"
4. Lance uma nota: Opção 4 → Matrícula: "20240001" → Código: "MAT101" → Nota: 8.5
5. Veja o boletim: Opção 5 → Matrícula: "20240001"

No Teste Rápido:

O teste_sistema.py já demonstra automaticamente:

· Cadastro de aluno "João Silva"
· Cadastro de disciplina "Programação"
· Matrícula do aluno
· Lançamento de nota 9.5
· Emissão do boletim

💾 Armazenamento de Dados

Os dados são automaticamente salvos no arquivo dados.json na mesma pasta. Não é necessário fazer backup manual - o sistema gerencia tudo automaticamente!

🛠 Estrutura do Projeto


sistema_academico/
├── sistema_academico.py  # Código principal do sistema
├── teste_sistema.py      # Teste automático das funcionalidades  
├── interface.py          # Interface interativa com menu
└── dados.json           # Arquivo de dados (criado automaticamente)


📝 Exemplo de Saída

Ao usar o sistema, você verá mensagens como:


Aluno João Silva cadastrado!
Disciplina Programação cadastrada!
Aluno matriculado em Programação!
Nota 9.5 lançada!

Boletim - João Silva
COMP101: 9.5


❓ Dúvidas Comuns

Problema: "ModuleNotFoundError"
Solução: Certifique-se que todos os arquivos estão na mesma pasta

Problema: Não consegue digitar no terminal
Solução: Use o modo interativo (interface.py) em vez do teste automático

Problema: Dados sumiram após fechar
Solução: Verifique se o arquivo dados.json está na pasta - ele salva automaticamente

---

Desenvolvido para fins acadêmicos 🎯 | Python 🐍 | Gestão Escolar 📚
