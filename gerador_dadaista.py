
"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Caio Túlio de Deus Andrade
  NUSP : 9797323
  Turma: BCC 2018
  Prof.: Marcelo Queiroz

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma referência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
  
  """

from random import randint
def main() :

    substantivos = armazena_substantivos()
    verbos = armazena_verbos()
    rima = input ("Voce deseja uma poesia com rima? Responda sim ou nao:\n")
    numeroDeVersos = int(input("Quantos versos voce deseja que a poesia tenha?"))
    produz_versos(substantivos, verbos, numeroDeVersos, rima)

def embaralha_ordem(ordem) : 
    """ 
        Função que recebe um vetor vazio e coloca numeros de 0 a 2 embaralhados
        nele.
    """

    for k in range(3) :
        ordem.append(k)
    for l in range(3) : 
        N = randint(0,2)
        while l == N : 
            N = randint(0,2)
            ##garante que os N sorteados sejam distindos entre si
        posicao_do_Lesimo_elemento = ordem[l]
        ordem[l] = ordem[N]
        ordem[N] = posicao_do_Lesimo_elemento

def produz_versos(substantivos, verbos, numeroDeVersos, rima) :
    """ 
        Função que recbebe uma lista de substantivos, verbos, o numero de versos
        , e se o usuário quer rima ou não, e produz um poema (rimado ou não). 
        A função armazena os termos como digitados pelo usuario em frase_bruta,
        além da preposição do verbo e o artigo do objeto. Posteriormente, a 
        entrada do usuário é gramaticalmente tratada, e armazenada em verso.
    """

    n_subs = len(substantivos)
    n_verbs = len(verbos)
    conjuncoes = ['como','e','enquanto','mesmo quando','porque','quando','se','toda vez que']
    rimaanterior = ''
    vetor_indicador_substantivos = gerador_booleano_nulo(n_subs)
    vetor_indicador_verbos = gerador_booleano_nulo(n_verbs)

    for i in range(numeroDeVersos) :

        frase_bruta = []         
        """
            Convenção : sujeito, verbo, objeto, preposição do verbo e artigo 
            do objeto correspondem as casas 0,1,2,3,4 respectivamente
        """

        ordem = []

        """
            Cada casa do vetor representa, por conveção,uma classe 
            gramatical : 0 = sujeito, 1 = verbo, 2 = objeto.
            Dessa forma, cada ordem[i] representa a posição aleatoria de
            i no verso já sorteado.
        """           


        verso = [[],[],[]] 

        """
            Vetor vazio que, ao longo do laço for, recebe os termos de 
            frase_bruta, mas tratados gramaticalmente (Frase pontuada com
            ponto final, objetos com preposição e artigo, etc), e seguindo
            a distribuição de sujeito, verbo e objeto determinada pelo vetor
            ordem.
        """


        substantivo = sorteia_subst(substantivos, vetor_indicador_substantivos)
        frase_bruta.append(substantivo)

        verbo = sorteia_verbos(verbos, vetor_indicador_verbos)
        frase_bruta.append(verbo) 

        objeto = sorteia_subst(substantivos, vetor_indicador_substantivos)
        frase_bruta.append(objeto)

        conjuncao = sorteia_conjuncao(conjuncoes)
        embaralha_ordem(ordem)

        verbo_e_preposicao = frase_bruta[1].split()
        frase_bruta.append(verbo_e_preposicao[1])
        
        artigo_e_objeto = frase_bruta[2].split()
        frase_bruta.append(artigo_e_objeto[0])
        preposição_com_artigo = cria_preposicao_objeto(frase_bruta[3], frase_bruta[4])  
        frase_bruta[1] = verbo_e_preposicao[0]

        if preposição_com_artigo != '' : 
            frase_bruta[2] = artigo_e_objeto[1]

        frase_bruta[1] = verbo_e_preposicao[0]
        frase_bruta[2] = preposição_com_artigo + frase_bruta[2] 

        if conjuncao != False :

            verso.append([])
            verso[0] = conjuncao
            for j in range(3) :

                indice = ordem[j] 
                verso[j+1] = frase_bruta[indice] 
        else : 
            for j in range(3) :

                indice = ordem[j]
                verso[j] = frase_bruta[indice]
        tamanho_frase = len(verso)
        indice_ultima_palavra_verso = ordem.index(2)
        if indice_ultima_palavra_verso == 2 or indice_ultima_palavra_verso == 0 : 
            ultima_palavra_verso = 'substantivo'
        else : 
            ultima_palavra_verso = 'verbo'
        if rima == 'sim' : 

            rimou_com_substantivo = False
            rima_verso = acha_rima(verso[tamanho_frase-1])

            if i == 0 or i%2 == 0: 
                #Garante que a rima é da forma AABBCCDD...
                rimaanterior = rima_verso
                verso[0] = verso[0].capitalize()

            else : 

                contador = 0

                if ultima_palavra_verso == 'substantivo' : 
                    while (rima_verso != rimaanterior and contador < n_subs + n_verbs) :
                            substantivo_sorteado = sorteia_subst(substantivos, vetor_indicador_substantivos)
                            rima_verso = acha_rima(substantivo_sorteado)
                            contador += 1

                    if rima_verso == rimaanterior and contador > 0: 
                        """
                         contador > 0 é condição para evitar um assignement error
                         com substantivo_sorteado, no caso em que o substantivo 
                         sorteado, por sorte, já rima.
                        """
                        artigo_e_objeto = substantivo_sorteado.split()
                        frase_bruta[4] = artigo_e_objeto[0]
                        preposicao_com_artigo = cria_preposicao_objeto(frase_bruta[3],frase_bruta[4])

                        if indice_ultima_palavra_verso == 2 : 
                            verso[tamanho_frase-1] = preposicao_com_artigo + artigo_e_objeto[1]
                        else : 
                            verso[tamanho_frase-1] = substantivo_sorteado

                        """     Se a palavra sorteada for um objeto, demanda-se 
                                que ela tenha um certo tratamento gramatical (
                                inserção de preposição e contração com o artigo)
                                no entanto, se for um sujeito, basta que seja 
                                adcionada ao fim do verso o artigo e o substantivo
                        """
                        rimaanterior = rima_verso
                else :       

                    contador = 0
                    while (rima_verso != rimaanterior and contador < n_verbs + n_subs) :
                        verbo_sorteado = sorteia_verbos(verbos, vetor_indicador_verbos)
                        verbo_sorteado_com_preposicao = verbo_sorteado.split()
                        verbo_sorteado_sem_preposicao = verbo_sorteado_com_preposicao
                        rima_verso = acha_rima(verbo_sorteado_sem_preposicao)
                        contador += 1

                    if rima_verso == rimaanterior and contador > 0:
                        """
                         contador > 0 é condição para evitar um assignement error
                         com verbo_sorteado_com_preposicao, no caso em que o 
                         verbo sorteado, por sorte, já rima.
                        """
                        frase_bruta[3] = verbo_sorteado_com_preposicao
                        preposicao_com_artigo = cria_preposicao_objeto(frase_bruta[3],frase_bruta[4])
                        indice_objeto = ordem[2]
                        verso[indice_objeto] = preposicao_com_artigo + frase_bruta[2] 
                        verso[tamanho_frase-1] = verbo_sorteado_sem_preposicao
                    rimaanterior = rima_verso

            if i%4 == 0 :
                print('')

        if i%2 != 0 or i == numeroDeVersos-1:
            ultimo = len(verso)-1
            verso[ultimo] += '.'

        for h in range(tamanho_frase):
            print(verso[h], end = ' ')

        print("") 


def sorteia_subst(substantivos, vetor_indicador_substantivos) :
    """
        Recebe uma lista de substantivos e retorna um substantivo aleatório (que
        não foi sorteado antes). 
    """
    num_subs = len(substantivos)
    indice_sorteado = randint(0, num_subs-1)
    sorteios = 0
    while (vetor_indicador_substantivos[indice_sorteado] == 1 and sorteios < num_subs) :
        indice_sorteado = randint(0, num_subs-1)
        sorteios += 1
    vetor_indicador_substantivos[indice_sorteado] = 1
    substantivo_sorteado = substantivos[indice_sorteado]
    return substantivo_sorteado

def sorteia_verbos (verbos, vetor_indicador_verbos) :
    """
        Recebe uma lista de substantivos e retorna um substantivo aleatório (que
        não foi sorteado antes). 
    """
    num_verbs = len(verbos)
    indice_sorteado = randint(0, num_verbs-1)
    sorteios = 0
    while (vetor_indicador_verbos[indice_sorteado] == 1 and sorteios < num_verbs) :
        indice_sorteado = randint(0, num_verbs-1)
        sorteios += 1
    vetor_indicador_verbos[indice_sorteado] = 1
    verbo_sorteado = verbos[indice_sorteado]
    return verbo_sorteado
def acha_rima(palavra) :
    """
        Função que retorna as duas ultimas letras de uma frase, para que o pró-
        ximo verso rime com o atual
    """
    tamanho_palavra = len(palavra)
    rima = palavra[tamanho_palavra-2:]
    return rima


def sorteia_conjuncao(conjuncoes) : 
    """
        Recebe uma lista de conjunções e retorna uma conjunção aleatóra (cada 
        conjunção possui uma possibilidade de 1/3 de aparecer). O caso do
        sorteio valer 1 é totalmente arbitrário, apenas é usado para fixar a 
        probabilidade
    """ 
    n_conjuncoes = len(conjuncoes)
    sorteio = randint(0,2)
    if sorteio == 1 : ##valor arbitrario, fazendo a probabilidade ser 1/3
       indice_conjuncao = randint(0,n_conjuncoes-1)
       conjuncao = conjuncoes[indice_conjuncao]
       return conjuncao
    else :
        return False



def gerador_booleano_nulo (tamanho) :
    """
        Cria um vetor nulo de len = tamanho.
    """
    booleano = []
    for i in range (tamanho) :
        booleano.append(0)
    return booleano


def cria_preposicao_objeto (preposicao_verbo, artigo_substantivo) : 
    """
        Função que recebe a preposição do verto e o artigo do substantivo, e retorna
        a contração entre os dois
    """
    
    if preposicao_verbo == '-' :
        return ''
    if preposicao_verbo == 'de' :
        if artigo_substantivo == 'a' :
            return 'da '
        else :
            return 'do '    
    if preposicao_verbo == 'em' :
        if artigo_substantivo == 'a' :
            return 'na '
        else :
            return 'no '
    if preposicao_verbo == 'a' :
        if artigo_substantivo == 'a' :
            return ' '
        else :
            return 'ao '
    if preposicao_verbo == 'por' :
        if artigo_substantivo == 'a' :
            return 'pela '
        else :
            return 'pelo '
    if preposicao_verbo == 'com' or preposicao_verbo == 'para' : 
        return preposicao_verbo + ' ' + artigo_substantivo + ' '
    print("\t\t",preposicao_verbo, artigo_substantivo)


def armazena_verbos() : 
    """
        Função utilizada para interagir com o usuário, pedindo e armazenando os
        verbos digitados
    """
    verbos = []
    lenght_verbos = int(input("Quantos verbos voce deseja utilizar?\n"))
    print ("Digite um verbo (com preposição) por linha:")
    for i in range(lenght_verbos) :
        verbos.append(input(""))
    return verbos

def armazena_substantivos() :
    """
        Função utilizada para interagir com o usuário, pedindo e armazenando os
        verbos digitados
    """
    substantivos = []
    lenght_substantivos = int(input("Quantos substantivos voce deseja utilizar?\n"))
    print ("Digite um substantivo (com artigo) por linha:")
    for i in range(lenght_substantivos) :
        substantivos.append(input(""))
    return substantivos

main()
