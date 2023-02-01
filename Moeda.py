import requests
from tkinter import *



def pegar_cotacoes():

    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

    requisao_dic = requisicao.json()

    cotacao_dolar = requisao_dic['USDBRL']['bid']

    texto = f'Dolar:$[{cotacao_dolar}]'

    texto_cotacao["text"] = texto


#interface grifica

janela = Tk()
janela.geometry('380x200')


janela.title('Casa da Moeda')
texto_inicio = Label(janela, text='Bem-Vindo ao cotador de moedas.Clique no botão para ver.')
texto_inicio.grid(column=0, row=0, padx=25, pady=15)

botao = Button(janela, text='Buscar Cotação', command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=25, pady=15)

texto_cotacao = Label(janela, text="")
texto_cotacao.grid(column=0, row=3, padx=25,pady=10)






janela.mainloop()