# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/   

from tkinter import *
import parser
import math

LARGE_FONT= ("Verdana", 12)

pos=0


class main_calculator(Tk):

    def __init__(self, *args, **kwargs):
        
        Tk.__init__(self, *args, **kwargs)

        self.title('Calculadora do Trindade')
        self.geometry('300x230') 

        # Criação do Menu tipo cascata
        topmenu = Menu(self)
        self.config(menu=topmenu)
        submenu = Menu(topmenu)
        topmenu.add_cascade(label='Options',menu=submenu)
        submenu.add_command(label='Cientific Calculator',command = lambda: clique())
        submenu.add_command(label='Standard Calculator',command = lambda: clique())
        submenu.add_separator()
        submenu.add_command(label='Exit',command = self.quit)

        container = Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (basic_calc, cientific_calc):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(basic_calc)
        
        # Função genérica de clique
        def clique():
            print('vc clicou')

    # Insere numeros no display
    def insert_num(self, display, invisible_display,num):    

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
    def clear_display(self,display):

        display.delete(0,END)
        display.insert(0,0)
        global pos
        pos=0

    def calculate(self, display, invisible_display):

        result_string = display.get()
        invisible_result = invisible_display.get()
        print(invisible_result)
        a = parser.expr(result_string).compile()
        result = eval(a)
        display.delete(0,END)
        display.insert(0,result)
        global pos
        pos=0

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

            
class basic_calc(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        titleframe = Frame(self)
        titleframe.pack(side=TOP,fill=BOTH)
        titlelabel1 = Label(titleframe,text='Calculadora do Trindade',
            bg='Yellow',fg='Red',relief=SUNKEN).pack(fill=BOTH,pady=10,ipady=10)

        displayframe = Frame(self)
        displayframe.pack(side=TOP,fill=X,pady=10)
        display = Entry(displayframe)
        invisible_display = Entry(displayframe)
        display.pack(fill=X,padx=20)
        display.insert(0,0)

        # Criaçao dos botoes numéricos
        buttonsframe1 = Frame(self)
        buttonsframe1.pack(side=LEFT,expand=1,fill=BOTH,anchor=W)
        button1 = Button(buttonsframe1,text="1",command = lambda: controller.insert_num(display,invisible_display,1)).grid(row=2,column=0,ipadx=5)
        button3 = Button(buttonsframe1,text="3",command = lambda: controller.insert_num(display,invisible_display,3)).grid(row=2,column=2,ipadx=5)
        button2 = Button(buttonsframe1,text="2",command = lambda: controller.insert_num(display,invisible_display,2)).grid(row=2,column=1,ipadx=5)
        button4 = Button(buttonsframe1,text="4",command = lambda: controller.insert_num(display,invisible_display,4)).grid(row=3,column=0,ipadx=5)
        button5 = Button(buttonsframe1,text="5",command = lambda: controller.insert_num(display,invisible_display,5)).grid(row=3,column=1,ipadx=5)
        button6 = Button(buttonsframe1,text="6",command = lambda: controller.insert_num(display,invisible_display,6)).grid(row=3,column=2,ipadx=5)
        button7 = Button(buttonsframe1,text="7",command = lambda: controller.insert_num(display,invisible_display,7)).grid(row=4,column=0,ipadx=5)
        button8 = Button(buttonsframe1,text="8",command = lambda: controller.insert_num(display,invisible_display,8)).grid(row=4,column=1,ipadx=5)
        button9 = Button(buttonsframe1,text="9",command = lambda: controller.insert_num(display,invisible_display,9)).grid(row=4,column=2,ipadx=5)
        button0 = Button(buttonsframe1,text="0",command = lambda: controller.insert_num(display,invisible_display,0)).grid(row=5,column=0,ipadx=5)
        buttonDOT = Button(buttonsframe1,text=".",command = lambda: controller.insert_num(display,invisible_display,'.')).grid(row=5,column=1,ipadx=8)
        buttonAC = Button(buttonsframe1,text="AC",command = lambda: controller.clear_display(display)).grid(row=5,column=2,ipadx=1)

        # Criação dos Botões com operações matemáticas e utilitarios
        buttonsframe2 = Frame(self)
        buttonsframe2.pack(side=RIGHT,expand=1,fill=BOTH,anchor=E,padx=8)
        buttonADI = Button(buttonsframe2,text="+",command = lambda: controller.insert_num(display,invisible_display,'+')).grid(row=2,column=0,ipadx=2,padx=3,sticky=W+E)
        buttonSUB = Button(buttonsframe2,text="-",command = lambda: controller.insert_num(display,invisible_display,'-')).grid(row=3,column=0,ipadx=2,padx=3,sticky=W+E)
        buttonDIV = Button(buttonsframe2,text="÷",command = lambda: controller.insert_num(display,invisible_display,'/')).grid(row=4,column=0,ipadx=2,padx=3,sticky=W+E)
        buttonMUL = Button(buttonsframe2,text="x",command = lambda: controller.insert_num(display,invisible_display,'*')).grid(row=5,column=0,ipadx=2,padx=3,sticky=W+E)
        buttonEQU = Button(buttonsframe2,text="=",command = lambda: controller.calculate(display,invisible_display)).grid(row=2,column=1,ipadx=2,padx=3,sticky=W+E)
        buttonPAR_O= Button(buttonsframe2,text="(",command = lambda:controller.insert_num(display,invisible_display,'(')).grid(row=3,column=1,ipadx=2,padx=3,sticky=W+E)
        buttonPAR_C= Button(buttonsframe2,text=")",command = lambda:controller.insert_num(display,invisible_display,')')).grid(row=4,column=1,ipadx=2,padx=3,sticky=W+E)
        buttonPERC = Button(buttonsframe2,text="√",command = lambda:controller.insert_num(display,invisible_display,'**(1/2)')).grid(row=5,column=1,ipadx=2,padx=3,sticky=W+E)
        button = Button(self, text="Go to Cientific Calculator",command=lambda: controller.show_frame(cientific_calc))
        button.pack()

class cientific_calc(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Cientific Calculator", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1 = Button(self, text="go to Calculator",command=lambda: controller.show_frame(basic_calc))
        button1.pack()

app = main_calculator()
app.mainloop()