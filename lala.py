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

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

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
            
class basic_calc(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        label = Label(self, text="Calculator", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button = Button(self, text="Visit Page 1",command=lambda: controller.show_frame(cientific_calc))
        button.pack()

class cientific_calc(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1 = Button(self, text="Back to Home",command=lambda: controller.show_frame(basic_calc))
        button1.pack()


app = main_calculator()
app.mainloop()