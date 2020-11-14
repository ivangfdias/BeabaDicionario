"Este código tem o objetivo de gerar conteúdo fonético das palavras para facilitar rimas."

# Foi tomado como base https://michaelis.uol.com.br/escolar-ingles/transcricao-fonetica-do-portugues/
# Vogais orais:     {10:ah, 11:eh, 12: e, 13: í, 14: oh, 15: o,16:ú, 17:a, 18: â}
# Vogais nasais:    {19:an, 20: en, 21: in, 22: on, 23: un}
# Semivogais:       {24:i, 25: u}
# Consoantes:       {26:p, 27:b, 28:t, 29:d, 30:f, 31:v, 32:m, 33:n, 34:l, 35:k,
#                         36:g, 37:s, 38:z, 39:x, 40:j, 41:lh, 42:nh, 43: r, 44: rr}
from silaba import separaSilabas as separa
#Banco de letras acentuadas
acentuados = ["à","À", "á","Á", "â","Â", "ã","Ã", "è","È", 
              "é","É", "ê","Ê", "ì","Ì", "í","Í", "î","Î", 
              "ò","Ò", "ó","Ó", "ô","Ô", "õ","Õ", "ù","Ù",
              "ú","Ú", "û","Û"] 
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

escritaSonora = {-1 : "", 10:"á", 11:"é", 12: "e", 13: "í", 14: "ó", 15: "o",16:"ú", 17:"a", 18: "â",
19:'ã', 20: '~e', 21: "~i", 22: 'õ', 23: '~u',24:'i', 25: 'u',26:'p', 27:'b', 28:'t', 29:'d', 30:'f', 
31:'v', 32:'m', 33:'n', 34:'l', 35:'k',36:'g', 37:'s', 38:'z', 39:'x', 40:'j', 41:'lh', 42:'nh', 43: 'r', 44: "rr", -1: ""}


class Palavra:
    "Classe de Palavras, usadas para determinar fonia e agrupar quantidade de silabas em um mesmo lugar."
    escrita = ""
    qtdSilabas = 0
    silabas = []
    tonica = ""
    indiceTonica = -1
    def __init__(self, texto, inteiro, vetorTexto, silabaTonica):
        "A Silaba Tonica é a última (1), penúltima (2) ou antepenúltima (3)"
        self.escrita = texto
        self.qtdSilabas = inteiro
        self.silabas = vetorTexto
        self.indiceTonica = len(self.silabas) - silabaTonica
        self.tonica = self.silabas[len(self.silabas) - silabaTonica]
    def getLetra(self, indice):
        "Auto explicativo; pega a letra no indice"
        if len(self.escrita) > indice:
            return self.escrita[indice]
        else:
            return ""
    def getSilaba(self, indiceDaLetra):
        "Retorna a silaba que contem a letra indicada por indiceDaLetra"
        silaba = 0
        somaLetras = len(self.silabas[0])
        
        while (indiceDaLetra >= somaLetras):
            silaba += 1
            somaLetras += len(self.silabas[silaba])
        return self.silabas[silaba]
    def getFinal(self, tamanho = 1):
        "Determina a ultima letra"
        if tamanho < len(self.escrita):
            return self.escrita[:tamanho]
        else:
            return ""
    def isInSilabasDiferentes(self,indice1, indice2):
        "Determina se duas letras estao na mesma silaba"
        silaba1 = 0
        somaLetras1 = len(self.silabas[silaba1])
        while (indice1 > somaLetras1):
            silaba1 += 1
            somaLetras1 += len(self.silabas[silaba1])
        silaba2 = 0
        somaLetras2 = len(self.silabas[silaba2])
        while (indice2 > somaLetras2):
            silaba2 += 1
            somaLetras2 += len(self.silabas[silaba2])
        return silaba1 == silaba2
    def estaNaTonica(self, indiceDaLetra):
        silaba = self.getSilaba(indiceDaLetra)
        return silaba == self.tonica
    def ehTonica (self, silaba):
        return silaba == self.tonica

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

def getNumVogais(silaba):
    "Retorna o numero de vogais na silaba"
    qtdVogais = 0
    for letra in silaba:
        if letra.lower() in 'aeiou' or letra in acentuados:
            qtdVogais += 1
    return qtdVogais
    
    
def ehHiato(silaba):
    "Retorna um booleano para ver se aquela silaba é hiato ou não"
    qtdVogais = 0
    for letra in silaba:
        if letra.lower() in 'aeiou' or letra in acentuados:
            qtdVogais += 1
    return qtdVogais > 1

def temAcento (silaba):
    "True se tiver um acento na silaba, False caso contrario"
    return any(char in acentuados for char in silaba)

def determinaTonica(silabas):
    "Uma sílaba acentuada é tônica, invariavelmente."
    for indice, silaba in enumerate(silabas):
        for acentuada in 'àáâêéíóôú':
            if acentuada in silaba:
                return len(silabas) - indice

