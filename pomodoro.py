import tkinter as tk
from tkinter import ttk

class PomdoroTimer(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)

        self.title("Pomodoro Timer")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.wm_iconbitmap('C:/Python Projects/Pomtimer/tom.ico')

        contrainer = ttk.Frame(self)
        contrainer.grid
        contrainer.columnconfigure(0, weight=1)

        timer_frame = Timer(contrainer)
        timer_frame.grid(row=0, column=0, sticky="NESW")

class Timer(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

    def decrement_time(self):
        pass

app = PomdoroTimer()
app.mainloop()