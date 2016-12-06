from tkinter import *
import time
from tkinter import messagebox
import random
import smtplib
import getpass
from PIL import ImageTk, Image
gold = 500
def resetGold():
    spentGold()
    reset()
def spentGold():
    global gold
    gold = gold - 250
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
    goldLabel.destroy()
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
    if gold >= 250:
        button1 = Button(frame1, command = resetGold)
        button1.pack(side = RIGHT)
    button2 = Button(frame1, command = reset)
    button2.pack(side = RIGHT)
    costlabel = Label(frame1, text = "Gold Price: 0")
    costlabel.pack(side = LEFT)
    costlabel2 = Label(frame1, text = "Gold Price: 250")
    costlabel2.pack(side = RIGHT)

def staffRoom():
    createRooms("waterstaff1.jpg", "fireStaff1.jpg")
def topRoom():
    createRooms("firetop1.jpg", "waterRobe1.jpg")
def wizardHatRoom():
    createRooms("fireHat1.jpg", "waterHat1.jpg")
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
randomGold = [1,2,3,4]

def WizardDoorUpdate():
    numberOfDoors1 = numberOfTimesDecremented

    global numberOfDoors2
    numberOfDoors2 = numberOfDoors1  - 1

    randomNumber = random.choice(randomArray)
    goldFind = random.choice(randomGold)

    if randomNumber == 1:
        messagebox.showinfo("You have entered the staff room")
        if goldFind == 1:
            global gold
            messagebox.showinfo("You also found 250 gold in the room")
            gold = gold + 250
        frame.pack_forget()
        randomArray.remove(randomNumber)
        staffRoom()
    if randomNumber == 2:
        messagebox.showinfo("You have entered the top room")
        if goldFind == 1:
            global gold
            messagebox.showinfo("You also found 250 gold in the room")
            gold = gold + 250
        frame.pack_forget()
        randomArray.remove(randomNumber)
        topRoom()
    if randomNumber == 3:
        messagebox.showinfo("You have entered the bottom room")
        if goldFind == 1:
            global gold
            messagebox.showinfo("You also found 250 gold in the room")
            gold = gold + 250
        frame.pack_forget()
        randomArray.remove(randomNumber)
        bottomRoom()
    if randomNumber == 4:
        messagebox.showinfo("You have entered the hat room")
        if goldFind == 1:
            global gold
            messagebox.showinfo("You also found 250 gold in the room")
            gold = gold + 250
        frame.pack_forget()
        randomArray.remove(randomNumber)
        wizardHatRoom()

def WarriorDoorUpdate():
    numberOfDoors1 = numberOfTimesDecremented

    global numberOfDoors2
    numberOfDoors2 = numberOfDoors1  - 1
    randomNumber = random.choice(randomArray)
    goldFind = random.choice(randomGold)
    if randomNumber == 1:
        messagebox.showinfo("You have entered the sword room")
        if goldFind == 1:
            global gold
            messagebox.showinfo("You also found 250 gold in the room")
            gold = gold + 250
        frame.pack_forget()
        randomArray.remove(randomNumber)
        swordRoom()
    if randomNumber == 2:
        messagebox.showinfo("You have entered the chest room")
        if goldFind == 1:
            global gold
            messagebox.showinfo("You also found 250 gold in the room")
            gold = gold + 250
        frame.pack_forget()
        randomArray.remove(randomNumber)
        chestRoom()
    if randomNumber == 3:
        messagebox.showinfo("You have entered the greaves room")
        if goldFind == 1:
            global gold
            messagebox.showinfo("You also found 250 gold in the room")
            gold = gold + 250
        frame.pack_forget()
        randomArray.remove(randomNumber)
        legsRoom()
    if randomNumber == 4:
        messagebox.showinfo("You have entered the helm room")
        if goldFind == 1:
            global gold
            messagebox.showinfo("You also found 250 gold in the room")
            gold = gold + 250
        frame.pack_forget()
        randomArray.remove(randomNumber)
        helmRoom()

