from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
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
        self.master.maxsize(width=326, height=309)
        self.master.minsize(width=326, height=309)
        self.master.iconbitmap(r'calculator_icon.ico')

        # menu

        Main_menu = Menu(self.master)
        self.master.config(menu=Main_menu)
        File_Menu = Menu(Main_menu, tearoff=False)
        Main_menu.add_cascade(label='File', menu=File_Menu)
        Main_menu.add_cascade(label='About')
        Main_menu.add_cascade(label='Exit', command=self.master.destroy)
        Main_menu.add_cascade(label='About', command=show_about)
        Main_menu.add_cascade(label='Help')
        Main_menu.add_cascade(label='Exit', command=master.destroy)
        File_Menu.add_command(label='New')
        File_Menu.add_command(label='Save')
        File_Menu.add_separator()
        File_Menu.add_command(label='Exit', command=self.master.destroy)
        mainframe = ttk.Frame(self.master, padding="30 20")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        # for entryes

        self.system_from = StringVar()
        self.system_in = StringVar()
        self.number_from = StringVar()
        self.number_in = StringVar()
        self.dots_count = StringVar()

        # texts entryes и comboboxes

        ttk.Label(mainframe, text='Системы счисления', font='arial 14 bold').grid(column=0, row=0, columnspan=3,
                                                                                  sticky=N, pady='0 10')
        ttk.Label(mainframe, text='Введите число', font='arial 8').grid(column=0, row=1, sticky=W)
        ttk.Label(mainframe, text='Система', font='arial 8').grid(column=1, row=1, sticky=E, padx='30 0')
        self.systemCom_from = ttk.Combobox(mainframe, width=4, textvariable=self.system_from,
                                           values=(tuple((i for i in range(2, 17)))))
        self.entry_from = ttk.Entry(mainframe, width=30, textvariable=self.number_from)
        self.entry_from.grid(column=0, row=2, sticky=E, pady='5 20')
        self.entry_from.focus()
        self.systemCom_from.grid(column=1, row=2, sticky=E, pady='5 20', padx='30 0')
        ttk.Label(mainframe, text='Получившееся число', font='arial 8').grid(column=0, row=3, sticky=W)
        ttk.Label(mainframe, text='Система', font='arial 8').grid(column=1, row=3, sticky=E, padx='30 0')
        self.entry_to = ttk.Entry(mainframe, width=30, textvariable=self.number_in)
        self.entry_to.grid(column=0, row=4, sticky=E, pady='5 20')
        self.systemCom_to = ttk.Combobox(mainframe, width=4, textvariable=self.system_in,
                                         values=(tuple((i for i in range(2, 17)))))
        self.systemCom_to.grid(column=1, row=4, sticky=E, pady='5 20', padx='30 0')

        # number digitals after comma

        ttk.Label(mainframe, text='Количество знаков после запятой', font='arial 8').grid(column=0, row=5, sticky=W)
        self.result_dots = ttk.Combobox(mainframe, width=4, textvariable=self.dots_count,
                                        values=(tuple((i for i in range(0, 30)))))
        self.result_dots.grid(column=1, row=5, sticky=E, padx='30 0')

        # frame with button and result

        resultframe = ttk.Frame(self.master, padding="30 0 30 20")
        resultframe.grid(column=0, row=1, sticky=(N, W, E, S))
        button = ttk.Button(resultframe, text='Вычислить', width=18, command=root.destroy)
        button.grid(column=0, columnspan=2, row=0, sticky=W, padx='0 20')
        button = ttk.Button(resultframe, text='Стереть', width=18, command=self.clear)
        button.grid(column=3, row=0, sticky=E, padx='10 0')
        ttk.Label(resultframe, text='Результат:', font='arial 11 bold').grid(column=0, row=1, sticky=W, pady='15 0')
        self.result = ttk.Label(resultframe, text='0', font='arial 14')
        self.result.grid(column=1, row=1, sticky=W, columnspan=3, pady='13 0')

    def clear(self):
        self.entry_to.delete(0, END)
        self.entry_from.delete(0, END)
        self.result['text'] = 0


def main():
    global root
    root = Tk()
    window = Application(root)
    root.mainloop()

if __name__ == "__main__":
    main()

