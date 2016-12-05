from tkinter import *
import time
from tkinter import messagebox
import random
import smtplib
from PIL import ImageTk, Image

def ClearScreen():
    button1.destroy()
    button2.destroy()
    button3.destroy()
    label1.destroy()
    label2.destroy()
    label3.destroy()
    textLabel.destroy()
    entry.destroy()
def reset():
    frame1.pack_forget()
    if (choice == 1):
        WizardCreateDoors(numberOfDoors2)
    if (choice == 2):
        WarriorCreateDoors(numberOfDoors2)
    if (choice == 3):
        RangerCreateDoors(numberOfDoors2)
def createRooms(img1, img2):
    global frame1
    frame1 = Frame(newWindow)
    frame1.pack()
    pathToImage1 = Image.open(img1)
    pathToImage2 = Image.open(img2)
    photoImage1 = ImageTk.PhotoImage(pathToImage1)
    photoImage2 = ImageTk.PhotoImage(pathToImage2)
    label1 = Label(frame1,image = photoImage1)
    label1.image = photoImage1
    label1.pack(side = RIGHT)
    label2 = Label(frame1,image= photoImage2)
    label2.image = photoImage2
    label2.pack(side = RIGHT)
    button1 = Button(frame1, command = reset)
    button1.pack(side = RIGHT)
    button2 = Button(frame1, command = reset)
    button2.pack(side = RIGHT)

def staffRoom():
    createRooms("firestaff1.jpg", "WaterStaff1.jpg")
def topRoom():
    createRooms("firetop1.jpg", "waterRobe1.jpg")
def wizardHatRoom():
    createRooms("waterHat1.jpg", "FireHat1.jpg")
def bottomRoom():
    createRooms("fireRobe1.jpg", "waterBottom1.jpg")

def swordRoom():
    createRooms("ElementalSword.jpg","MetalSword.jpg")
def legsRoom():
    createRooms("ElementalLegs.jpg","MetalLegs.jpg")
def chestRoom():
    createRooms("ElementalPlate.jpg", "MetalBody.jpg")
def helmRoom():
    createRooms("ElementalFullHelm.jpg", "MetalFullHelm.jpg")

def bowRoom():
    createRooms("ElementalBow.jpg", "Bow.jpg")
def RangerHatRoom():
    createRooms("elementalArcherHat.png", "robinHoodHat.jpg")
def leggingsRoom():
    createRooms("elementalArcherLegs.png","archerLegs.png")
def torsoRoom():
    createRooms("elementalArcherTop.png", "ArcherTop.jpg")

randomArray = [1,2,3,4]


def WizardDoorUpdate():
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

def WarriorDoorUpdate():
    numberOfDoors1 = numberOfTimesDecremented

    global numberOfDoors2
    numberOfDoors2 = numberOfDoors1  - 1
    randomNumber = random.choice(randomArray)

    if randomNumber == 1:
        messagebox.showinfo("You have entered the sword room")
        frame.pack_forget()
        randomArray.remove(randomNumber)
        swordRoom()
    if randomNumber == 2:
        messagebox.showinfo("You have entered the chest room")
        frame.pack_forget()
        randomArray.remove(randomNumber)
        chestRoom()
    if randomNumber == 3:
        messagebox.showinfo("You have entered the greaves room")
        frame.pack_forget()
        randomArray.remove(randomNumber)
        legsRoom()
    if randomNumber == 4:
        messagebox.showinfo("You have entered the helm room")
        frame.pack_forget()
        randomArray.remove(randomNumber)
        helmRoom()

def RangerDoorUpdate():
    numberOfDoors1 = numberOfTimesDecremented

    global numberOfDoors2
    numberOfDoors2 = numberOfDoors1  - 1
    randomNumber = random.choice(randomArray)
    if randomNumber == 1:
        messagebox.showinfo("You have entered the bow room")
        frame.pack_forget()
        randomArray.remove(randomNumber)
        bowRoom()
    if randomNumber == 2:
        messagebox.showinfo("You have entered the torso room")
        frame.pack_forget()
        randomArray.remove(randomNumber)
        torsoRoom()
    if randomNumber == 3:
        messagebox.showinfo("You have entered the leggings room")
        frame.pack_forget()
        randomArray.remove(randomNumber)
        leggingsRoom()
    if randomNumber == 4:
        messagebox.showinfo("You have entered the hat room")
        frame.pack_forget()
        randomArray.remove(randomNumber)
        RangerHatRoom()

def WizardDoor():
    global userEmail
    userEmail = entry.get()
    try:
        gameserver  =  smtplib.SMTP('smtp.gmail.com',587)
        gameserver.ehlo()
    except:
        print ("There was a problem")
    gameserver.starttls()
    password = getpass.getpass("Enter your password: ")
    gameserver.login( userEmail, password) # the user sends the results to themselves
    gameserver.sendmail( userEmail, userEmail, "Hello player") #placeholder until results are ready
    gameserver.quit()
    ClearScreen()
    global choice
    choice = 1
    messagebox.showinfo("wizard door", "You have entered the Wizard door! Choose another door and this will lead you to either the hat door, the top door, the robe door, or the staff door.")
    WizardCreateDoors(4)