def RangerDoorUpdate():
    numberOfDoors1 = numberOfTimesDecremented

    global numberOfDoors2
    numberOfDoors2 = numberOfDoors1  - 1
    randomNumber = random.choice(randomArray)
    goldFind = random.choice(randomGold)
    if randomNumber == 1:
        messagebox.showinfo("You have entered the bow room")
        if goldFind == 1:
            global gold
            messagebox.showinfo("You also found 250 gold in the room")
            gold = gold + 250
        frame.pack_forget()
        randomArray.remove(randomNumber)
        bowRoom()
    if randomNumber == 2:
        messagebox.showinfo("You have entered the torso room")
        if goldFind == 1:
            global gold
            messagebox.showinfo("You also found 250 gold in the room")
            gold = gold + 250
        frame.pack_forget()
        randomArray.remove(randomNumber)
        torsoRoom()
    if randomNumber == 3:
        messagebox.showinfo("You have entered the leggings room")
        if goldFind == 1:
            global gold
            messagebox.showinfo("You also found 250 gold in the room")
            gold = gold + 250
        frame.pack_forget()
        randomArray.remove(randomNumber)
        leggingsRoom()
    if randomNumber == 4:
        messagebox.showinfo("You have entered the hat room")
        if goldFind == 1:
            global gold
            messagebox.showinfo("You also found 250 gold in the room")
            gold = gold + 250
        frame.pack_forget()
        randomArray.remove(randomNumber)
        RangerHatRoom()

def WizardDoor():
    global userEmail
    userEmail = entry.get()
    if userEmail != "":
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
    if userEmail != "":
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
    if userEmail != "":
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
    goldamount = StringVar()
    goldamount.set("Gold: " + str(gold))
    global goldLabel
    goldLabel = Label(newWindow, textvariable = goldamount)
    goldLabel.pack(side = TOP)
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
    goldamount = StringVar()
    goldamount.set("Gold: " + str(gold))
    global goldLabel
    goldLabel = Label(newWindow, textvariable = goldamount)
    goldLabel.pack(side = TOP)
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
    goldamount = StringVar()
    goldamount.set("Gold: " + str(gold))
    global goldLabel
    goldLabel = Label(newWindow, textvariable = goldamount)
    goldLabel.pack(side = TOP)
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
goldamount = StringVar()
goldamount.set("Gold: " + str(gold))
global goldLabel
goldLabel = Label(newWindow, textvariable = goldamount)
entry = Entry(newWindow, textvariable = mytext)
entry.pack(side = BOTTOM)
textLabel = Label(newWindow, text = "Enter your email")
textLabel.pack(side = BOTTOM)
img1 = Image.open("door5.jpg")
img2 = ImageTk.PhotoImage(img1)
warriorImg = Image.open("fighter.jpg")
warriorImg2 = ImageTk.PhotoImage(warriorImg)
wizardImg = Image.open("wizard.png")
wizardImg2 = ImageTk.PhotoImage(wizardImg)
rangerImg = Image.open("ranger.jpg")
rangerImg2 = ImageTk.PhotoImage(rangerImg)
label1 = Label(newWindow, image = wizardImg2)
label1.pack(side = RIGHT)
label2 = Label(newWindow, image = warriorImg2)
label2.pack(side = RIGHT)
label3 = Label(newWindow, image = rangerImg2)
label3.pack(side = RIGHT)
wizardDoorCount = 4
button1 = Button(newWindow, text = "WIZARD", command = WizardDoor)
button1.pack(side = BOTTOM)
button2 = Button(newWindow, text = "WARRIOR", command = WarriorDoor)
button2.pack(side = BOTTOM)
button3 = Button(newWindow, text = "RANGER", command = RangerDoor)
button3.pack(side = BOTTOM)
