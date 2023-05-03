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
        if variavel.find(" ") >= 1:
            print("valor inserido incorretamente")
        elif len(variavel)>=1:
            return variavel


def Upper(string):
   retorno = ''
   for caractere in string:
      if caractere.islower():
         retorno += caractere.upper()
      else:
         retorno = caractere
   return retorno


def AdicionarBD (desafiante, desafiado, palavra, erros, dicas, resultado):
    try:
        arquivo = open("bd.relatorio", "a")
        dados = arquivo.write("\nDesafiante: {}\nDesafiado: {}\npalavra: {}\nErros: {}\nQuantidade de dicas: {}\nresultado: {}".format(desafiante, desafiado, palavra, erros, dicas, resultado))
        arquivo.close
    except:
        arquivo = open("bd.relatorio", "w")
        arquivo.close

def desenho(erros):
    if erros == 0:
        print()
        print("|----- ")
        print("|    | ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|      ")
        print()

    elif erros == 1:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|      ")
        print("|      ")
        print("|      ")
        print()

        
    elif erros == 2:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|    | ")
        print("|    |  ")
        print("|      ")
        print()

    elif erros == 3:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|    |\ ")
        print("|    |  ")
        print("|      ")
        print()

        
    elif erros == 4:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\ ")
        print("|    | ")
        print("|      ")
        print()


        
    elif erros == 5:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\ ")
        print("|    | ")
        print("|     \ ")
        print()

    elif erros == 6:
        print()
        print("------ ")
        print("|    | ")
        print("|    O ")
        print("|   /|\ ")
        print("|    | ")
        print("|   / \ ")
        print()