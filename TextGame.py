#comment
from tkinter import *
import time
from tkinter import messagebox
import random

from PIL import ImageTk, Image
# hi my name is siddarth




#hi my name is siddarth krishnan. I love to play tennis.



def ClearScreen():
    button1.destroy()
    button2.destroy()
    button3.destroy()
    label1.destroy()
    label2.destroy()
    label3.destroy()


    


def DoorUpdate():
    numberOfDoors1 = numberOfTimesDecremented

    numberOfDoors2 = numberOfDoors1  - 1

     
        

    
        
        

    
    frame.destroy()

    

    createDoors(numberOfDoors2)


    

   
        

    

    

    



def createDoors(numberOfDoors):

   
    global numberOfTimesDecremented
    numberOfTimesDecremented = 0
    
    img5 = Image.open("/Users/siddarthkrishnan/Desktop/door5.jpg")
    img6 = ImageTk.PhotoImage(img1)

    global frame
    frame = Frame(newWindow)
    frame.pack()
    
   
    while numberOfDoors != 0:
        global labelx
        labelx = Label(frame, image = img2)
        labelx.pack(side = RIGHT)
        global button2
        button2 = Button(frame, command = DoorUpdate)
        button2.pack(side = RIGHT)
        numberOfDoors = numberOfDoors - 1
        numberOfTimesDecremented = numberOfTimesDecremented + 1

   
    

        




    



    



        

        
    
    
    



def WizardDoor():
    ClearScreen()
    
 
                          
 
    messagebox.showinfo("wizard door", "You have entered the Wizard door! Choose another door and this will lead you to either the hat door, the top door, the robe door, or the staff door.")
    createDoors(4)


                             
   
    
    
    

newWindow = Tk()
img1 = Image.open("/Users/siddarthkrishnan/Desktop/door5.jpg")
img2 = ImageTk.PhotoImage(img1)
label1 = Label(newWindow, image = img2)
label1.pack(side = RIGHT)
label2 = Label(newWindow, image = img2)
label2.pack()
label3 = Label(newWindow, image = img2)
label3.pack(side = LEFT)
wizardDoorCount = 4
button1 = Button(newWindow, text = "WIZARD", command = WizardDoor)
button1.pack(side = RIGHT)
button2 = Button(newWindow, text = "WARRIOR")
button2.pack(side = LEFT)
button3 = Button(newWindow, text = "RANGER")
button3.pack()


    
                    


    

