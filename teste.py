from tkinter import *
import parser
import math



pos=0

# Função genérica de clique
def clique():
    print('vc clicou')

# Insere numeros no display
def insert_num(num):    
    global pos 
    if pos == 0:
        display.delete(0,END) 
    display.insert(pos,num)
    invisible_display.insert(pos,num)
    if num == '**(1/2)':
        pos+=6
    else:
        pos+=1

# Limpa o display ao clicar em 'AC'
def clear_display():
    display.delete(0,END)
    display.insert(0,0)
    global pos
    pos=0

def calculate():
    result_string = display.get()
    invisible_result = invisible_display.get()
    print(invisible_result)
    a = parser.expr(result_string).compile()
    result = eval(a)
    display.delete(0,END)
    display.insert(0,result)
    global pos
    pos=0

# Funções Lambdas com as operações mateméticas
adition = lambda x,y: x+y
substrac = lambda x,y: x-y
division = lambda x,y: x/y
multiply = lambda x,y: x*y

# Criação do Objeto, título da janela e suas dimensões
root = Tk()
root.title('Calculadora do Trindade')
root.geometry('300x230') 

# Criação do Menu tipo cascata
topmenu = Menu(root)
root.config(menu=topmenu)
submenu = Menu(topmenu)
topmenu.add_cascade(label='Options',menu=submenu)
submenu.add_command(label='Cientific Calculator',command = clique)
submenu.add_command(label='Standard Calculator',command = clique)
submenu.add_separator()
submenu.add_command(label='Exit',command = root.quit)

# Criação do Frame principal
mainframe = Frame(root)
mainframe.pack()

# Nome da calculadora, novamente
titleframe = Frame(mainframe)
titleframe.pack(side=TOP,fill=BOTH)
titlelabel1 = Label(titleframe,text='Calculadora do Trindade',bg='Yellow',fg='Red',relief=SUNKEN).pack(fill=BOTH,pady=10,ipady=10)

# Criação do Frame e display
displayframe = Frame(mainframe)
displayframe.pack(side=TOP,fill=X,pady=10)
display = Entry(displayframe)
invisible_display = Entry(displayframe)
display.pack(fill=X,padx=20)
display.insert(0,0)

# Criaçao dos botoes numéricos
buttonsframe1 = Frame(mainframe)
buttonsframe1.pack(side=LEFT,expand=1,fill=BOTH,anchor=W)
button1 = Button(buttonsframe1,text="1",command = lambda: insert_num(1)).grid(row=2,column=0,ipadx=5)
button2 = Button(buttonsframe1,text="2",command = lambda: insert_num(2)).grid(row=2,column=1,ipadx=5)
button3 = Button(buttonsframe1,text="3",command = lambda: insert_num(3)).grid(row=2,column=2,ipadx=5)
button4 = Button(buttonsframe1,text="4",command = lambda: insert_num(4)).grid(row=3,column=0,ipadx=5)
button5 = Button(buttonsframe1,text="5",command = lambda: insert_num(5)).grid(row=3,column=1,ipadx=5)
button6 = Button(buttonsframe1,text="6",command = lambda: insert_num(6)).grid(row=3,column=2,ipadx=5)
button7 = Button(buttonsframe1,text="7",command = lambda: insert_num(7)).grid(row=4,column=0,ipadx=5)
button8 = Button(buttonsframe1,text="8",command = lambda: insert_num(8)).grid(row=4,column=1,ipadx=5)
button9 = Button(buttonsframe1,text="9",command = lambda: insert_num(9)).grid(row=4,column=2,ipadx=5)
button0 = Button(buttonsframe1,text="0",command = lambda: insert_num(0)).grid(row=5,column=0,ipadx=5)
buttonDOT = Button(buttonsframe1,text=".",command = lambda: insert_num('.')).grid(row=5,column=1,ipadx=8)
buttonAC = Button(buttonsframe1,text="AC",command = lambda: clear_display()).grid(row=5,column=2,ipadx=1)

# Criação dos Botões com operações matemáticas e utilitarios
buttonsframe2 = Frame(mainframe)
buttonsframe2.pack(side=RIGHT,expand=1,fill=BOTH,anchor=E,padx=8)
buttonADI = Button(buttonsframe2,text="+",command = lambda:insert_num('+')).grid(row=2,column=0,ipadx=2,padx=3,sticky=W+E)
buttonSUB = Button(buttonsframe2,text="-",command = lambda: insert_num('-')).grid(row=3,column=0,ipadx=2,padx=3,sticky=W+E)
buttonDIV = Button(buttonsframe2,text="÷",command = lambda: insert_num('/')).grid(row=4,column=0,ipadx=2,padx=3,sticky=W+E)
buttonMUL = Button(buttonsframe2,text="x",command = lambda: insert_num('*')).grid(row=5,column=0,ipadx=2,padx=3,sticky=W+E)
buttonEQU = Button(buttonsframe2,text="=",command = lambda: calculate()).grid(row=2,column=1,ipadx=2,padx=3,sticky=W+E)
buttonPAR_O= Button(buttonsframe2,text="(",command = lambda: insert_num('(')).grid(row=3,column=1,ipadx=2,padx=3,sticky=W+E)
buttonPAR_C= Button(buttonsframe2,text=")",command = lambda: insert_num(')')).grid(row=4,column=1,ipadx=2,padx=3,sticky=W+E)
buttonPERC = Button(buttonsframe2,text="√",command = lambda: insert_num('**(1/2)')).grid(row=5,column=1,ipadx=2,padx=3,sticky=W+E)

root.mainloop()