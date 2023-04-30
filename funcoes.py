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
        if len(variavel)>=1:
            return variavel
        else:
            print("Valor incorreto!")


def Upper(string):
   retorno = ''
   for caractere in string:
      if caractere.islower():
         retorno += caractere.upper()
      else:
         retorno = caractere
   return retorno