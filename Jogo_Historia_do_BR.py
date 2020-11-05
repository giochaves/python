#Variaveis iniciais
pontuacao = 0
acerto = 0
erro = 0
contador = 1
checanome = 1
decisao = 0

# Funcao do menu
def menuzinho():
    global decisao
    global cont
    cont = 2
    while cont > 1:
        print('Escolha uma opção digitando o número desejado:')
        print('1. Próxima pergunta ')
        print('2. Ver pontuação atual')
        print('3. Desistir\n')
        decisao = input('Selecionar:')
        if decisao == '1':
            print('OK, vamos continuar. Boa sorte!\n')
            cont = 0
        elif decisao == '2':
            print('Sua pontuação atual é: {}\n'.format(pontuacao))
        elif decisao == '3':
            print('Desistiu é? HAHAHAAHA Eu sabia que te venceria!')
            input('Pressione enter, perdedor!')
            exit()
        else:
            print('Opção inválida, digite novamente!')

#Funcao do acerto sequencial
def acertosequencial(facerto, ferro):
    global pontuacao
    global acerto
    global erro
    if facerto == 3:
        print('Você acertou 3 seguidas, {}, Ganhou 3 pontos a mais!'.format(nome))
        acerto = 0
        pontuacao += 3
    else:
        if ferro == 3:
            print('Você errou 3 seguidas, {}, que pena! Perdeu 3 pontos a mais!'.format(nome))
            erro = 0
            pontuacao -= 3
             
#Funcao que recebera a pergunta
def perguntahbr(a, b, c, d, pergunta):
    print(pergunta)
    print('A) {}'.format(a))
    print('B) {}'.format(b))
    print('C) {}'.format(c))
    print('D) {}'.format(d))

# Funcao perguntas e pontuacao
def p1():
    global r1
    global acerto
    global erro
    global pontuacao
    global contador
    contador=2
    while contador > 1:
        perguntahbr(1300, 1450, 1933, 1500, 'Em que ano os portugueses chegaram ao Brasil?')
        r1 = input('Resposta:')
        if r1.upper() == 'A' or r1.upper() == 'B' or r1.upper() == 'C' or r1.upper() == 'D':
            contador = 0
        else:
            print('Poxa, você digitou um dado inválido :( \n Digite apenas alguma das alternativas!')                     

    if r1.upper() == 'D':
        print('Parabens, {}, acertou em cheio! Voce ganhou 5 pontos!\n'.format(nome))
        acerto += 1
        pontuacao += 5
    else:
        print('Voce errou, perdeu 3 pontos {}!\n'.format(nome))
        erro += 1
        pontuacao -= 3
        if pontuacao < 0:
            pontuacao = 0

    acertosequencial(acerto, erro)
    input('Pressione Enter!')
    menuzinho()
    input('Pressione enter para próxima pergunta...\n')

def p2():
    global r1
    global acerto
    global erro
    global pontuacao
    contador=2
    while contador > 1:
        perguntahbr(1889, 1877, 1630, 1522, 'Em que ano ocorreu a proclamação da república?')
        r1 = input('Resposta:')
        if r1.upper() == 'A' or r1.upper() == 'B' or r1.upper() == 'C' or r1.upper() == 'D':
            contador = 0
        else:
            print('Poxa, você digitou um dado inválido :( \n Digite apenas alguma das alternativas!')                     

    if r1.upper() == 'A':
        print('Parabens, {}, acertou em cheio! Voce ganhou 5 pontos!\n'.format(nome))
        pontuacao += 5
        acerto += 1
    else:
        print('Voce errou, perdeu 3 pontos {}!\n'.format(nome))
        erro += 1
        pontuacao -= 3
        if pontuacao < 0:
            pontuacao = 0
            
    acertosequencial(acerto, erro)
    input('Pressione Enter!')
    menuzinho()
    input('Pressione enter para próxima pergunta...\n')

