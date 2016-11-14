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

def reset():
    frame1.pack_forget()
    createDoors(numberOfDoors2)

def createRooms(img1, img2):
    
    

    global frame1
    frame1 = Frame(newWindow)
    frame1.pack()
   
    
    pathToImage1 = Image.open("/Users/siddarthkrishnan/Desktop/" + img1)
    pathToImage2 = Image.open("/Users/siddarthkrishnan/Desktop/" + img2)
    photoImage1 = ImageTk.PhotoImage(pathToImage1)
    photoImage2 = ImageTk.PhotoImage(pathToImage2)
    label1 = Label(frame1,image = photoImage1)
    label1.image = photoImage1
    label1.pack(side = RIGHT)
    label2 = Label(frame1,image= photoImage2)
    label2.image = photoImage2
    label2.pack(side = RIGHT)
    button1 = Button(frame1, command = reset)
    button1.pack()
    button2 = Button(frame1, command = reset)
    button2.pack()
    
    
     


def staffRoom():
    createRooms("firestaff.jpg", "WaterStaff.jpg")
    
    


def topRoom():
    createRooms("firetop.jpg", "waterRobe.jpg")


def wizardHatRoom():
    createRooms("waterHat.jpg", "FireHat.jpg")


def bottomRoom():
    createRooms("fireRobe.jpg", "waterBottom.jpg")




randomArray = [1,2,3,4]


def DoorUpdate():
    
    
    numberOfDoors1 = numberOfTimesDecremented

    global numberOfDoors2
    numberOfDoors2 = numberOfDoors1  - 1

    
    randomNumber = random.choice(randomArray)

    if randomNumber == 1:
        messagebox.showinfo("You have entered the staff room")
        frame.pack_forget()
        randomArray.remove(randomNumber)
        staffRoom()
    if randomNumber == 2:
        messagebox.showinfo("You have entered the top room")
        frame.pack_forget()
        randomArray.remove(randomNumber)
        topRoom()
    if randomNumber == 3:
        messagebox.showinfo("You have entered the bottom room")
        frame.pack_forget()
        randomArray.remove(randomNumber)
        bottomRoom()
    if randomNumber == 4:
        messagebox.showinfo("You have entered the hat room")
        frame.pack_forget()
        randomArray.remove(randomNumber)
        wizardHatRoom()
    
   

    

    
    
   
    

  

    




   
        

    

    

    



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


    
                    
