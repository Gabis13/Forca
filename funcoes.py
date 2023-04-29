import os, time, random



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

def RandomWord ():
    arquivo = open("bd.forca", "r")
    dados = arquivo.readlines()
    while True:
        aleatorio = random.randint(0, len(dados))
        try:
            if aleatorio % 2 != 1:
                    palavra = dados[aleatorio]
            else: 
                palavra = dados[0]
        except:
            palavra = dados[0]
        break
    return palavra