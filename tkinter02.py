from tkinter import *
from tkinter import messagebox, ttk

'''

# ---- 1 ----

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


# ---- 2 ----

def get_data(event=None): 

    print("String: ", strVar.get()) 

    print("Integer: ", intVar.get()) 

    print("Double: ", dbVar.get()) 

    print("Boolean: ", boolVar.get()) 

  
def bind_button(event=None): 

    if boolVar.get(): 

        getDataButton.unbind("<Button-1>") 

    else: 

        getDataButton.bind("<Button-1>", get_data) 


root = Tk() 

strVar = StringVar() 

intVar = IntVar() 

dbVar = DoubleVar() 

boolVar = BooleanVar() 

strVar.set("Enter String") 

intVar.set("Enter Integer") 

dbVar.set("Enter Double") 

boolVar.set(True) 

strEntry = Entry(root, textvariable=strVar) 

strEntry.pack(side=LEFT) 
 

intEntry = Entry(root, textvariable=intVar) 

intEntry.pack(side=LEFT) 


dbEntry = Entry(root, textvariable=dbVar) 

dbEntry.pack(side=LEFT) 


theCheckBut = Checkbutton(root, text="Switch", variable=boolVar) 

theCheckBut.bind("<Button-1>", bind_button) 

theCheckBut.pack(side=LEFT) 

getDataButton = Button(root, text="Get Data") 

getDataButton.bind("<Button-1>", get_data) 

getDataButton.pack(side=LEFT) 

root.mainloop() 


# ---- 3 ----

def open_msg_box(): 

    messagebox.showwarning( 

        "Event Triggered", 

        "Button Clicked" 

    ) 

  
root = Tk() 

root.geometry("300x300") 

root.resizable(width=False, height=False) 

frame = Frame(root) 

style = ttk.Style() 
  
style.configure("TButton", 

                foreground="midnight blue", 

                font="Times 20 bold italic", 

                padding=20) 


print(ttk.Style().theme_names()) 

print(style.lookup("TButton", "font")) 

print(style.lookup("TButton", "foreground")) 

print(style.lookup("TButton", "padding")) 

theButton = ttk.Button(frame, 

                       text="Important Button", 

                       command=open_msg_box) 


theButton['state'] = 'disabled' 

theButton['state'] = 'normal' 

theButton.pack() 

frame.pack() 

root.mainloop() 


# ---- 4 ----


def quit_app(): 

    root.quit() 
 

def show_about(event=None): 

    messagebox.showwarning( 

        "About", 

        "This Awesome Program was made in 2016" 

    ) 


root = Tk() 

the_menu = Menu(root) 

file_menu = Menu(the_menu, tearoff=0) 

file_menu.add_command(label="Open") 

file_menu.add_command(label="Save") 

file_menu.add_separator() 

file_menu.add_command(label="Quit", command=quit_app) 

the_menu.add_cascade(label="File", menu=file_menu) 

root.config(menu=the_menu) 

root.mainloop() 


'''



def quit_app():
    root.quit()


def show_about(event=None):
    messagebox.showwarning(
        "About",
        "This Awesome Program was made in 2021"
    )


root = Tk()

the_menu = Menu(root)

# ----- File Menu ----- #


file_menu = Menu(the_menu, tearoff=0)

file_menu.add_command(label="Open")

file_menu.add_command(label="Save")

file_menu.add_separator()

file_menu.add_command(label="Quit", command=quit_app)

the_menu.add_cascade(label="File", menu=file_menu)

# ----- Font Menu ----- #
text_font = StringVar()
text_font.set("Times")


def change_font(event=None):
    print("Font Picked: ", text_font.get())


font_menu = Menu(the_menu, tearoff=0)

font_menu.add_radiobutton(label="Times",
                          variable=text_font,
                          command=change_font)

font_menu.add_radiobutton(label="Courier",
                          variable=text_font,
                          command=change_font)

font_menu.add_radiobutton(label="Ariel",
                          variable=text_font,
                          command=change_font)


# ----- View Menu ----- #

view_menu = Menu(the_menu, tearoff=0)

line_numbers = IntVar()
line_numbers.set(1)

view_menu.add_checkbutton(label="Line Numbers",
                          variable=line_numbers)

view_menu.add_cascade(label="Fonts", menu=font_menu)

the_menu.add_cascade(label="View", menu=view_menu)


# ----- Help Menu ----- #

help_menu = Menu(the_menu, tearoff=0)

# accelerator is used to show a shortcut
# OSX, Windows and Linux use the following options
# Command-O, Shift+Ctrl+S, Command-Option-Q with the
# modifiers Control, Ctrl, Option, Opt, Alt, Shift,
# and Command

help_menu.add_command(label="About",
                      accelerator="command-A",
                      command=show_about)

the_menu.add_cascade(label="Help", menu=help_menu)

root.bind('<Command-A>', show_about)
root.bind('<Command-a>', show_about)


root.config(menu=the_menu)

root.mainloop()
