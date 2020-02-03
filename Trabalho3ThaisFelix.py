# Eu nao consegui implementar corretamente as funcoes alugar e reservar carros,
# Por que nao consegui fazer a parte de alugar um carro no dia escolhido, e antes verificar se vai chocar com outro aluguel
# A parte do atraso de dias tambem nao consegui fazer
# No caso, o meu programa faz o aluguel na hora, se voce for alugar um carro, ele ja fica alugado naquele momento

from datetime import datetime # para pegar a data atual da maquina

class main(object):
    veiculos = [] # lista que guarda todos os veiculos alugados
    veiculos_alugados = [] # lista que guarda todos os alugueis
    contador_de_veiculos = 0
    contador_de_veiculos_alugados = 0
    contador_de_atrasos = 0


    agr = datetime.now() # para pegar a data atual
    dia = agr.day
    mes = agr.month
    ano = agr.year

    opcao = 'a' # variavel que guarda a opcao que o usuario escolheu
    while(opcao != 'g'): # enquanto o usuario nao escolher "Sair", fica no looping
        print("*"*55)
        data_atual = str(dia) + "/" + str(mes) + "/" + str(ano) # formata a data
        print("Data atual: {}".format(data_atual))

        print("Quantidade de veiculos cadastrados: {}".format(len(veiculos)))
        print("Quantidade de veiculos alugados: {}".format(len(veiculos_alugados)))
        print("Quantidade de atrasos: {}".format(contador_de_atrasos))
        print("")
        print("Escolha uma das seguintes opcoes:(a,b,c,d,e,f,g)")
        print("a - Consultar veiculos")         #ok
        print("b - Adicionar veiculos")         #ok
        print("c - Alugar/Reservar veiculos")
        print("d - Devolver/Liberar veiculos")
        print("e - Excluir veiculos")           #ok
        print("f - Avancar data atual")         #ok
        print("g - Sair")                       #ok
        opcao = input("-> ")
        print("")

        # consulta
        if (opcao == 'a'):
            print ("***********CONSULTA***********")
            if len(veiculos) == 0: # verifica se ja tem carros na lista
                print("Sem Veiculos Cadastrados")
            else:
                for x in range(0, len(veiculos)):
                    # se tiver ele exibe formatado
                    print("Codigo: ",veiculos[x][0])
                    print("Modelo: ", veiculos[x][1])
                    print("Status: ", veiculos[x][5])
                    
                    print("")

                mop = input("Mais detalhes? (s/n)")
                if (mop == "s"):
                    for x in range(0, len(veiculos)):
                        print("Codigo: ",veiculos[x][0])
                        print("Modelo: ", veiculos[x][1])
                        print("Status: ", veiculos[x][5])
                        print("Marca: ", veiculos[x][2])
                        print("Ano: ", veiculos[x][3])
                        print("Valor: ", veiculos[x][4])
                        
                        print("")

        # adicionar
        elif (opcao == 'b'):
            print ("***********ADICIONAR***********")
            modelo = input("Digite o modelo: ")
            marca = input("Digite a marca: ")
            ano = int(input("Digite o ano do carro: "))
            vd = float(input("Informe o valor: "))
            status = 'Disponivel' # todos os veiculos que sao cadastrados ja sao disponiveis
            contador_de_veiculos = contador_de_veiculos + 1
            veiculos.append([contador_de_veiculos, modelo, marca, ano, vd, status]) # adiciona na lista
            print("Veiculo adicionado com sucesso")

        # alugar/revervar
        elif (opcao == 'c'):
            print ("***********ALUGAR/RESERVAR VEICULO***********")
            codc_aluguel = int(input("Digite o cod do carro que deseja alugar: "))
            dia_aluguel = int(input("Digite o dia que deseja alugar: "))
            mes_aluguel = int(input("Digite o mes que deseja alugar: "))
            ano_aluguel = int(input("Digite o ano que deseja alugar: "))
            quant_dias = int(input("Digite a quantidade de dias que deseja alugar: "))

            aux = False  # apenas para exibir a mensagem de "Erro"
            cont = False # pra saber se achou algum problema com o aluguel nesse dia
            v = 0
            for x in range(0, len(veiculos)):
                if codc_aluguel == veiculos[x][0]:
                    aux = True
                    if(veiculos[x][5] == "Disponivel"):
                        v = x
                        cont = True # para "burlar" o sistema e sempre da certo
                        break

                        # na verdade essa parte deveria ser assim
                        # testar se pode alugar nesse dia e com a quant de dias
                        # se poder ele continua e testa os proximos
                            #  cont = True # dizendo que deu certo pode add, so falta testar outros casos
                            #  continue
                        # se nao poder
                            #  print("Nao pode Alugar nesses dias")
                            #  cont = False #  dizendo que nao deu certo
                            #  break
                    else:
                        print("Veiculo ja alugado")
                    

            if aux == False:
                print("Codigo nao encontrado")
            if cont == True:
                locatorio = input("Digite seu nome: ")
                contador_de_veiculos_alugados = contador_de_veiculos_alugados + 1
                veiculos_alugados.append([contador_de_veiculos_alugados, codc_aluguel, locatorio, quant_dias, dia_aluguel, mes_aluguel, ano_aluguel])          
                print ("Veiculo alugado com sucesso")
                valor_f_a = quant_dias * veiculos[v][4]
                print ("O valor final do aluguel eh de {}".format(valor_f_a))
                veiculos[v][5] = "Alugado" # agora o veiculo esta alugado

        # devolver/liberar
        elif (opcao == 'd'):
            print ("***********DELVOLVER/LIBERAR VEICULO ALUGADO***********")
            if len(veiculos_alugados) == 0:
                print("Sem Veiculos Alugados Para Liberar")
            else:
                for x in range(0, len(veiculos_alugados)):
                    print("Codigo do aluguel: ", veiculos_alugados[x][0])
                    print("Codigo do carro: ", veiculos_alugados[x][1])
                    print("Nome locatorio: ", veiculos_alugados[x][2])
                    print("")

                qual_excluir = int(input("Digite o codigo do aluguel que voce deseja liberar: "))
                cont = False
                for x in range(0, len(veiculos_alugados)):
                    if qual_excluir == veiculos[x][0]:
                        del(veiculos_alugados[x])
                        print("Excluido com sucesso")
                        veiculos[x][5] = "Disponivel"  # volta a ser disponivel
                        cont = True
                        break
                if cont == False:
                    print("Codigo nao encontrado")

        #excluir
        elif (opcao == 'e'):
            print ("***********EXCLUIR VEICULO***********")
            if len(veiculos) == 0: # testa se tem veiculos cadatrados
                print("Sem Veiculos Cadastrados Para Excluir")
            else:
                qual_excluir = int(input("Digite o codigo do carro que voce deseja excluir: "))
                cont = False # variavel auxiliar para so pra mostrar se a mensagem "Cod n encontrado" caso nao ache o veiculo
                for x in range(0, len(veiculos)):
                    if qual_excluir == veiculos[x][0]: # procura o cod
                        cont = True
                        if (veiculos[x][5] == "Disponivel"): # so apaga se nao tiver alugado
                            del(veiculos[x]) # apaga
                            print("Excluido com sucesso")
                        else:
                            print ("Veiculo Alugado, nao pode excluir")
                        break # ja sai do for se der certo
                    
                if cont == False:
                    print("Codigo nao encontrado")

        # avancar dia
        elif (opcao == 'f'):
            print ("***********AVANCAR DIA***********")
            if dia == 31 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
                # se for dia 31 desses meses, o dia tem q ir pra 1
                dia = 1
                if mes == 12:
                    # mas se o dia for 31 de dezembro, o dia e o mes vai pra 1, e o ano avanca 1
                    mes = 1
                    ano = ano + 1
                else:
                    # pro outros casos que nao sao fim do ano
                    mes = mes + 1
            elif dia == 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
                # se for dia 30 desses meses, o dia tem q ir pra 1
                dia = 1
                mes = mes + 1
            elif dia == 28 and mes == 2:
                # para o caso de fevereiro
                dia = 1
                mes = mes + 1
            else:
                # e para os demais dias do ano
                dia = dia + 1
            print("Data atualizada")
            
        # sair
        elif (opcao == 'g'):
            print("Fim do Programa")
            
        # outro caso
        else:
            print("Opcao incorreta")

        print("")
        print("")
        print("")
