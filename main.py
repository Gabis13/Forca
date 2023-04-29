from funcoes import limparTela, aguarde, mudarCor, lerString, RandomWord
import random

limparTela()
print("Seja Bem-vindo ao Jogo da Forca! ")
aguarde(1)

while True:
    limparTela()
    print("(0) Sair")
    print("(1) Mudar Cor do Layout")
    print("(2) Iniciar Jogo")
    print("(3) Para adicionar palavras e dicas")
    print("(4) Mostrar palavras e dicas")
    opcao = input()
    if opcao == "0":
        break
    elif opcao == "1":
        cor = int(input("Digite o número da cor desejada: "))
        mudarCor(cor)
        input("press enter to continue...")
        aguarde(2)

    elif opcao == "2":
        palavra = RandomWord()
        
        limparTela()
        print("processando...")    
        aguarde(2)
        print("A palavra foi escolhida")
        aguarde(2)
        tamanho = len(palavra)
        riscos = ("_"*int(tamanho-1))
        print(riscos)
        word = []
        word2 = []
        for i in riscos:
            word.append(i)

        while True:
            letra = input("digite uma letra: ")
            s = palavra.find(letra)
            if s == -1: 
                print("Não tem esta letra")
            else:
                word[s] = letra
                print(word)
                



    elif opcao == "3":
        print("Informe a Nova Palavra, e suas respectivas 3 dicas")
        palavra = lerString("Palavra: ")
        dica1 = lerString("Dica nº 1: ")
        dica2 = lerString("Dica nº 2: ")
        dica3 = lerString("Dica nº 3: ")
        try:
            arquivo = open("bd.forca","a")
            arquivo.write(palavra + "\n" + dica1+" "+dica2+ " "+ dica3+ "\n") #tem que organizar melhor para aparecer uma lista de forma correta
            arquivo.close
            print("Palavra Adicionada com Sucesso! ")
            aguarde(2)
        except:
            arquivo = open("bd.forca", "w")
            arquivo.close
    elif opcao == "4":
        arquivo = open("bd.forca","r")
        dados = arquivo.read()
        print(dados)
        #print("bd.forca","r")
        #input("press enter to continue...")
        arquivo.close
        aguarde(5)
    else:
        print("Opção Inválida!")
        input("press enter tot continue...")
        aguarde(2)
print("Volte Sempre!")
        
#(str(palavra) +"-"+ str(dica1)+ "-"+ str(dica2)+"-" + str(dica3)+"-"+ "\n")
#(palavra +"-"+ dica1+ "-"+ dica2+"-" + dica3+"-"+ "\n")