def p3():
    global r1
    global acerto
    global erro
    global pontuacao
    contador=2
    while contador > 1:
        perguntahbr(1934, 1315, 1888, 1500, 'Em qual ano foi assinada a Lei Áurea que "libertou" os escravos?')
        r1 = input('Resposta:')
        if r1.upper() == 'A' or r1.upper() == 'B' or r1.upper() == 'C' or r1.upper() == 'D':
            contador = 0
        else:
            print('Poxa, você digitou um dado inválido :( \n Digite apenas alguma das alternativas!')                     

    if r1.upper() == 'C':
        print('Parabens, {}, acertou em cheio! Voce ganhou 5 pontos!\n'.format(nome))
        pontuacao += 5
        acerto += 1
    else:
        print('Voce errou, perdeu 3 pontos {}!\n'.format(nome))
        erro += 1
        pontuacao -= 3
        if pontuacao < 0:
            pontuacao = 0
            
    acertosequencial(acerto, erro)
    input('Pressione Enter!')
    menuzinho()
    input('Pressione enter para próxima pergunta...\n')

def p4():
    global r1
    global acerto
    global erro
    global pontuacao
    contador=2
    while contador > 1:
        perguntahbr(1900, 1746, 1999, 1200, 'Em que ano nasceu tiradentes?')
        r1 = input('Resposta:')
        if r1.upper() == 'A' or r1.upper() == 'B' or r1.upper() == 'C' or r1.upper() == 'D':
            contador = 0
        else:
            print('Poxa, você digitou um dado inválido :( \n Digite apenas alguma das alternativas!')                         

    if r1.upper() == 'B':
        print('Parabens, {}, acertou em cheio! Voce ganhou 5 pontos!\n'.format(nome))
        pontuacao += 5
        acerto += 1
    else:
        print('Voce errou,  perdeu 3 pontos {}!\n'.format(nome))
        erro += 1
        pontuacao -= 3
        if pontuacao < 0:
            pontuacao = 0

    acertosequencial(acerto, erro)
    input('Pressione Enter!')
    menuzinho()
    input('Pressione enter para próxima pergunta...\n')

def p5():
    global r1
    global acerto
    global erro
    global pontuacao
    contador=2
    while contador > 1:
        perguntahbr('Lula', 'Bolsonaro', 'Marechal Deodoro', 'Getulio Vargas',
                'Qual o nome do primeiro presidente do Brasil?')
        r1 = input('Resposta:')
        if r1.upper() == 'A' or r1.upper() == 'B' or r1.upper() == 'C' or r1.upper() == 'D':
            contador = 0
        else:
            print('Poxa, você digitou um dado inválido :( \n Digite apenas alguma das alternativas!')                     

    if r1.upper() == 'C':
        print('Parabens, {}, acertou em cheio! Voce ganhou 5 pontos!\n'.format(nome))
        pontuacao += 5
        acerto += 1
    else:
        print('Voce errou,  perdeu 3 pontos {}!\n'.format(nome))
        erro += 1
        pontuacao -= 3
        if pontuacao < 0:
            pontuacao = 0

    acertosequencial(acerto, erro)
    input('Pressione Enter!')
    menuzinho()
    input('Pressione enter para próxima pergunta...\n')

def p6():
    global r1
    global acerto
    global erro
    global pontuacao
    contador=2
    while contador > 1:
        perguntahbr('Joaquim Osório Duque-Estrada', 'Francisco Manuel da Silva', 'Chico Buarque', 'Michel Teló', 'Quem escreveu a letra do atual hino brasileiro?')
        r1 = input('Resposta:')
        if r1.upper() == 'A' or r1.upper() == 'B' or r1.upper() == 'C' or r1.upper() == 'D':
            contador = 0
        else:
            print('Poxa, você digitou um dado inválido :( \n Digite apenas alguma das alternativas!')                     

    if r1.upper() == 'A':
        print('Parabens, {}, acertou em cheio! Voce ganhou 5 pontos!\n'.format(nome))
        pontuacao += 5
        acerto += 1
    elif r1.upper() == 'D':
        print('FATAL ERROR ;)')
        exit()
    else:
        print('Voce errou,  perdeu 3 pontos {}!\n'.format(nome))
        erro += 1
        pontuacao -= 3
        if pontuacao < 0:
            pontuacao = 0

    acertosequencial(acerto, erro)
    input('Pressione Enter!')
    menuzinho()
    input('Pressione enter para próxima pergunta...\n')

