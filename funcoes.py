import os
import time

def limparTela():
    os.system("cls")

def aguarde(segundos = 1):
    time.sleep(segundos)

def mudarCor(codeCor):
    os.system("color " +str(codeCor))

def lerString(mensagem):
    while True:
        variavel = input(mensagem)
        if len(variavel)>1:
            return variavel
        else:
            print("Valor incorreto!")
