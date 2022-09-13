from logging import root
from pickletools import read_string1
from tkinter import *
from tkinter import ttk

class Calculadora:
    def __init__(self, master=None):
        self.fonte = ('calibri', '12')

        # cores
        self.cor1 = "#feffff"
        self.cor2 = "#38576b"  
        self.cor3 ="#ECEFF1"
        self.cor4='#FFAB40'

        self.fundo = "#3b3b3b"

        self.resultado = 0

        # Cria o container que conterá a tela
        self.display = Frame(master)
        self.display['pady'] = 10
        self.display.pack()

        # Cria a primeira fileira de botões
        self.linhaBotoes1 = Frame(master)
        self.linhaBotoes1.pack()

        # Cria a segunda fileira de botões
        self.linhaBotoes2 = Frame(master)
        self.linhaBotoes2.pack()

        # Cria terceira fileira de botões
        self.linhaBotoes3 = Frame(master)
        self.linhaBotoes3.pack()

        # Cria a quarta fileira de botões
        self.linhaBotoes4 = Frame(master)
        self.linhaBotoes4.pack()

        # Cria a quinta fileira de botões
        self.linhaBotoes5 = Frame(master)
        self.linhaBotoes5.pack()

        # Cria uma label para a tela
        self.tela = Label(self.display, text="", width=16, height=2, bg='#37474F', fg=self.cor1)
        self.tela['font'] = ('Ivy', '18')
        self.tela.pack()

        # BOTÕES

        # Botão de apagar
        self.botaoApagar = Button(self.linhaBotoes1)
        self.botaoApagar["text"] = 'C'
        self.botaoApagar["font"] = self.fonte
        self.botaoApagar["width"] = 8
        self.botaoApagar["height"] = 2
        self.botaoApagar["command"] = self.limparTela
        self.botaoApagar.pack(side=LEFT)

        # Botão de porcentagem
        self.botaoPorcentagem = Button(self.linhaBotoes1)
        self.botaoPorcentagem["text"] = "%"
        self.botaoPorcentagem["font"] = self.fonte
        self.botaoPorcentagem["width"] = 4
        self.botaoPorcentagem["height"] = 2
        self.botaoPorcentagem["command"] = lambda: self.inserirNum("%")
        self.botaoPorcentagem.pack(side=LEFT)

        # botão de divisão
        self.botaoDivisao = Button(self.linhaBotoes1)
        self.botaoDivisao["text"] = "/"
        self.botaoDivisao["font"] = self.fonte
        self.botaoDivisao["width"] = 4
        self.botaoDivisao["height"] = 2
        self.botaoDivisao["bg"] = self.cor4
        self.botaoDivisao["command"] = lambda: self.inserirNum("/")
        self.botaoDivisao.pack(side=LEFT)

        # botão 7
        self.botao7 = Button(self.linhaBotoes2)
        self.botao7["text"] = "7"
        self.botao7["font"] = self.fonte
        self.botao7["width"] = 2
        self.botao7["height"] = 2
        self.botao7["command"] = lambda: self.inserirNum("7")
        self.botao7.pack(side=LEFT)

        # botão 8
        self.botao8 = Button(self.linhaBotoes2)
        self.botao8["text"] = "8"
        self.botao8["font"] = self.fonte
        self.botao8["width"] = 3
        self.botao8["height"] = 2
        self.botao8["command"] = lambda: self.inserirNum("8")
        self.botao8.pack(side=LEFT)

        # botão 9
        self.botao9 = Button(self.linhaBotoes2)
        self.botao9["text"] = "9"
        self.botao9["font"] = self.fonte
        self.botao9["width"] = 4
        self.botao9["height"] = 2
        self.botao9["command"] = lambda: self.inserirNum("9")
        self.botao9.pack(side=LEFT)

        # botão de multiplicação
        self.botaoMult = Button(self.linhaBotoes2)
        self.botaoMult["text"] = "*"
        self.botaoMult["font"] = self.fonte
        self.botaoMult["width"] = 4
        self.botaoMult["height"] = 2
        self.botaoMult["bg"] = self.cor4
        self.botaoMult["command"] = lambda: self.inserirNum("*")
        self.botaoMult.pack(side=LEFT)

        # botão 4
        self.botao4 = Button(self.linhaBotoes3)
        self.botao4["text"] = "4"
        self.botao4["font"] = self.fonte
        self.botao4["width"] = 2
        self.botao4["height"] = 2
        self.botao4["command"] = lambda: self.inserirNum("4")
        self.botao4.pack(side=LEFT)
        
        # botão 5
        self.botao5 = Button(self.linhaBotoes3)
        self.botao5["text"] = "5"
        self.botao5["font"] = self.fonte
        self.botao5["width"] = 3
        self.botao5["height"] = 2
        self.botao5["command"] = lambda: self.inserirNum("5")
        self.botao5.pack(side=LEFT)

        # botão 6
        self.botao6 = Button(self.linhaBotoes3)
        self.botao6["text"] = "6"
        self.botao6["font"] = self.fonte
        self.botao6["width"] = 4
        self.botao6["height"] = 2
        self.botao6["command"] = lambda: self.inserirNum("6")
        self.botao6.pack(side=LEFT)

        # botão subtração
        self.botaoSub = Button(self.linhaBotoes3)
        self.botaoSub["text"] = "-"
        self.botaoSub["font"] = self.fonte
        self.botaoSub["width"] = 4
        self.botaoSub["height"] = 2
        self.botaoSub["bg"] = self.cor4
        self.botaoSub["command"] = lambda: self.inserirNum("-")
        self.botaoSub.pack(side=LEFT)

        # botão 1
        self.botao1 = Button(self.linhaBotoes4)
        self.botao1["text"] = "1"
        self.botao1["font"] = self.fonte
        self.botao1["width"] = 2
        self.botao1["height"] = 2
        self.botao1["command"] = lambda: self.inserirNum("1")
        self.botao1.pack(side=LEFT)

        # botão 2
        self.botao2 = Button(self.linhaBotoes4)
        self.botao2["text"] = "2"
        self.botao2["font"] = self.fonte
        self.botao2["width"] = 3
        self.botao2["height"] = 2
        self.botao2["command"] = lambda: self.inserirNum("2")
        self.botao2.pack(side=LEFT)

        # botão 3
        self.botao3 = Button(self.linhaBotoes4)
        self.botao3["text"] = "3"
        self.botao3["font"] = self.fonte
        self.botao3["width"] = 4
        self.botao3["height"] = 2
        self.botao3["command"] = lambda: self.inserirNum("3")
        self.botao3.pack(side=LEFT)

        # botão de soma
        self.botaoSoma = Button(self.linhaBotoes4)
        self.botaoSoma["text"] = "+"
        self.botaoSoma["font"] = self.fonte
        self.botaoSoma["width"] = 4
        self.botaoSoma["height"] = 2
        self.botaoSoma["bg"] = self.cor4
        self.botaoSoma["command"] = lambda: self.inserirNum("+")
        self.botaoSoma.pack(side=LEFT)

        # Botão 0
        self.botao0 = Button(self.linhaBotoes5)
        self.botao0["text"] = '0'
        self.botao0["font"] = self.fonte
        self.botao0["width"] = 8
        self.botao0["height"] = 2
        self.botao0["command"] = lambda: self.inserirNum("0")
        self.botao0.pack(side=LEFT)

        # Botão .
        self.botaoPonto = Button(self.linhaBotoes5)
        self.botaoPonto["text"] = "."
        self.botaoPonto["font"] = self.fonte
        self.botaoPonto["width"] = 4
        self.botaoPonto["height"] = 2
        self.botaoPonto["command"] = lambda: self.inserirNum(".")
        self.botaoPonto.pack(side=LEFT)

        # botão de resultado
        self.botaoResult = Button(self.linhaBotoes5)
        self.botaoResult["text"] = "="
        self.botaoResult["font"] = self.fonte
        self.botaoResult["width"] = 4
        self.botaoResult["height"] = 2
        self.botaoResult["bg"] = self.cor4
        self.botaoResult["command"] = lambda: self.result()
        self.botaoResult.pack(side=LEFT)

    def limparTela(self):
        self.tela["text"] = ""

    def inserirNum(self, caracter):
        # Add o ultimo caracter digitado a tela
        self.tela["text"] += caracter

    def result(self):
        # Calcula o resultado da expressão e a exibe no display
        self.resultado = eval(self.tela["text"])
        self.tela["text"] = str(self.resultado)

# Instaciamos a classe TK() que permite que os widgets sejam utilizados na aplicação
root = Tk()

# Passamos a variavel root como parãmetro do método construtor de Application()
Calculadora(root)

# Exibe a tela
root.mainloop()