def determinaFonema(palavra, indice, somAnterior = 0):
    "Determina a fonética de cada letra na palavra e retorna em uma espécie de escrita acentuada"

    anterior= ""
    prox = ""

    naoNoComeco = (indice > 0)
    if (naoNoComeco):
        anterior = palavra.getLetra(indice-1)
    aux = minusculariza(palavra.getLetra(indice))
    naoNoFinal = (indice < len(palavra.escrita) - 1)
    silabaAux = palavra.getSilaba(indice)
    if naoNoFinal:
        prox = palavra.getLetra(indice+1)
    # Á + A*(N+M) (Som A aberto)
    if (aux.lower() in 'aeiou' or aux in acentuados):
        if (aux == "á"):
            return 10
        # Â + A*((M+N+NH)*SilabasDiferentes) (Som de â)
        elif (aux == "â") or naoNoFinal and (aux == "a" and ((prox == "n" or prox == "m") and not palavra.isInSilabasDiferentes(indice,indice+1))):
            return 18
        # Ã + A*(M+N+NH)*SilabasIguais (Som de ã, an)
        elif (aux == "ã") or naoNoFinal and (aux == "a" and ((prox == "n" or prox == "m"))):
            return 19
        # A (Som A normal)
        elif aux == "a":
            return 10
        # É + E*(Pq*(O + OS))
        elif aux == "é" or naoNoFinal and (aux == "e" and (len(palavra.escrita) < 6) and (palavra.getFinal() == "o" or palavra.getFinal(1) == "os")):
            return 11
        elif aux == "e":
            return 12
        elif aux == "í":
            if naoNoFinal and (prox == "m" or prox == "n"):
                return 20
            else:
                return 13
        elif aux == "i":
            if naoNoFinal and (prox == "m" or prox == "n"):
                return 21
            elif not ehHiato(silabaAux):
                return 24
            else:
                return 13  
        elif aux == "ó":
            return 14 
        elif aux == "õ":
            return 22
        elif aux == "ô":
            return 15
        elif aux == "o":
            if naoNoFinal and (prox == "m" or prox == "n") and not palavra.isInSilabasDiferentes(indice,indice+1):
                return 22
            elif(palavra.estaNaTonica(indice) and not ehHiato(silabaAux)):
                return 14
            else:
                return 15
        elif aux == "u":
            if (naoNoFinal and (prox == "m" or prox == "n")):
                return 23
            elif naoNoComeco and (anterior == "g" or anterior == "q" and prox == "e" or prox == "i" or prox in acentuados[8:20]):
                return -1
            elif (ehHiato(silabaAux)) or (ehHiato(silabaAux) and "i" in silabaAux) or ((palavra.estaNaTonica(indice)) and ("g" in silabaAux and "q" in silabaAux and (prox in acentuados[0:8] or prox == "a" or prox == "o" or prox in acentuados [20:28]))):
                return 16

            else:
                return 25
        elif aux == "ú":
            return 16
        return -1
    else:
        if aux == "p": 
            return 26
        elif aux == "b":
            return 27
        elif aux == "t":
            return 28
        elif aux == "d":
            return 29
        elif aux == "f":
            return 30
        elif aux == "v":
            return 31
        elif aux == "m":
            return 32
        elif aux == "n":
            if prox == "h":
                return 42
            else:
                return 33
        elif aux == "l":
            if naoNoComeco and (anterior.lower() in 'aeiou' or anterior in acentuados) and not palavra.isInSilabasDiferentes(indice-1, indice):
                return 25
            elif prox == "h":
                return 41
            else:
                return 34
        elif aux == "c":
            if prox == "h":
                return 39
            elif prox == "e" or prox == "i" or prox in acentuados[8:20]:
                return 37
            else:
                return 35
        elif aux == "q" or aux == "k":
            return 35
        elif aux == "ç":
            return 37
        elif aux == "g":
            if (not prox.lower() in 'aeiou') or prox == "o" or prox == "u" or prox == "a" or prox in acentuados[0:9] or prox == "ú":
                return 36
            else:
                return 40
        elif aux == "s":
            if naoNoComeco and naoNoFinal and (prox.lower() in 'aeiou' or prox in acentuados) and (anterior.lower() in 'aeiou' or anterior in acentuados):
                return 38
            else:
                return 37
        elif aux == "z":
            return 38
        elif aux == "x":
            if naoNoComeco and naoNoFinal and (prox.lower() in 'aeiou' or prox in acentuados) and (anterior.lower() in 'aeiou' or anterior in acentuados):
                return 38
            else:
                return 39
        elif aux == "j":
            return 40
        elif aux == "r":
            if not naoNoComeco and naoNoFinal and (anterior == "r" or prox == "r" or anterior == "n"):
                return 44
            else:
                return 43
        return -1
             
def fonetizar(escrita, tonica):
    "Opera a função determinaFonema() sobre a palavra toda e printa a fonetização da palavra"
    "Exemplo: fonetizar(hipotálamo,3) tem como output ipoTÁlãmo "

    palavra = Palavra(escrita, len(separa(escrita)), separa(escrita), tonica)
    i = 0
    somAnterior = 0
    somTotal = []
    for indice, letra in enumerate(palavra.escrita):
        somAnterior = determinaFonema(palavra,indice, somAnterior)
        somTotal.append(somAnterior)
    print("Palavra escrita:" + palavra.escrita)
    print("Palavra falada", end=":")
    for indice,som in enumerate(somTotal):
        if palavra.estaNaTonica(indice):
                print(maiusculariza(escritaSonora[som]), end = "")
        else:
            print(escritaSonora[som], end = "")

#Testes
print(".")
print(determinaTonica(separa('')))
fonetizar("hipotálamo", 3)