def p7():
    global r1
    global acerto
    global erro
    global pontuacao
    contador=2
    while contador > 1:
        perguntahbr('São Paulo', 'Ceará', 'Rio de Janeiro', 'Santa Catarina','Onde fica localizada a estátua do Cristo Redentor?')
        r1 = input('Resposta:')
        if r1.upper() == 'A' or r1.upper() == 'B' or r1.upper() == 'C' or r1.upper() == 'D':
            contador = 0
        else:
            print('Poxa, você digitou um dado inválido :( \n Digite apenas alguma das alternativas!')
            
    if r1.upper() == 'C':
        print('Parabens, {}, acertou em cheio! Voce ganhou 5 pontos!\n'.format(nome))
        pontuacao += 5
        acerto += 1
    else:
        print('Voce errou,  perdeu 3 pontos {}!\n'.format(nome))
        erro += 1
        pontuacao -= 3
        if pontuacao < 0:
            pontuacao = 0

    acertosequencial(acerto, erro)
    input('Pressione Enter!')
    menuzinho()
    input('Pressione enter para próxima pergunta...\n')

def pbns():
    global r1
    #global acerto
    #global erro
    global pontuacao
    contador=2
    while contador > 1:
        perguntahbr('Cristovão Colombo', 'Pero Vaz de Caminha', 'Pedro Alvares Cabral', 'Dom Pedro II','Quem descobriu o Brasil?')
        r1 = input('Resposta:')
        if r1.upper() == 'A' or r1.upper() == 'B' or r1.upper() == 'C' or r1.upper() == 'D':
            contador = 0
        else:
            print('Poxa, você digitou um dado inválido :( \n Digite apenas alguma das alternativas!')
            
    if r1.upper() == 'C':
        print('Parabéns, você acertou a pergunta master e ganhou mais 25 pontos!\n'.format(nome))
        pontuacao += 25
        print('Aqui está sua pontuação final {}\n'.format(pontuacao))
        
    else:
        print('Voce errou a última pergunta e perdeu todos os pontos, que pena! :(\n'.format(nome))
        pontuacao = 0
        print('Aqui está sua pontuação final {}\n'.format(pontuacao))
    exit()

# Apresentacao e validação:
while checanome == 1:
    nome = input('Bem vindo ao templo do conhecimento! Voce deve obter uma pontuação acima de 15 após a última pergunta, para chegar na questão final! Como devemos te chamar? \n')
    if nome.isnumeric(): #Valida se foi digitado valor numerico ou string
        print('Digite corretamente seu nome, sem números! \n')
    else:
        nome = nome.capitalize()
        print('OK, {}, então vamos começar! Divirta-se!'.format(nome))
        input('Pressione enter para continuar...')
        checanome = 0

#Variaveis para executar as perguntas
q1=1
q=1
q3=[7]
pbonus=0
fp=['p1()','p2()', 'p3()', 'p4()', 'p5()', 'p6()', 'p7()'] #lista com todas as perguntas
while q==1:
    while q1==1:
        import random #importas biblioteca random
        q2=random.choice(fp) #Seleciona uma pergunta randomicamente
        fp.remove(q2) #remove o ultimo valor obtido da lista para não repetir a pergunta      
        exec(q2) #executa a funcao da pergunta
        if pbonus < 6:
            pbonus += 1
            print(pbonus)
        else:
            q=0
            q1=0
if pontuacao >= 15:
    print('Parabens, você fez mais de 15 pontos e chegou na pergunta bonus! Vamos lá. \n')
    input('Pressione enter para continuar...\n')
    pbns()             
            
            
