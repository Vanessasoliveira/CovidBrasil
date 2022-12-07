import pandas as pd
import openpyxl

### convertendo os dados de csv para xlsx para facilitar a manipulação dos dados, pois com o f csv constava apenas 
###uma coluna, o que dificultou o trabalho com os dados
dadosCovidCSV = pd.read_csv('cases-brazil-total.csv')
estadosCovid = pd.ExcelWriter('cases-brazil-total.xlsx')
dadosCovidCSV.to_excel(estadosCovid, index= False)

estadosCovid.save()

dadosEstadosCovid = pd.read_excel('cases-brazil-total.xlsx')



###print(dadosCovid)
### convertendo os dados de csv para xlsx para facilitar a manipulação dos dados, pois com o formato csv constava apenas 
###uma coluna, o que dificultou o trabalho com os dados
cidadesCovidCSV = pd.read_csv('cases-brazil-cities.csv')
cidadesCovid = pd.ExcelWriter('cases-brazil-cities.xlsx')
cidadesCovidCSV.to_excel(cidadesCovid, index= False)

cidadesCovid.save()

dadosCidadesCovid = pd.read_excel('cases-brazil-cities.xlsx')


### dataset disponivel em: https://www.kaggle.com/datasets/wlcota/covid19-cases-in-brazil-at-city-level?resource=download&select=cases-brazil-states.csv

def carregarMenu():
    print('')
    print('Panorama sobre a situação da COVID-19 no Brasil')
    print('1 - exibir quantidade de casos e de mortos por estado')
    print('2 - Exibir estado com menor número de mortes')
    print('3 - Exibir estado com maior número de mortes')
    print('4 - Exibir o total de casos no país')
    print('5 - Exibir todos dados de covid por estado')
    print('6 - Exibir dados de covid por cidades')
    print('7- Exibir dados de Covid da cidade Araraquara')
    print('8- Exibir dados apenas de cidades do estado de SP')
    print('9- Exibe os dados da cidade, COM ACENTO, que você quiser seguindo o modelo Gramado/RS(1ª letra maiscula, com acento e /Sigla do estado)')
    print('10 - Exibir o tamanho da tabela de cidades')
    print('11 - Dados da cidade de São Carlos/SP')
    print('12 - Exibir dados das cidades de um estado. DIGITE A SIGLA EM MAISCULO EX: PE')
    print('13 - Sair')


opcao = -1

while opcao !=0:
    carregarMenu()
    print('')
    opcao = int(input('Digite a opcao: '))
    if opcao == 1:
        mortosEstados = pd.read_excel('cases-brazil-total.xlsx', usecols=['state', 'totalCases','deaths'])
        print(mortosEstados)
    elif opcao ==2:      
       print('O estado com menor número de mortos é:') 
       print(dadosEstadosCovid.min())
    elif opcao ==3:
        print('O estado com maior número de mortos é:') 
        ###Não usei a função máxima porque retorna o valor de casos do Brasil, pois na planilha, o total está no campo state
        print(dadosEstadosCovid.loc[26])
    elif opcao ==4:
        print('O total de casos no país é:')
        print(dadosEstadosCovid.loc[0])
    elif opcao ==5:
        print('Todos dados de covid por estado:')
        TesteEstadosCovid = pd.read_excel('cases-brazil-total.xlsx', usecols=['state','totalCases','deaths', 'vaccinated_third_per_100_inhabitants','date', 'newCases','newDeaths'])
        print('')
        print(TesteEstadosCovid)
    elif opcao ==6:
        print('Dados de covid por cidades:')
        TesteCidadesCovid = pd.read_excel('cases-brazil-cities.xlsx', usecols=['state','city','totalCases','deaths', 'date', 'newCases','newDeaths'])
        print('')
        print(TesteCidadesCovid)
    elif opcao ==7:
        araraquara = dadosCidadesCovid.loc[297]
        print('Dados de Araraquara:\n')
        print(araraquara)
    elif opcao ==8:
        print('Dados de cidades do estado de SP:\n')
        dadosCidadesSP = dadosCidadesCovid.loc[dadosCidadesCovid['state'] == 'SP', ['state','city','deaths','totalCases', 'date']]
        print('')
        print(dadosCidadesSP)
    elif opcao ==9:
        nomeCidade = input('Digite o nome da cidade seguindo o modelo de exemplo Dobrada/SP:')
        cidade = dadosCidadesCovid.loc[dadosCidadesCovid['city'] == nomeCidade, ['state', 'city', 'deaths', 'totalCases']]
        print('')
        print(cidade)
    elif opcao ==10:
        print('O tamanho da tabela de cidades é: (linhas, Colunas)')
        print(dadosCidadesCovid.shape)
    elif opcao ==11:
        saoCarlos = dadosCidadesCovid.loc[4770]
        print(' Dados de São Carlos')
        print(saoCarlos)
    elif opcao ==12:
        siglaEstado = input('Digite a sigla do estado:')
        estado = dadosCidadesCovid.loc[dadosCidadesCovid['state'] == siglaEstado, ['state', 'city', 'deaths', 'totalCases']]
        print('')
        print(estado)
    elif opcao ==13:
        exit()

        ###It was created as an assignment to my graduate course. First we had to choose a dataset on Kaggle, after that we needed analysing them using the pandas library.
