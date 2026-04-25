# ===== SISTEMA DE NOTAS =====

alunos = {}

def cadastrar_aluno():
    """Pergunta nome e as 3 notas, guarda no dicionário"""
    nome = input("Por favor digite seu nome: ")
    if nome in alunos:
        print(f"Aluno {nome} já esta cadastrado no sistema. ")
        return
    nota1 = float(input("Por favor digite sua nota de matemática:  "))
    nota2 = float(input("Por favor digite sua nota de português:  "))
    nota3 = float(input("Por favor digite sua nota de ciências:  "))
    turma = input("Por favor digite sua turma: ")
    if len(turma) >= 2:
        numero = turma[0]
        letra = turma[1]
        if numero not in ["6", "7", "8", "9"] and letra.upper() not in ["A", "B", "C", "D"]:
            print(f"Turma {turma} é inválida.")
        return
    media = (nota1 + nota2 + nota3) / 3
    alunos[nome] = {                    
        "turma": turma,
        "matematica": nota1,
        "portugues": nota2,
        "ciencias": nota3,
        "média": media
    }
    print(f"Aluno {nome} cadastrado com sucesso! ")
    pass

def mostrar_todos():
    """Mostra todos os alunos e suas médias"""
    global alunos
    if not alunos:
         print("Nenhum aluno cadastrado")
    else:
         for nome, dados in alunos.items():
              print(f"Nome: {nome}, Turma: {dados['turma']}, Média: {dados['média']:.2f}")
    pass

def buscar_aluno():
    """Busca um aluno e mostra suas 3 notas individuais"""
    nome = input("Por favor digite o nome do aluno para descobrirmos:  ")
    if nome not in alunos:
        print("Aluno não cadastrado, por favor cadastre ou insira o nome correto. ")
        pass
    elif nome in alunos:
        dados = alunos[nome]
        print(f"Nome: {nome}")
        print(f"Turma: {dados['turma']}")
        print(f"Matemática: {dados['matematica']}")
        print(f"Português: {dados['portugues']}")
        print(f"Ciências: {dados['ciencias']}")
        media = (dados['matematica'] + dados['portugues'] + dados['ciencias']) / 3
        print(f"Média: {media:.2f}")

def media_turma():
    """Calcula e mostra a média de uma turma específica"""
    turma_pesq = input("Digite a turma (ex: 9A, 6B, 7C, 8D): ").upper()
    
    soma = 0
    total_notas = 0
    encontrou_aluno = False
    
    for nome, dados in alunos.items():
        if dados["turma"].upper() == turma_pesq:
            encontrou_aluno = True
            soma += dados["matematica"] + dados["portugues"] + dados["ciencias"]
            total_notas += 3
    
    if not encontrou_aluno:
        print(f"❌ Nenhum aluno encontrado na turma {turma_pesq}.")
    else:
        media = soma / total_notas
        print(f"Média da turma {turma_pesq}: {media:.2f}")

# ===== PROGRAMA PRINCIPAL =====

while True:
    print("\n=== SISTEMA DE NOTAS ===")
    print("1 - Cadastrar aluno")
    print("2 - Mostrar todos os alunos")
    print("3 - Buscar aluno")
    print("4 - Média da turma")
    print("5 - Sair")
    
    opcao = input("Escolha: ")
    
    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        mostrar_todos()
    elif opcao == "3":
        buscar_aluno()
    elif opcao == "4":
        media_turma()
    elif opcao == "5":
        print("Programa encerrado!")
        break
    else:
        print("Opção inválida!")