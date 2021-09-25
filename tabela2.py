from tkinter import ttk
import tkinter as tk
window = tk.Tk()
window.resizable(width = 1, height = 1)
treev = ttk.Treeview(window, selectmode ='browse')
treev.pack()
verscrlbar = ttk.Scrollbar(window,
                           orient ="vertical",
                           command = treev.yview)
verscrlbar.pack(side ='right', fill ='x')
treev.configure(xscrollcommand = verscrlbar.set)
treev["columns"] = ("1", "2", "3")
treev['show'] = 'headings'
treev.column("1", width = 90, anchor ='c')
treev.column("2", width = 90, anchor ='se')
treev.column("3", width = 90, anchor ='se')
treev.heading("1", text ="Name")
treev.heading("2", text ="Sex")
treev.heading("3", text ="Age")
treev.insert("", 'end', text ="L1",
             values =("Nidhi", "F", "25"))
treev.insert("", 'end', text ="L2",
             values =("Nisha", "F", "23"))


window.mainloop()