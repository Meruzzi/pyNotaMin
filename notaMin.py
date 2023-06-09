
#Array com os candidatos disponiveis para verificar as notas
candidatos = [
    ('Candidato um',5,10,8,8),
    ('Candidato dois',10,7,7,8),
    ('Candidato tres',8,5,4,9),
    ('Candidato quatro',2,2,2,1),
    ('Candidato cinco',10,10,8,9)
]

#Função para verificar as notas dos candidatos disponiveis na Array e retornar em uma lista os usuarios qualificados.
def verificarCanditados(notaMin1, notaMin2, notaMin3, notaMin4):
    listaCanditadosSelecionados = []
    for candidato in candidatos:
        nomeCandidato = candidato[0]
        nota1 = candidato[1]
        nota2 = candidato[2]
        nota3 = candidato[3]
        nota4 = candidato[4]
        if nota1 >= notaMin1 and nota2 >= notaMin2 and nota3 >= notaMin3 and nota4 >= notaMin4:
            listaCanditadosSelecionados.append(nomeCandidato)
    return listaCanditadosSelecionados

#Função com o inicio do programa, perguntando quantas vezes o usuario deseja fazer a verificação de notas e pergunta a nota minima desejada.
def inicioPrograma():
    print("Ola, seja bem vindo!")

    #Verifica se o número é acima de 0.
    while True:
        try:
            qntVezes = int(input("Quantas vezes deseja verificar a nota dos candidatos? "))
            if qntVezes > 0:
                break
            else:
                print("A quantidade de vezes deve ser acima de 0.")
        except ValueError:
            print("Informe apenas números.")
    
    for i in range(qntVezes):
        if i == 0:
            print("Informe as notas mínimas:")
        else:
            print(f"Informe as notas mínimas do {i+1} candidato:")
        
        #Verifica se as respostas foram números validos
        while True:
            try:
                notaMin1 = int(input("Nota minima 1: "))
                notaMin2 = int(input("Nota minima 2: "))
                notaMin3 = int(input("Nota minima 3: "))
                notaMin4 = int(input("Nota minima 4: "))
                break
            except ValueError:
                print("Por favor, informe apenas números.")
        
        #Verifica se as notas estao entre 1 e 10
        while not (1 <= notaMin1 <= 10 and 1 <= notaMin2 <= 10 and 1 <= notaMin3 <= 10 and 1 <= notaMin4 <= 10):
            print("As notas mínimas devem estar entre 1 e 10.")
            notaMin1 = int(input("Nota minima 1: "))
            notaMin2 = int(input("Nota minima 2: "))
            notaMin3 = int(input("Nota minima 3: "))
            notaMin4 = int(input("Nota minima 4: "))

        listaCanditadosSelecionados = verificarCanditados(notaMin1, notaMin2, notaMin3, notaMin4)
        if len(listaCanditadosSelecionados) > 0:
            print("Candidatos que possuem a nota minima informada:")
            for candidato in listaCanditadosSelecionados:
                print(candidato)
        else:
            print("Nenhum candidato conseguiu a nota minima.")

inicioPrograma()