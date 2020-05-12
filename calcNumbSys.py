from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import re
import ctypes
import About


def show_about():
      global root
      root = Tk()
      window = About(root)
      root.mainloop()


class Application:
    def __init__(self, master):
        self.master = master

        # window

        self.master.title("Системы счисления")

        #fixme who comented this from below?

        #myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
        #ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        self.master.iconbitmap('calculator_icon.ico')

        # menu

        Main_menu = Menu(self.master)
        self.master.config(menu=Main_menu)
        File_Menu = Menu(Main_menu, tearoff=False)
        Main_menu.add_cascade(label='File', menu=File_Menu)     
        Main_menu.add_cascade(label='About', command=show_about)
        Main_menu.add_cascade(label='Help')
        View_Menu = Menu(Main_menu, tearoff=False)
        View_Menu.add_command(label='Сhange View', command=self.more_functions)
        Main_menu.add_cascade(label='View', menu = View_Menu)
        Main_menu.add_cascade(label='Exit', command=master.destroy)

        File_Menu.add_separator()
        File_Menu.add_command(label='Exit', command=self.master.destroy)
        mainframe = ttk.Frame(self.master, padding="30 20")
        mainframe.grid(column=0, row=0, sticky=(S))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(2, weight=100)
        self.master.rowconfigure(4, weight=100)

        # texts entryes и comboboxes

        ttk.Label(mainframe, text='Системы счисления', font='Helvetica 14 bold').grid(column=0, row=0, columnspan=3,
                                                                                  sticky=N, pady='0 10')
        ttk.Label(mainframe, text='Введите число', font='Helvetica 8').grid(column=0, row=1, sticky=W)
        ttk.Label(mainframe, text='Система', font='Helvetica 8').grid(column=1, row=1, sticky=W, padx='30 0')
        self.systemCom_from = ttk.Combobox(mainframe, width=4, textvariable=StringVar(),
                                           values=(tuple((i for i in range(2, 17)))))
        self.entry_from = ttk.Entry(mainframe, width=30, textvariable=StringVar())
        self.entry_from.grid(column=0, row=2, sticky=E, pady='5 20')
        self.entry_from.focus()
        self.systemCom_from.grid(column=1, row=2, sticky=E, pady='5 20', padx='30 0')
        ttk.Label(mainframe, text='Получившееся число', font='Helvetica 8').grid(column=0, row=3, sticky=W)
        ttk.Label(mainframe, text='Система', font='Helvetica 8').grid(column=1, row=3, sticky=W, padx='30 0')
        self.entry_to = ttk.Entry(mainframe, width=30, textvariable=StringVar())
        self.entry_to.grid(column=0, row=4, sticky=E, pady='5 20')
        self.systemCom_to = ttk.Combobox(mainframe, width=4, textvariable=StringVar(),
                                         values=(tuple((i for i in range(2, 17)))))
        self.systemCom_to.grid(column=1, row=4, sticky=E, pady='5 20', padx='30 0')

        # number digitals after comma

        ttk.Label(mainframe, text='Количество знаков после запятой', font='Helvetica 8').grid(column=0, row=5, sticky=W)
        self.result_dots = ttk.Combobox(mainframe, width=4, textvariable=StringVar(),
                                        values=(tuple((i for i in range(0, 30)))))
        self.result_dots.grid(column=1, row=5, sticky=E, padx='30 0')

        # frame with buttons for numbersSystem

        resultframe = ttk.Frame(self.master, padding="30 0 30 20")
        resultframe.grid(column=0, row=1, sticky=(N))
        button = ttk.Button(resultframe, text='Перевести', padding='25 0', width=10, command=self.translate)
        button.grid(column=0, row=0, sticky=N, padx='0 20')
        button = ttk.Button(resultframe, text='Стереть', padding='25 0', width=10, command= lambda: self.clear(self.entry_to, self.entry_from))
        button.grid(column=1, row=0, sticky=N, padx='10 0')

        # set default values

        self.systemCom_from.insert(0, 10)
        self.systemCom_to.insert(0, 2)
        self.result_dots.insert(0, 0)

        #frame with ariphmetic

        additional = ttk.Frame(self.master, padding="30 20")
        additional.grid(column=0, row=2, sticky=(N, W, E, S))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        # texts entryes и comboboxes

        ttk.Label(additional, text='Арифметические операции', font='Helvetica 12 bold').grid(column=0, row=0, columnspan=3,
                                                                                  sticky=N, pady='0 10')
        ttk.Label(additional, text='Введите первое число', font='Helvetica 8').grid(column=0, row=1, sticky=W)
        ttk.Label(additional, text='Знак', font='Helvetica 8').grid(column=1, row=1, sticky=W, padx='30 0')
        self.decimalCom = ttk.Combobox(additional, width=4, textvariable=StringVar(),
                                           values=('+', '-', '×','÷'))
        self.first_digit = ttk.Entry(additional, width=30, textvariable=StringVar())
        self.first_digit.grid(column=0, row=2, sticky=E, pady='5 20')
        self.decimalCom.grid(column=1, row=2, sticky=E, pady='5 20', padx='30 0')
        ttk.Label(additional, text='Введите второе число', font='Helvetica 8').grid(column=0, row=3, sticky=W)
        ttk.Label(additional, text='Система', font='Helvetica 8').grid(column=1, row=3, sticky=W, padx='30 0')
        self.second_digit = ttk.Entry(additional, width=30, textvariable=StringVar())
        self.second_digit.grid(column=0, row=4, sticky=E, pady='5 10')
        self.systemCom = ttk.Combobox(additional, width=4, textvariable=StringVar(),
                                         values=(tuple((i for i in range(2, 17)))))
        self.systemCom.grid(column=1, row=4, sticky=E, pady='5 10', padx='30 0')

        # frame with buttons for ariphmetic operations

        resultframe2 = ttk.Frame(self.master, padding="30 0 30 20")
        resultframe2.grid(column=0, row=4, sticky=(N, W, E, S))
        button = ttk.Button(resultframe2, text='Посчитать', padding='25 0', width=10, command=self.ariphmetics_operations)
        button.grid(column=0, row=0, sticky=N, columnspan=2, padx='0 20')
        button = ttk.Button(resultframe2, text='Стереть', padding='25 0', width=10, command= lambda: self.clear(self.first_digit, self.second_digit, self.result))
        button.grid(column=2, row=0, sticky=N, padx='10 0')
        ttk.Label(resultframe2, text='Результат: ', font='Helvetica 12').grid(column=0, row=3, sticky=W, pady='20 0')
        self.result = ttk.Label(resultframe2, text='0', font='Helvetica 12')
        self.result.grid(column=1, row=3, columnspan = 2 ,sticky=W, pady='20 0')

        #default values for comboboxes

        self.decimalCom.insert(0, "+")
        self.systemCom.insert(0, 2)

        #fixed window

        self.wind_status = 1
        self.master.update()
        w = root.winfo_width()  # width of window
        h = int(root.winfo_height() / 1.9) # height of window
        self.master.maxsize(width=w, height=h)
        self.master.minsize(width=w, height=h)

        #buttons on keyboard

        self.master.bind('<Escape>', self.more_functions)

    #for clear entryes ans result label

    def clear(self, *list_with):

        for i in list_with:
            if i == self.result:
                self.result['text'] = '0'
            else:
                i.delete(0, END)

    #after this funсtion window's height decreases or increases

    def more_functions(self, *args):
        self.master.update()
        if self.wind_status == 1:
            w = root.winfo_width()  # width of window
            h = int(root.winfo_height() * 1.9)  # height of window
            self.master.maxsize(width=w, height=h)
            self.master.minsize(width=w, height=h)
            self.wind_status = 0
        else:
            w = root.winfo_width()  # width of window
            h = int(root.winfo_height() / 1.9)  # height of window
            self.master.maxsize(width=w, height=h)
            self.master.minsize(width=w, height=h)
            self.wind_status = 1

    def ten_to_q(self, number, base):
        '''функция перевода из десятичной системы счисления
        в любую другую систему счисления'''
        exp = re.split('\.|,', number)
        print(exp)
        number_int = exp[0]
        alphabet = "0123456789ABCDEF"
        r = ''
        number_int = int(number_int)
        while number_int:
            number_int, y = divmod(number_int, base)
            r = alphabet[y]+r
        if len(exp) == 0:
            return '0'
        if len(exp) > 1 and int(self.result_dots.get()) > 0:
            return r +re.findall('\.|,' , number)[0] +self.fract_ten_to_q(exp[-1], base, self.result_dots.get())
        else:
            return r

    def q_to_ten(self, number, base):
        '''функция перевода из любой системы счисления
        в десятичную систему счисления'''
        print(number, base)
        exp = re.split('\.|,', number)
        print(exp)
        number_int = exp[0]
        num_str = number_int[::-1]
        num = 0
        for k in range(len(num_str)):
            dig = num_str[k]
            if dig.isdigit():
                dig = int(dig)
            else:
                dig = ord(dig.upper())-ord('A')+10
            num += dig*(base**k)
        if len(exp) == 0:
            return '0'
        elif len(exp) > 1 and int(self.result_dots.get()) > 0:
            return str(num) + re.findall('\.|,' , str(number))[0] + self.fract_q_to_ten(exp[-1], base, self.result_dots.get())
        else:
            return str(num)

    def fract_ten_to_q(self, number, base, comma=10):
        alphabet = "0123456789ABCDEF"
        alphabet = {str(i) : alphabet[i] for i in range(len(alphabet))}
        number = float('0.'+number)
        result = ''
        while number != 0 and len(result)<int(comma)+20:
            number *= int(base)
            exp = re.split('\.', str(number))
            result += alphabet[exp[0]]
            number = float('0.'+exp[-1])
        result = result + '0'*(int(comma) - len(result))
        result = result[:int(comma)]
        print('result', result)
        return result

    def fract_q_to_ten(self, number, base, comma=10):
        alphabet = "0123456789ABCDEF"
        number = [int(alphabet.index(i.upper())) for i in list(number)]
        result = 0
        for i in range(0, len(number)):
            result += number[i] * int(base) ** ((i+1) // -1)
        result = str(round(float(result), int(comma)))
        result = str(result)[2:]
        result += (int(comma) - len(result)) * '0'

        return result
    def translate(self, *args):
        '''функция перевода чисел из одной системы счисления в другую.
        Данная функция будет обращаться за помощью к функциям
        ten_to_q а также к функции q_to_ten'''
        number = self.entry_from.get()
        base = int(self.systemCom_from.get())
        to_base = int(self.systemCom_to.get())
        print(number,'-', base, '-',to_base)
        # fixme Ниже код для тестов, его нужно править
        # fixme но я думаю что if elif else тут будет уместно
        # fixme определиться с целом либо дробным числом
        self.entry_to.delete(0, END)
        if base == 10:
            self.entry_to.insert(0, self.ten_to_q(number, to_base))
        elif to_base == 10:
            self.entry_to.insert(0,self.q_to_ten(number, base))
        else:
            self.entry_to.insert(0,self.ten_to_q(self.q_to_ten(number, base), to_base))

    #ariphmetics operations will processing when user press button посчитать

    def ariphmetics_operations(self):
        '''функция арифметический операций в разных системах исчисления, данная
        фуекция будет обращаться за помощью к функциям add, minus, dev, mult'''
        first_number = str(self.first_digit.get())
        second_number = str(self.second_digit.get())
        decimal = self.decimalCom.get()
        base = int(self.systemCom.get())
        if decimal == '+':
            result = self.add(first_number, second_number, base)
        elif decimal == '-':
            result = self.minus(first_number, second_number, base)
        elif decimal == '/' or decimal == '÷':
            result = self.dev(first_number, second_number, base)
        elif decimal == '*' or decimal == '×':
            result = self.mult(first_number, second_number, base)
        self.result['text'] = result
        if self.result['text'] == '':
            self.result['text'] = '0'

    def add(self, first_digit, second_digit, base):
        return self.ten_to_q(str(float(self.q_to_ten(first_digit, base)) + float(self.q_to_ten(second_digit, base))), base)

    def minus(self, first_digit, second_digit, base):
        return self.ten_to_q(str(float(self.q_to_ten(first_digit, base)) - float(self.q_to_ten(second_digit, base))), base)

    def mult(self, first_digit, second_digit, base):
        return self.ten_to_q(str(float(self.q_to_ten(first_digit, base)) * float(self.q_to_ten(second_digit, base))), base)

    def dev(self, first_digit, second_digit, base):
        return self.ten_to_q(str(float(self.q_to_ten(first_digit, base)) / float(self.q_to_ten(second_digit, base))), base)


def main():
    global root
    root = Tk()
    window = Application(root)
    root.mainloop()


if __name__ == "__main__":
    main()