#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib
import urllib.request
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from datetime import date  
import shutil
data = date.today()
#import os
hdr = {'User-Agent': 'Mozilla/5.0'}
def fazer_sopa(url):
    #proxies = {'https': 'https://proxy.unicentro.br:8080'}
    #print("Using HTTP proxy %s" % proxies['https'])
    #urllib.urlopen("http://www.google.com", proxies=proxies)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    #pagina = urllib.request.urlopen(url)
    pagina = urlopen(req).read()
    dados = BeautifulSoup(pagina, "html.parser") #, headers=hdr)#, proxies=proxies)
    return dados
def baixar_img(url, nome):
    name = str(str(nome) + ".jpg")
    print("baixando: %s" % nome)
    try:
        res = requests.get(url, stream=True)
        with open(name, 'wb') as f:
            res.raw.decode_content = True
            shutil.copyfileobj(res.raw, f)
    except Exception as e:
        print(e)

conta = 0
#url = "https://www.ahnegao.com.br/2020/02/coletanea-de-imagens-aleatorias-da-semana-291.html"
url = str(input("URL do Site: "))
print("fazendo a sopa...")
soup = fazer_sopa(url)
print("sopa feita")
#print(soup)
procura = 'img'
termo = str(input("Qual é o termo das imagens? "))

lista = []
#print(soup.find_all("img"))
print("procurando...")
for img in soup.findAll(procura):
    #print("for")
    #print(type(img))
    #print(">>>>>> {}".format('img-' in img))
    if termo in img['src']:
        #print(img['src'])
        lista.append(img['src'])
        #print("procurando...")
    else:
        conta += 1
        #print(img)
        #print("não achei", conta)
            
print("Acabou, achei %s imagens" %len(lista))
conta = 1
#baixar_img("https://www.ahnegao.com.br/wp-content/uploads/2020/02/img-1-1.jpg", "teste")
for itens in lista:
    nomee = str(data.day) + "-" + str(data.month) + "-" + str(data.year) + "-" + str(conta)
    conta += 1
    print(itens)
    baixar_img(itens, nomee)
    #if conta == 3:
        #break
    #print(itens)
    #print(nomee)
#print(len(lista))
