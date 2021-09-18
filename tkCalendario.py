from tkinter import *
from tkcalendar import *

# root = Tk()
# root.title("Calendario")
# root.geometry("600x400")
#
# cal = Calendar(root, selectmode="day", year=2021, month=9, day=15)
# cal.pack(pady=20, fill="both", expand=True)
#
#
# def grab_date():
#     #my_label.config(text=cal.get_date())
#     my_label.config(text="Hoje é: " + cal.get_date())
#
#
# my_button = Button(root, text="Get Date", command=grab_date)
# my_button.pack(pady=20)
#
# my_label = Label(root, text="")
# my_label.pack(pady=20)
#
#
#
# root.mainloop()

screen = Tk()
screen.minsize(800, 600)
screen.title("Meu calendario")
screen.config(bg="#A1CDEC")

def selectDate():
    myDate = myCal.get_date()
    selectedDate = Label(text=myDate)
    selectedDate.place(x=425, y=350)


myCal = Calendar(screen, setmode='day', date_pattern='d/m/yy')
myCal.place(x=300, y=100)


openCal = Button(screen, text="Select Date", command=selectDate)
openCal.place(x=425, y=300)


screen.mainloop()




