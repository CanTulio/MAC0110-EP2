def produzversos(substantivos, verbos, numeroDeVersos, rima) :
    entradededados()
    for i in range(numeroDeVersos) :
        ##inicializa a frase bruta
        frase_bruta = [] ##convenção : sujeito, verbo, objjeto, conjunção, preposição do verbo e artigo do objeto correspondem as casas 0,1,2,3,4,5 respectivamente
        ordem = [] #cada iesima casa representa a iesima casa de frase_bruta, o conteudo de ordem[i] fala em qual casa de frase está o termo frase_bruta[i]
        verso = [ , , ]
        substantivo = sorteia_substantivos(substantivos)
        frase_bruta.append(substantivo)
        verbo = sorteia_verbo(verbos)
        frase_bruta.append(verbo) 
        objeto = sorteia_substantivos
        frase_bruta.append(objeto)
        preposição = sorteia_preposicao()
        frase_bruta.append(preposição)

        ##ordena
        tamanho_frase = 3
        if preposição != False : 
            verso.append(' ')
            tamanho_frase += 1
        for i in range(tamanho_frase) : 
            N = randint(0,tamanho_frase-1)
            ordem.append(N)

        ##gramatica

        verbo_e_preposicao = frase_bruta[1].split
        artigo_e_objeto = frase_bruta[2].split
        frase_bruta.append(verbo_e_preposicao[1])
        frase_bruta.append(artigo_e_objeto[0])
        preposição_com_artigo = junta_preposicao(frase_bruta[4], frase_bruta[5])
        frase_bruta[1] = verbo_e_preposicao[0]
        frase_bruta[2] = preposição_com_artigo + frase_bruta[2]

        ## cria frase
        
        for i in range(tamanho_frase) :
            indice = ordem[i] ## guarda para qual lugar o i esimo termo deve ir
            frase[indice] = frase_bruta[i]

        # rima





