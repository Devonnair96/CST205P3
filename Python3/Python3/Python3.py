from tkinter import *
class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        
        self.master = master
       
        self.init_window()

    def init_window(self):
        self.master.title("Teststuff")
        self.pack(fill=BOTH, expand=1)
        quitButton = Button(self, text="Quit", command=self.gamequit)
        quitButton.place(x=0, y=0)

    def gamequit(self):
        exit()

root = Tk()
root.geometry("400x400")
app = Window(root)
root.mainloop()