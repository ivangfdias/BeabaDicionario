"Este programa tem como objetivo separar as sílabas de uma palavra"

#Banco de letras acentuadas
acentuados = ["à","À", "á","Á", "â","Â", "ã","Ã", "è","È", 
              "é","É", "ê","Ê", "ì","Ì", "í","Í", "î","Î", 
              "ò","Ò", "ó","Ó", "ô","Ô", "õ","Õ", "ù","Ù",
              "ú","Ú", "û","Û"]
#Banco de consoantes especiais
ConsEspeciais = ["ñ",'Ñ','ç','Ç']
#Relaciona acentuadas maiusculas com sua contraparte minuscula
diciMaiToMin = {"À":"à", "Á":"á", "Â":"â", "Ã":"ã", "Ç":"ç",
              "È":"è", "É":"é", "Ê":"ê", "Ì":"ì", "Í":"í",
              "Î":"î", "Ñ":"ñ", "Ò":"ò", "Ó":"ó", "Ô":"ô",
              "Õ":"õ", "Ù":"ù", "Ú":"ú", "Û":"û", 
              "à":"à", "á":"á", "â":"â", "ã":"ã", "ç":"ç",
              "è":"è", "é":"é", "ê":"ê", "ì":"ì", "í":"í",
              "î":"î", "ñ":"ñ", "ò":"ò", "ó":"ó", "ô":"ô",
              "õ":"õ", "ù":"ù", "ú":"ú", "û":"û"}
#Relaciona acentuadas minusculas com sua contraparte maiuscula
diciMinToMai = {"à":"À", "á":"Á", "â":"Â", "ã":"Ã", "ç":"Ç",
              "è":"È", "é":"É", "ê":"Ê", "ì":"Ì", "í":"Í",
              "î":"Î", "ñ":"Ñ", "ò":"Ò", "ó":"Ó", "ô":"Ô",
              "õ":"Õ", "ù":"Ù", "ú":"Ú", "û":"Û",
              "À":"À", "Á":"Á", "Â":"Â", "Ã":"Ã", "Ç":"Ç",
              "È":"È", "É":"É", "Ê":"Ê", "Ì":"Ì", "Í":"Í",
              "Î":"Î", "Ñ":"Ñ", "Ò":"Ò", "Ó":"Ó", "Ô":"Ô",
              "Õ":"Õ", "Ù":"Ù", "Ú":"Ú", "Û":"Û",}
vogais = 'aeiouàáâãèéêìíîòóôõùúû'
consoantes = 'bcdfghjklmnpqrstvwxzçñ'

def minusculariza(letra):
    "Alternativa que engloba caracteres latinos ao .lower()"
    if letra.lower() in 'abcdefghijklmnopqrstuvwxyz':
        return letra.lower()
    else:
        return diciMaiToMin[letra]

def maiusculariza(letra):
    "Alternativa que engloba caracteres latinos ao .upper()"
    if letra.lower() in 'abcdefghijklmnopqrstuvwxyz':
        return letra.upper()
    else:
        return diciMinToMai[letra]    

