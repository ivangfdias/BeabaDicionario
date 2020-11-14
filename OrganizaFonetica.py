"Este código tem o objetivo de organizar em um banco .xml a fonetização de palavras"

from xml.etree.ElementTree import Element, SubElement, Comment, tostring, ElementTree
from xml.dom import minidom
from progress.bar import Bar
import xml.etree.ElementTree as ElemTree
import silaba
import AdicionaFonetica as AF

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

tree = ElemTree.parse('bancoPalavras.xml')
root = tree.getroot()

for child in root:
    aPentear = str(child.attrib)
    aPentear = aPentear[13:]
    palavra = aPentear[:2]
    print(palavra)
    silabas = silaba.separaSilabas(palavra)
    tonica = -1
    while tonica != 1 and tonica != 2 and tonica != 3:
        print("Insira qual a sílaba tônica da palavra \"" + palavra + "\"\n 1 - Oxítona\t2 - Paroxítona\t3 - Proparoxítona")
        tonica = input('Sílaba tônica:')
        if tonica != '1' and tonica != '2' and tonica != '3':
            print("Valor inválido. Por favor, tente novamente.")
        else:
            tonica = int(tonica)

    palavraObjeto = AF.Palavra(palavra, len(silabas), silabas, tonica)
    print(palavraObjeto.escrita)
    i = 0
    somAnterior = 0
    somTotal = []
    for indice, letra in enumerate(palavraObjeto.escrita):
        somAnterior = AF.determinaFonema(palavraObjeto,indice, somAnterior)
            
        somTotal.append(somAnterior)
    
    print("Palavra escrita:" + palavraObjeto.escrita)
    print("Palavra falada", end=": ")
    for indice,som in enumerate(somTotal):
        if palavraObjeto.estaNaTonica(indice):
                print(AF.maiusculariza(AF.escritaSonora[som]), end = "")
        else:
            print(escritaSonora[som])
    