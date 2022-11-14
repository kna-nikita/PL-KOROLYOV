from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter.ttk import Radiobutton
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Menu
from tkinter import scrolledtext

window = Tk()
window.title("Королёв_Никита_УБ-23")
window.geometry('500x200')

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control) 
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text = 'Калькулятор')
tab_control.add(tab2, text = 'Выбор ответа')
tab_control.add(tab3, text = 'Работа с текстом')
tab_control.pack(expand = 1, fill = 'both')

def click3():
    txt.delete('1.0', END)
    q = filedialog.askopenfilename(filetypes = (("Text files", "*.txt"),("All files", "*.*")))
    file = open(q, 'r')
    lines = file.readlines()
    row = len(lines)
    for i in range(row):
        txt.insert(INSERT, lines[i]) 

menu = Menu(tab3)
new_item = Menu(menu)
menu.add_cascade(label = 'Файл', menu = new_item)
new_item.add_command(label = 'Загрузить', command = click3)
new_item.add_separator() 
window.config(menu = menu) 


number1 = Entry(tab1, width = 5)                 # Первая страница
number1.grid(column= 0, row = 0)
number1.insert(0, '0')

number2 = Entry(tab1, width = 5)
number2.grid(column= 2, row = 0)
number2.insert(0, '1')

def click1():
    a = number1.get()
    b = number2.get()
    c = combo.get()
    r = 0
    if c == '+':
        r =  int(a) + int(b)
    elif c == '-':
        r = int(a) - int(b)
    elif c == '*':
        r = int(a) * int(b)
    elif c == '/':
        r = int(a) / int(b)
    lbl1['text'] = r
 
btn1 = Button(tab1, text = '=', command = click1)
btn1.grid(column = 3, row = 0)

combo = Combobox(tab1)
combo['values'] = ('+', '-', '*', '/')
combo.grid(column = 1, row = 0)
combo.current(0)

lbl1 = Label(tab1, text = '')
lbl1.grid(column = 4, row = 0) 


def click2():                                                                                       # Вторая страница
    messagebox.showinfo('Результат', 'Вы выбрали ' + str(selected.get()) + ' вариант ответа')                                                                         # Вторая страница    

lbl2 = Label(tab2, text = 'Выберите вариант ответа:')         
lbl2.grid(column = 0, row = 0)
selected = StringVar()
rad1 = Radiobutton(tab2, text = 'Первый', value = 'первый', variable = selected)
rad2 = Radiobutton(tab2, text = 'Второй', value = 'второй', variable = selected)
rad3 = Radiobutton(tab2, text = 'Третий', value = 'третий', variable = selected)
rad1.grid(column = 0, row = 1)
rad2.grid(column = 0, row = 2)
rad3.grid(column = 0, row = 3)
btn2 = Button(tab2, text = 'Продолжить', command = click2)
btn2.grid(column = 0, row = 4)


txt = scrolledtext.ScrolledText(tab3, width = 50, height = 50)                      # Третья страница
txt.grid(column =  0, row = 0)


window.mainloop() 