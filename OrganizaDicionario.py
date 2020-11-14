"Este programa tem como objetivo organizar em um .xml palavras compiladas em um arquivo .txt"

from xml.etree.ElementTree import Element, SubElement, Comment, tostring, ElementTree
from xml.dom import minidom
from progress.bar import Bar
def prettify(elem):
    #"""Return a pretty-printed XML string for the Element.
    #"""
    rough_string = tostring(elem, 'unicode')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


def corta_do_fim(texto, sufixo):
    if not texto.endswith(sufixo):
        return texto
    return texto[:len(texto)-len(sufixo)]
def corta_do_comeco(texto, prefixo):
    if not text.startswith(prefixo):
        return texto
    return text[len(texto)-len(prefixo):]
def determinaConjugacao(texto):
    if texto.endswith("ar"):
        return 1
    if texto.endswith("er"):
        return 2
    if texto.endswith("ir"):
        return 3
    return -1    

def parsear (documento):
    arquivo = open(documento, 'r', encoding='utf-8')
    palavras = []
    
    palavra = ""
    linha = 0
    for line in arquivo:
        palavra0eSilaba = []
        palavra, silaba_aux = line.split("|")
        silabas = silaba_aux.split("-")
        i = 0
        palavra0eSilaba.append(palavra)
        for silaba in silabas:
            silaba = corta_do_fim(silaba, "\n")
            palavra0eSilaba.append(silaba) 
            i += 1
        #print(palavra0eSilaba)
        palavras.append(palavra0eSilaba)
        linha += 1
    
    arquivo.close
    return palavras

dicionario = Element('dicionario')
comment = Comment('Dicionario de Palavras!')
dicionario.append(comment)
print(prettify(dicionario))

with Bar('\b\b\b\b1 silaba', max=len(parsear("palavra1.txt"))) as bar:
    for item in parsear("palavra1.txt"):
        elemPalavra = SubElement(dicionario, 'palavra', {'escrita':item[0]})
        numSilabas = SubElement(elemPalavra, 'qtdSilabas')
        numSilabas.text = str(len(item) - 1)
        silabas = SubElement(elemPalavra, 'Silabas')
        textoSilabas = ''
        for indice, silaba in enumerate(item[1:]):
            textoSilabas+=(silaba)
            if(indice < len(item[1:])-1):
                textoSilabas+=("-")
        silabas.text = textoSilabas
        bar.next()
with Bar('\b\b\b\b2 silabas', max=len(parsear("palavra2.txt"))) as bar:
    for item in parsear("palavra2.txt"):
        #palavra = item[0]
        elemPalavra = SubElement(dicionario, 'palavra', {'escrita':item[0]})
        numSilabas = SubElement(elemPalavra, 'qtdSilabas')
        numSilabas.text = str(len(item) - 1)
        silabas = SubElement(elemPalavra, 'Silabas', {'separacao':''})
        textoSilabas = ''
        for indice, silaba in enumerate(item[1:]):
            textoSilabas+=(silaba)
            if (indice < len(item[1:])-1):
                textoSilabas+=("-")
        silabas.set('separacao',textoSilabas)
        bar.next()
with Bar('\b\b\b\b3 silabas', max=len(parsear("palavra3.txt"))) as bar:
    for item in parsear("palavra3.txt"):
        elemPalavra = SubElement(dicionario, 'palavra', {'escrita':item[0]})
        numSilabas = SubElement(elemPalavra, 'qtdSilabas')
        numSilabas.text = str(len(item) - 1)
        silabas = SubElement(elemPalavra, 'Silabas')
        textoSilabas = ''
        for indice, silaba in enumerate(item[1:]):
            textoSilabas+=(silaba)
            if (indice < len(item[1:])-1):
                textoSilabas+=("-")
        silabas.text = textoSilabas
        bar.next()
with Bar('\b\b\b\b4 silabas', max=len(parsear("palavra4.txt"))) as bar:
    for item in parsear("palavra4.txt"):
        elemPalavra = SubElement(dicionario, 'palavra', {'escrita':item[0]})
        numSilabas = SubElement(elemPalavra, 'qtdSilabas')
        numSilabas.text = str(len(item) - 1)
        silabas = SubElement(elemPalavra, 'Silabas')
        textoSilabas = ''
        for indice, silaba in enumerate(item[1:]):
            textoSilabas+=(silaba)
            if (indice < len(item[1:])-1):
                textoSilabas+=("-")
        silabas.text = textoSilabas
        bar.next()
with Bar('\b\b\b\b5 silabas', max=len(parsear("palavra5.txt"))) as bar:
    for item in parsear("palavra5.txt"):
        elemPalavra = SubElement(dicionario, 'palavra', attrib={'escrita':item[0]})
        numSilabas = SubElement(elemPalavra, 'qtdSilabas')
        numSilabas.text = str(len(item) - 1)
        silabas = SubElement(elemPalavra, 'Silabas')
        textoSilabas = ''
        for indice, silaba in enumerate(item[1:]):
            textoSilabas+=(silaba)
            if indice < len(item[1:])-1:
                textoSilabas+=("-")
        silabas.text = textoSilabas
        #print(elemPalavra)
        
        #print(ElementTree.tostring(elemPalavra, encoding='unicode'))
        bar.next()
with Bar('\b\b\b\bVerbos', max=len(parsear("verbos.txt"))) as bar:
    for item in parsear("verbos.txt"):
        elemPalavra = SubElement(dicionario, 'palavra', attrib={'escrita':item[0]})
        numSilabas = SubElement(elemPalavra, 'qtdSilabas')
        numSilabas.text = str(len(item) - 1)
        silabas = SubElement(elemPalavra, 'Silabas')
        textoSilabas = ''
        for indice, silaba in enumerate(item[1:]):
            textoSilabas+=(silaba)
            if indice < len(item[1:])-1:
                textoSilabas+=("-")
        silabas.text = textoSilabas
        classe = SubElement(elemPalavra, 'classe')
        classe.text = 'verbo'
        conjugacao = SubElement(elemPalavra, 'conjugacao', attrib={'tipo':str(determinaConjugacao(item[0]))})
        #print(elemPalavra)
        
        #print(ElementTree.tostring(elemPalavra, encoding='unicode'))
        bar.next()


banco = open("bancoPalavras.xml", 'w',encoding='utf-8')
print (prettify(dicionario))
banco.write(prettify(dicionario))
