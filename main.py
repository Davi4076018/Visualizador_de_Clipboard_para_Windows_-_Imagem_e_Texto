from tkinter import *
import tkinter as tk
from tkinter import ttk
import pyperclip
import os
import inspect
import re
from PIL import ImageTk, ImageGrab, Image


def LoopClip():
    colar = pyperclip.paste()
    HistClip.config(text=colar)
    if(len(colar) > 500):
        Texto1.grid_forget()
    else:
        Texto1.grid(row = 2, column=1, sticky = 'S', pady = 50)
    if colar == "":
        try:
            temp_path = pathclip  # O caminho do arquivo temporario
            im = ImageGrab.grabclipboard()  # Atribui a variavel a imagem no Clipboard ***********
            im.thumbnail((250, 200)) # Muda a Resolução da Imagem mantendo a proporção
            im.save(temp_path)  # Salva a imagem no arquivo temporario
            load_for_label = ImageTk.PhotoImage(file=temp_path)  # A imagem é carregada para ser colocada
            imagem.config(image=load_for_label)  # Atribuindo a imagem no label
            imagem.image = load_for_label  # A imagem é salva como referencia na memoria
        except:
            temp_path = pathclip  # O caminho do arquivo temporario
            im = ImageGrab.grabclipboard()  # Atribui a variavel a imagem no Clipboard
    else:
        try:
            temp_path = pathwin  # O caminho do arquivo temporario
            im = Image.open(Pastadarq) # A imagem é aberta pra o seu uso
            im.thumbnail((250, 250))  # Muda a Resolução da Imagem mantendo a proporção
            im.save(temp_path)  # Salva a imagem no arquivo temporario
            load_for_label = ImageTk.PhotoImage(file=temp_path)  # A imagem é carregada para ser colocada
            imagem.config(image=load_for_label)  # Atribuindo a imagem no label
            imagem.image = load_for_label  # A imagem é salva como referencia na memoria
        except:
            temp_path = pathwin  # O caminho do arquivo temporario
            im = Image.open(Pastadarq) # A imagem é aberta pra o seu uso
    tab1.after(1000, LoopClip)  # A função chama ela mesma após 1 segundo ou 1000 ms


# criação da janela
sist=tk.Tk()

# titulo da janela
sist.title('Visualizador de Clipboard - Trabalho de SO II')

#busca e salva o diretorio atual
filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(filename))
Pastadarq = path + '\windows.png'
Pastadarqe = Pastadarq
Pastadarq = re.sub(r'\\', '/', Pastadarq)
path = re.sub(r'\\', r"\\\\" , path)
pathclip = path + '\\\\ClipImage.png'
pathwin =  path + '\\\\windows.png'


# tamanho da janela

sist.resizable(False, False)
sist.geometry("500x400")



#criação dos tabs

tabControl = ttk.Notebook(sist)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

# cor do background
sist['bg'] = "#00a2ed"

tabControl.add(tab1, text='Clipboard')
#tabControl.add(tab2, text='Tab 2')
tabControl.pack(expand=1, fill="both")

# Cor e estilo dos tabs
style = ttk.Style()

style.theme_create('Meutema', settings={
    ".": {
        "configure": {
            "background": "#00a2ed",  # cor dentro dos tabs
        }
    },
    "TNotebook": {
        "configure": {
            "background": "#0293dc",  # Cor da margem
            "tabmargins": [0, 0, 0, 0],  # margins: left, top, right, separator
        }
    },
    "TNotebook.Tab": {
        "configure": {
            "background": 'White',  # Cor do tab não selecionado
            "padding": [5, 1],
            # espaço do texto as extremidades do tab
        },
        "map": {
            "background": [("selected", "#00a2ed")],  # Cor do tab selecionado
            "expand": [("selected", [2, 0, 2, 2])]  # Margens do texto
        }
    }
})

style.theme_use('Meutema')

PHistClip = Label(tab1,
               text = ("Clipboard do Sistema:"),
               bg = "#00a2ed",
               fg = "black",
               bd = 2,
               relief = "groove",
               width = 71)


HistClip = Label(tab1,
               text = (" "),
               bg = "White",
               fg = "Black",
               bd = 2,
               relief = "solid",
               width = 35,
               height = 25,
               anchor = NW,
               justify = LEFT,
               wraplength=250)

ImgClip = Label(tab1,
               text = (" "),
               bg = "#00a2ed",
               fg = "#00a2ed",
               width = 35,
               height = 25,
               anchor = NW,
               justify = LEFT)



#imagem salva
img = Image.open(Pastadarq)
img.thumbnail((250, 250))
tkimage = ImageTk.PhotoImage(img)


Texto1 = Label(tab1,
               text = ("TEXTO"),
               bg = "White",
               fg = "#e6e6e6")

Texto1.config(font=("IMPACT", 30))

Texto2 = Label(tab1,
               text = ("IMAGEM"),
               bg = "#00a2ed",
               fg = "White")

Texto2.config(font=("IMPACT", 30))

LoopClip()

imagem = Label(tab1,
               image=tkimage,
               bg = "#00a2ed",
               justify = CENTER)

#Organização do Layout por Grid

ImgClip.grid(row = 2, column=2, sticky = 'w')
imagem.grid(row = 2, column=2, sticky = 'N', pady = 30)
PHistClip.grid(row = 1, column=1, sticky = 'w', columnspan = 2)
HistClip.grid(row = 2, column=1, sticky = 'w')
Texto2.grid(row = 2, column=2, sticky = 'S', pady = 50)

#looping da janela
sist.mainloop()