def WarriorDoor():
    global userEmail
    userEmail = entry.get()
    try:
        gameserver  =  smtplib.SMTP('smtp.gmail.com',587)
        gameserver.ehlo()
    except:
        print("There was a problem")
    gameserver.starttls()
    password = getpass.getpass("Enter your password: ")
    gameserver.login( userEmail, password) # the user sends the results to themselves
    gameserver.sendmail( userEmail, userEmail, "Hello player") #placeholder until results are ready
    gameserver.quit()
    ClearScreen()
    global choice
    choice = 2
    messagebox.showinfo("warrior door", "You have entered the Warrior door! Choose another door and this will lead you to either the helm door, the chest door, the greaves door, or the sword door.")
    WarriorCreateDoors(4)
def RangerDoor():
    global userEmail
    userEmail = entry.get()
    try:
        gameserver  =  smtplib.SMTP('smtp.gmail.com',587)
        gameserver.ehlo()
    except:
        print("There was a problem")
    gameserver.starttls()
    password = getpass.getpass("Enter your password: ")
    gameserver.login( userEmail, password) # the user sends the results to themselves
    gameserver.sendmail( userEmail, userEmail, "Hello player") #placeholder until results are ready
    gameserver.quit()
    ClearScreen()
    global choice
    choice = 3
    messagebox.showinfo("ranger door", "You have entered the Ranger door! Choose another door and this will lead you to either the hat door, the torso door, the leggings door, or the bow door.")
    RangerCreateDoors(4)

def WizardCreateDoors(numberOfDoors):
    global numberOfTimesDecremented
    numberOfTimesDecremented = 0
    img5 = Image.open("door5.jpg")
    img6 = ImageTk.PhotoImage(img1)
    global frame
    frame = Frame(newWindow)
    frame.pack()
    while numberOfDoors != 0:
        global labelx
        labelx = Label(frame, image = img2)
        labelx.pack(side = RIGHT)
        global button1
        button1 = Button(frame, command = WizardDoorUpdate)
        button1.pack(side = RIGHT)
        numberOfDoors = numberOfDoors - 1
        numberOfTimesDecremented = numberOfTimesDecremented + 1
def WarriorCreateDoors(numberOfDoors):
    global numberOfTimesDecremented
    numberOfTimesDecremented = 0
    img5 = Image.open("door5.jpg")
    img6 = ImageTk.PhotoImage(img1)
    global frame
    frame = Frame(newWindow)
    frame.pack()
    while numberOfDoors != 0:
        global labelx
        labelx = Label(frame, image = img2)
        labelx.pack(side = RIGHT)
        global button2
        button2 = Button(frame, command = WarriorDoorUpdate)
        button2.pack(side = RIGHT)
        numberOfDoors = numberOfDoors - 1
        numberOfTimesDecremented = numberOfTimesDecremented + 1
def RangerCreateDoors(numberOfDoors):
    global numberOfTimesDecremented
    numberOfTimesDecremented = 0
    img5 = Image.open("door5.jpg")
    img6 = ImageTk.PhotoImage(img1)
    global frame
    frame = Frame(newWindow)
    frame.pack()
    while numberOfDoors != 0:
        global labelx
        labelx = Label(frame, image = img2)
        labelx.pack(side = RIGHT)
        global button2
        button2 = Button(frame, command = RangerDoorUpdate)
        button2.pack(side = RIGHT)
        numberOfDoors = numberOfDoors - 1
        numberOfTimesDecremented = numberOfTimesDecremented + 1

newWindow = Tk()
mytext = StringVar()
entry = Entry(newWindow, textvariable = mytext)
entry.pack(side = BOTTOM)
textLabel = Label(newWindow, text = "Enter your email")
textLabel.pack(side = BOTTOM)
img1 = Image.open("door5.jpg")
img2 = ImageTk.PhotoImage(img1)
label1 = Label(newWindow, image = img2)
label1.pack(side = RIGHT)
label2 = Label(newWindow, image = img2)
label2.pack(side = RIGHT)
label3 = Label(newWindow, image = img2)
label3.pack(side = RIGHT)
wizardDoorCount = 4
button1 = Button(newWindow, text = "WIZARD", command = WizardDoor)
button1.pack(side = BOTTOM)
button2 = Button(newWindow, text = "WARRIOR", command = WarriorDoor)
button2.pack(side = BOTTOM)
button3 = Button(newWindow, text = "RANGER", command = RangerDoor)
button3.pack(side = BOTTOM)
