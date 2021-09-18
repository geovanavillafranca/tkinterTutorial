from tkinter import *
from tkinter import ttk
from random import randint


def sortear():
    sort = randint(0, 10)
    num_entry = int(entry1.get())
    if num_entry == sort:
        resultado.config(text="Você acertou parabéns!!")
    else:
        resultado.config(text=f"Você errou... O número era {sort}")


root = Tk(className="Adivinhação")

root.geometry("300x150")

Label(root, text="Digite um número entre 0 a 10").pack()

entry1 = Entry(root)
entry1.pack()

botao = Button(root, text="SORTEAR", command=sortear).pack()

resultado = Label(root, text="Resultado")
resultado.pack()

root.mainloop()

'''

root = Tk(className = "button_click_label")
root.geometry("200x200")

# message = StringVar()
# message.set('hi')

l1 = Label(root, text="hi")
l1.pack()

def press():
    l1.config(text="hello")

b1 = Button(root, text = "clickhere", command = press).pack()

root.mainloop()'''
