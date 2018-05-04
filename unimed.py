#!/usr/local/bin/python
# -*- coding: utf-8 -*-


#
# Versão para Python 2 não funciona no Python 3
#

import os, sys
import tweepy
import re
import time
import random
from random import randint
from random import uniform
from random import random
from mechanize import Browser
from keys import keys

# Endereço a ser lido pelo mechanize ,onde esta localizado o formulário de consulta de autorização de serviços

end= ""



senha =raw_input ("Digite a senha de autorização que esta localizada na guia: ")
print("")
print("A senha digitada foi %s"%senha)
print("")

#Parte para receber a resposta por mensagem no Tweeter
#
print("Deseja enviar um tweeter? ")
print("")
tweetar = raw_input(" Digite Sim ou Nao \n")
if (tweetar == "sim" or tweetar == "Sim" or tweetar == "SIM"):
    userTweeter = raw_input("Qual o nome do usuário que deseja enviar, escreva @nomedousuário")
    mensagem = "0"

print("")

# Fim da interação ativa do usuário


#criação do objeto navegador = nav

nav = Browser()

# abre o site a fazer a consulta 
nav.open(end)

#cancela robots
nav.set_handle_robots(False)

# seleciona o formulário a ser lido no caso é o 1 pois o primeiro é de busca na página
# Por se tratar de um scrapp bem básico, não fizemos regex para buscar qual seria a posição adequada
# para o método select_form(nr=numero do formulário), deve se atentar que esse método inicia a contagem em zero

nav.select_form(nr=1)

# senha da guia da operadora
# Aqui também depende de como é o seu formulário no meu caso específico era uma string

nav['numAut'] =str(senha)

# envia a consulta
enviar = nav.submit()

# pega o resultado do envio
resultado = enviar.read()

# tratamento do resultado

if "Pendente" in resultado:
    mensagem = "Pendente"
## Sai do programa 
    sys.exit("Ainda Pendente")
else:
    mensagem = "Ok"

## Se a mensagem for OK envia um twitter para a conta

if mensagem =="Ok":


    ## Parte que envia o tweet com a resposta 

    CONSUMER_KEY = keys['consumer_key']
    CONSUMER_SECRET = keys['consumer_secret']
    ACCESS_TOKEN = keys['access_token']
    ACCESS_TOKEN_SECRET = keys['access_token_secret']

## chaves de autenticação tweeter

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

## lê o arquivo.txt onde estão os nomes de usuários 
## para mensagens diretas

    arq = open("tweeterUsers.txt","r")
    linha = arq.readlines()
    arq.close()

## Laço para enviar a msg para os usuários do arquivo tweeterUsers.txt

## Gera um valor aleatório entre 0 e 1  para a string valor, isso é necessário pois mensagens repetidas seguidas são 
## barradas pela api

    valor = str(uniform(0,1))

    for i in linha:
        i = i.rstrip()
        msg = i + "  " + mensagem + " :p" + valor
        s = api.update_status(msg)
        nap = randint(1,60)
        time.sleep(nap)
