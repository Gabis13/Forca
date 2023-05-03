#Arthur Dezingrini - 1135044   Gabriel viecili - 1135192
from funcoes import limparTela, aguarde, mudarCor, lerString, Upper, AdicionarBD, desenho
from random import randint
limparTela()
print("Seja Bem-vindo ao Jogo da Forca! ")
aguarde(2)

desafiante = input("Informe o nome do desafiante: ")
desafiado = input("informe o nome do desafiado: ")

contador = 0
while True:
    limparTela()
    gameover = True
    print("(0) Sair")
    print("(1) Mudar Cor do Layout")
    print("(2) Iniciar Jogo")
    print("(3) Para adicionar palavras e dicas")
    print("(4) Mostrar palavras e dicas")
    print("(5) Resetar palavras e dicas")
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
                    palavra = dados[aleatorio].split()[1]
                    break
                else:
                    aleatorio = aleatorio - 1
                    palavra = dados[aleatorio].split()[1]
                    break
            tamanho = len(palavra)
            riscos = ("_"*int(tamanho))
            print("A palavra foi escolhida")
            arquivo.close
            count = 0
            desenho(count)
            print(riscos)
            word = []
            word2 = []
            for i in riscos:
                word.append(i)
            for i in palavra:
                word2.append(i)
            stop = True
            while gameover:
                escolha = input("(1)jogar\n(2)dica ")
                if escolha == "1":
                        while word.count("_") != 0 and gameover and escolha == "1":
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
                                        resultado = "O desafiado ganhou"
                                except:
                                    if indice == -1:
                                        print("Não tem esta letra")
                                        count = count + 1
                                        print("Erros: ", count)
                                        stop = False
                                        escolha = "2"
                                        desenho(count)
                                    if count == 6:
                                        print("voce perdeu, tente novamente")
                                        aguarde(2)
                                        gameover = False
                                        escolha = '2'
                                        resultado = ("O desafiador ganhou")
                                    else:
                                        desenho(count)
                                        print(*word, sep=" ")
                                        print("vidas: ", count)
                                        stop = False
                                        escolha = '2'
                                        
                elif escolha == '2' and contador <= 3:
                    arquivo = open("bd.forca", "r")
                    dados = arquivo.readlines()
                    if contador == 0:
                        dicas = dados[aleatorio+1].split()[1]
                        contador = contador + 1
                        print(dicas)
                    elif contador == 1:
                        dicas = dados[aleatorio+1].split()[3]
                        contador = contador + 1
                        print(dicas)
                    elif contador == 2:
                        dicas = dados[aleatorio+1].split()[5]
                        contador = contador + 1
                        print(dicas)
                    else:
                        print("Não ha mais dicas")
                        aguarde(2)
        AdicionarBD(desafiante, desafiado, palavra, count, contador, resultado)
        print("\nDesafiante: {}\nDesafiado: {}\npalavra: {}\nErros: {}\nQuantidade de dicas: {}\nresultado: {}".format(desafiante, desafiado, palavra, count, dicas, resultado))
        
    elif opcao == "3":
        print("Informe a Nova Palavra, e suas respectivas 3 dicas")
        palavra = Upper(lerString("Palavra: "))
        dica1 = Upper(lerString("Dica nº 1: "))
        dica2 = Upper(lerString("Dica nº 2: "))
        dica3 = Upper(lerString("Dica nº 3: "))
        try:
            arquivo = open("bd.forca", "a")
            arquivo.write("Palavra: {}\nDicas: {} - {} - {} \n" .format(palavra, dica1, dica2, dica3))
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

    elif opcao == "5":
        arquivo = open("bd.forca", "w")
        arquivo.close
        print("Palavras e dicas restadas com sucesso")
        aguarde(2)
    else:
        print("Opção Inválida!")
        input("press enter tot continue...")
        aguarde(2)
print("Volte Sempre!")
aguarde(2)

