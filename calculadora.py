from tkinter import *

num1 = 0
operacao = ""

def inserir(numero):
    visor.insert(END, numero)

def soma():
    global operacao, num1
    try:
        num1 = float(visor.get())
    except ValueError:
        return
    operacao = "+"
    visor.delete(0, END)

def inserir_ponto():
    if "." in visor.get():
        return
    visor.insert(END, ".")

def menos():
    global operacao, num1
    try:
        num1 = float(visor.get())
    except ValueError:
        return
    operacao = "-"
    visor.delete(0, END)

def multiplicao():
    global operacao, num1
    try:
        num1 = float(visor.get())
    except ValueError:
        return
    operacao = "x"
    visor.delete(0, END)

def divicao():
    global operacao, num1
    try:
        num1 = float(visor.get())
    except ValueError:
        return
    operacao = "/"
    visor.delete(0, END)


def igual():
    numero2 = float(visor.get())
    if operacao == "+":
        resultado = numero2 + num1
    elif operacao == "-":
        resultado = num1 - numero2
    elif operacao == "x":
        resultado = numero2 * num1
    elif operacao == "/":
        resultado = num1 / numero2
    visor.delete(0, END)
    visor.insert(0, resultado)


def apaga():
    visor.delete(0, END)

def apaga_ultimo():
    texto = visor.get()
    visor.delete(0, END)
    visor.insert(0, texto[:-1])

janela = Tk()
janela.title("Calculadora")
janela.geometry("290x318")


posicoes = {"7": (1, 0), "8": (1, 1), "9": (1, 2),
            "4": (2, 0), "5": (2, 1), "6": (2, 2),
            "1": (3, 0), "2": (3, 1), "3": (3, 2),
            "0": (4, 0)}

for texto, (linha, coluna) in posicoes.items():
    Button(janela, text=texto, width = 4, command= lambda t=texto: inserir(t)).grid(row=linha, column =coluna, padx = 5, pady = 5)



frame_visor = Frame(janela, width=230, height=50, bg="#C0C0C0")
frame_visor.grid(row=0, column=0, columnspan=5)

visor = Entry(frame_visor, font="Arial, 19", justify="right")
visor.pack(fill=BOTH, expand=TRUE)

botaodel = Button(janela, text="⌫", width=4, command=apaga_ultimo)
botaodel.grid(row=1, column=3, padx=5, pady=5)

botaoC = Button(janela, text="C", width=4, command=apaga)
botaoC.grid(row=4, column=2, padx=5, pady=5)

botaoponto = Button(janela, text=".", width=4, command= inserir_ponto)
botaoponto.grid(row=4, column=1, padx=5, pady=5)

botaodiv = Button(janela, text="➗", width=4, command=divicao)
botaodiv.grid(row=2, column=3, padx=5, pady=5)

botaomult = Button(janela, text="✖", width=4, command=multiplicao)
botaomult.grid(row=3, column=3, padx=5, pady=5)

botaomais = Button(janela, text="➕", width=4, command=soma)
botaomais.grid(row=5, column=3, padx=5, pady=5)

botaomenos = Button(janela, text="➖", width=4, command=menos)
botaomenos.grid(row=4, column=3, padx=5, pady=5)

botaoigual = Button(janela, text="🟰", bg="#0000FF", width=4, command=igual)
botaoigual.grid(row=6, column=3, padx=5, pady=5)


janela.mainloop()