def separaSilabas (palavra):
    '''Separação recursiva de silabas de uma palavra seguindo as regras do português'''
    anterior = '.'
    silabas = []
    vaiSeparar = False
    continua = True
    if len(palavra) == 1:
        silabas.append(palavra)
    else:
        for indice, letra in enumerate(palavra):
            if continua:
                letra = minusculariza(letra)

                if letra in vogais:#Vogais
                    if letra == 'a':
                        if anterior == 'i':
                            silabas.append(palavra[:indice])
                            silabas += separaSilabas(palavra[indice:])
                            continua = False
                    elif letra == 'à':
                        pass
                    elif letra == 'á':
                        pass
                    elif letra == 'â':
                        if anterior not in consoantes and indice != len(palavra) - 1:
                            vaiSeparar = True
                        else:
                            silabas.append(palavra[:indice+1])
                            silabas += separaSilabas(palavra[indice+1:])
                            continua = False

                    elif letra == 'ã':
                        pass
                    elif letra == 'e':
                        if anterior == 'o' and indice - 2 >= 0 and (palavra[indice-2] not in 'csv' or palavra[indice+1] != None):
                            silabas.append(palavra[:indice])
                            silabas += (separaSilabas(palavra[indice:]))
                            continua = False
                        elif anterior == 'u' and palavra[indice+1] in consoantes:
                            silabas.append(palavra[:indice])
                            silabas += (separaSilabas(palavra[indice:]))
                            continua = False
                    elif letra == 'é':
                        pass
                    elif letra == 'ê':
                        pass
                    elif letra == 'i':
                        pass
                    elif letra == 'í':
                        if anterior in vogais:
                            silabas.append(palavra[:indice])
                            silabas.append(palavra[indice])
                            silabas += (separaSilabas(palavra[indice+1:]))
                            continua = False
                        elif anterior == '.':
                            vaiSeparar = True
                            
                    elif letra == 'o':
                        if anterior == 'o':
                            silabas.append(palavra[:indice])
                            silabas += (separaSilabas(palavra[indice:]))
                            continua = False
                    elif letra == 'ó':
                        pass
                    elif letra == 'ô':
                        pass
                    elif letra == 'u':
                        if anterior in 'gq' and indice > 1:
                            silabas.append(palavra[:indice-1])
                            silabas += (separaSilabas(palavra[indice-1:]))
                            continua = False

                    elif letra == 'ú':
                        if anterior in vogais:
                            silabas.append(palavra[:indice])
                            silabas.append(palavra[indice])
                            silabas += (separaSilabas(palavra[indice+1:]))
                        continua = False
                    

                elif letra in consoantes:#consoantes
                    if vaiSeparar and (letra in 'nmls'):
                        print("vs",end=",")
                        silabas.append(palavra[:indice+1])
                        silabas += (separaSilabas(palavra[indice+1:]))
                        vaiSeparar = False
                        continua = False
                    else:
                        if (letra in 'rs') and anterior == letra:
                            print("rr/ss",end=",")
                            silabas.append(palavra[:indice])
                            silabas += (separaSilabas(palavra[indice:]))
                            continua = False
                        elif letra == 'h' and (anterior in 'cln') and indice > 1:
                            silabas.append(palavra[:indice-1])
                            silabas += (separaSilabas(palavra[indice-1:]))
                            continua = False
                        elif letra in 'rl' and indice > 1:
                            if anterior in consoantes:
                                silabas.append(palavra[:indice-1])
                                silabas += (separaSilabas(palavra[indice-1:]))
                            elif anterior in vogais and(indice < (len(palavra) - 1) and palavra[indice+1] in vogais):
                                silabas.append(palavra[:indice])
                                silabas += (separaSilabas(palavra[indice:]))
                            else:
                                silabas.append(palavra[:indice+1])
                                silabas += (separaSilabas(palavra[indice+1:]))                                
                            continua = False
                        elif letra in 'snml' and anterior in vogais and palavra[indice+1] in vogais:
                            silabas.append(palavra[:indice])
                            silabas += (separaSilabas(palavra[indice:]))
                            continua = False
                        elif letra in 'cç' and anterior in 'sx':
                            silabas.append(palavra[:indice])
                            silabas += (separaSilabas(palavra[indice:]))
                            continua = False
                        elif letra in 'jbdzckpt' and indice > 0:
                            silabas.append(palavra[:indice])
                            silabas += (separaSilabas(palavra[indice:]))
                            continua = False
                            '''elif letra in 'nm' and anterior in vogais and palavra[indice+1] in vogais:
                            silabas.append(palavra[:indice])
                            silabas += (separaSilabas(palavra[indice:]))
                            continua = False'''
                
                if indice >= len(palavra) - 1 and continua:
                    silabas.append(palavra)
                    continua = False        
            else:
                
                break
            
            anterior = letra
    return silabas


#print(separaSilabas('framboesia'),end='1\n')
#print(separaSilabas('basílica'),end='2\n')