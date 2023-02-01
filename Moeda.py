import requests
from tkinter import *



def pegar_cotacoes():

    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

    requisao_dic = requisicao.json()

    cotacao_dolar = requisao_dic['USDBRL']['bid']

    print(cotacao_dolar)

pegar_cotacoes()

#interface grifica

janela = Tk()

janela.title('Casa da Moeda')
texto_inicio = Label(janela, text='Bem-Vindo ao cotador de moedas.Clique no botão para ver.')
texto_inicio.grid(column=0, row=0)

botao = Button(janela, text='Buscar Cotação', command=pegar_cotacoes)
botao.grid(column=0, row=1)






janela.mainloop()