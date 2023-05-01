from funcoes import limparTela, aguarde, mudarCor, lerString, Upper
from random import randint
limparTela()
print("Seja Bem-vindo ao Jogo da Forca! ")
aguarde(2)
while True:
    limparTela()
    gameover = True
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
        while gameover:
            limparTela()
            print("processando...")
            aguarde(2)
            arquivo = open("bd.forca", "r")
            dados = arquivo.readlines()
            if dados == []:
                print("nenhuma palavra encontrada no banco de dados, adicione para pode jogar")
                aguarde(3)
                break

            while True:
                aleatorio = randint(0, len(dados)-1)
                if aleatorio % 2 == 0:
                    palavra = dados[aleatorio]
                    break
                else:
                    aleatorio = aleatorio - 1
                    palavra = dados[aleatorio]
                    break
            
            tamanho = len(palavra)
            riscos = ("_"*int(tamanho-1))
            print(riscos)
            arquivo.close
            print("A palavra foi escolhida")
            aguarde(2)
            print("As dicas são: {}".format(dados[aleatorio+1]))
            word = []
            word2 = []
            for i in riscos:
                word.append(i)
            for i in palavra:
                word2.append(i)
            count = 5
            stop = True
            while word.count("_") != 0 and gameover:
                letra = Upper(lerString("digite uma letra: "))
                stop = True
                indice = -1
                while stop:
                    try:
                        indice = word2.index(letra)
                        word[indice] = letra
                        word2[indice] = "_"
                        if word.count("_") == 0:
                            print("parabens, voce ganhou o jogo")
                            aguarde(2)
                            gameover = False
                    except:
                        if indice == -1:
                            print("Não tem esta letra")
                            count = count - 1
                            print(*word, sep=" ")
                            print("vidas: ", count)
                            aguarde(1)
                            stop = False
                        if count == 0:
                                print("voce perdeu, tente novamente")
                                aguarde(2)
                                gameover = False
                        else:
                            print(*word, sep=" ")
                            print("vidas: ", count)
                            stop = False
    elif opcao == "3":
        print("Informe a Nova Palavra, e suas respectivas 3 dicas")
        palavra = Upper(lerString("Palavra: "))
        dica1 = Upper(lerString("Dica nº 1: "))
        dica2 = Upper(lerString("Dica nº 2: "))
        dica3 = Upper(lerString("Dica nº 3: "))
        try:
            arquivo = open("bd.forca", "a")
            # tem que organizar melhor para aparecer uma lista de forma correta
            arquivo.write("{}\n{} - {} - {} \n" .format(palavra, dica1, dica2, dica3))
            arquivo.close
            print("Palavra Adicionada com Sucesso! ")
            aguarde(2)
        except:
            arquivo = open("bd.forca", "w")
            arquivo.close

    elif opcao == "4":
        arquivo = open("bd.forca", "r")
        dados = arquivo.read()
        print(dados)
        arquivo.close
        aguarde(5)
    else:
        print("Opção Inválida!")
        input("press enter tot continue...")
        aguarde(2)
print("Volte Sempre!")
aguarde(2)
