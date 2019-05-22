#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
    
nomearquivo = "exemplo.txt"  # ARQUIVO !!!!!!!!!!!!!!!!!!!!
## abre o arquivo##
arquivo = open(nomearquivo, 'r') 
    ## Cria as listas ##
Y = []
X = []
    ##Lê o arquivo ##
linha = arquivo.readline()
    ## Separa os itens do arquivos em 2 lista ##
while linha != '':
    separado = linha.split(',')
    Y.append(float(separado[1]))
    X.append(int(separado[0]))
    linha = arquivo.readline()

    ## Fecha o arquivo ## 
arquivo.close()


        ## Função para plotar um grafico de linha ##
def grafico_linha(x, y, legendax, legenday, titulo, escX, escfX, escY, escfY):
    fig, ax = plt.subplots()
    plt.ylim(escY, escfY)  # Intervalo do grafico em Y
    plt.xlim(escX, escfX)  # Intervalo do grafico em X
    ax.plot(x, y)          #plota o grafico 
    #define titulo e legendas ##
    ax.set(xlabel= legendax, ylabel=legenday, title=titulo)
    
    #Grade no grafico ##
    ax.grid(True)
    # Salva os arquivos em png e em PDF ##
    fig.savefig("exemplo.png")
    fig.savefig("exemplo.pdf")
    ## motra o grafico ##
    plt.show()
    
    
### Define a escala inicial e a final ##
escalaX_inicial = 0
escalaX_final = 10
escalaY_inicial = 0
escalaY_final = 20
## chama a função para plotar o grafico ##
grafico_linha(X, Y, 'legenda X', '', 'titulo', escalaX_inicial, escalaX_final, escalaY_inicial, escalaY_final)
   
    