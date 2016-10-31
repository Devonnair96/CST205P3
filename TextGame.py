
from tkinter import *
from PIL import ImageTk, Image



def Dragon_Door():
    button1.destroy()
    button2.destroy()
    button3.destroy()
    label1.destroy()
    label2.destroy()
    label3.destroy()
    dragonImage = Image.open("/Users/siddarthkrishnan/Desktop/dragon12.jpg")
    dragonImage1 = ImageTk.PhotoImage(dragonImage)
    labelx = Label(newWindow,image = dragonImage1)
    labelx.image = dragonImage1
    labelx.pack()
    
    
    

newWindow = Tk()
img1 = Image.open("/Users/siddarthkrishnan/Desktop/door5.jpg")
img2 = ImageTk.PhotoImage(img1)
label1 = Label(newWindow, image = img2)
label1.pack(side = RIGHT)
label2 = Label(newWindow, image = img2)
label2.pack()
label3 = Label(newWindow, image = img2)
label3.pack(side = LEFT)
button1 = Button(newWindow, text = "DRAGON", command = Dragon_Door)
button1.pack(side = RIGHT)
button2 = Button(newWindow, text = "WARRIOR")
button2.pack(side = LEFT)
button3 = Button(newWindow, text = "WIZARD")
button3.pack()

    
                    


    

