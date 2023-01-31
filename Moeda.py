import requests

def pegar_cotacoes():

    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

    requisao_dic = requisicao.json()

    cotacao_dolar = requisao_dic['USDBRL']['bid']

    print(cotacao_dolar)

pegar_cotacoes()
