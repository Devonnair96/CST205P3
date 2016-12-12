from tkinter import *
import time
from tkinter import messagebox
import random
import smtplib
import getpass
import pyaudio
import winsound
import sys
from PIL import ImageTk, Image
gold = 500
def gameOver():
    frame4.pack_forget()
    frame5 = Frame(newWindow)
    frame5.pack()
    global dragonHealth,playerHealth, turnNumber
    win = "Congratulations! You defeated the dragon!"
    lose = "The dragon burnt you to a crisp and ate you"
    if (dragonHealth <= 0):
        gLabel = Label(frame5, text = win)
    if (playerHealth <= 0):
        gLabel = Label(frame5, text = lose)
    gLabel.grid(row = 1)
    emailLabel = Label(frame5, text = "Enter your email if you want the results of your adventure")
    emailLabel.grid(row = 2)
    myemail = StringVar()
    global entry
    entry = Entry(frame5, textvariable = myemail)
    entry.grid(row = 2, column = 1)
    sendButton = Button(frame5, text = "Send Email", command = sendEmail)
    sendButton.grid(row = 1, column =1)
def sendEmail():
    global head, chest, legs, weapon, userEmail, turnNumber, playerHealth, dragonHealth, userEmail, entry
    userEmail = entry.get()
    emailText = ""
    turnText= str(turnNumber)
    if(dragonHealth <= 0):
        emailText = "Congratulations on beating the dragon! In order to defeat the dragon, you used your " + weapon + ". You were wearing the " + head + ", the " + chest + ", and the " + legs + ". You defeated the dragon in " + turnText + " turns . Thanks for playing!"
    if(playerHealth <= 0):
        emailText = "The dragon bested you this time. Your " + weapon + " was unable to save you. You were wearing the " + head + ", the " + chest + ", and the " + legs + " before the dragon burnt them all to ash. The dragon defeated you in " + turnText + " turns. Thanks for playing!"
    if (userEmail != ""):
        try:
                gameserver  =  smtplib.SMTP('smtp.gmail.com',587)
                gameserver.ehlo()
                gameserver.starttls()
                password = getpass.getpass("Enter your password: ")
                gameserver.login( userEmail, password) # the user sends the results to themselves
                gameserver.sendmail( userEmail, userEmail, emailText) 
                gameserver.quit()
        except:
                print("There was a problem")
                
def bossFight():
    frame3.pack_forget()
    goldLabel.pack_forget()
    global frame4
    frame4 = Frame(newWindow)
    frame4.pack()
    dragonImage = Image.open("blueEyes.png")
    dragonImage2 = ImageTk.PhotoImage(dragonImage)
    dragonLabel = Label(frame4, image = dragonImage2)
    dragonLabel.image = dragonImage2
    dragonLabel.grid(row = 0, columnspan = 4)
    global playerHealth, dragonHealth, actionPoints, turnNumber
    playerHealth = 100
    dragonHealth = 200
    actionPoints = 10
    turnNumber = 1
    global healthAmt, healthLabel
    healthAmt = StringVar()
    healthAmt.set("Health: " + str(playerHealth))
    healthLabel = Label(frame4, textvariable = healthAmt)
    healthLabel.grid(row = 1)
    global apAmt, apLabel
    apAmt = StringVar()
    apAmt.set("Action Points: " + str(actionPoints))
    apLabel = Label(frame4, textvariable = apAmt)
    apLabel.grid(row =1, column =1)
    global dHealthAmt, dHealthLabel
    dHealthAmt = StringVar()
    dHealthAmt.set("Dragon Health: " + str(dragonHealth))
    dHealthLabel = Label(frame4, textvariable = dHealthAmt)
    dHealthLabel.grid(row=1, column = 3)
    global turnCount, turnLabel
    turnCount = StringVar()
    turnCount.set("Turn Number: " + str(turnNumber))
    turnLabel = Label(frame4, textvariable = turnCount)
    turnLabel.grid(row = 1, column = 2)
    wAttack = Button(frame4, text = "Weak Attack", command = weakAttack)
    wAttack.grid(row = 2)
    sAttack = Button(frame4, text = "Strong Attack", command = strongAttack)
    sAttack.grid(row = 2, column = 1)
    spAttack = Button(frame4, text = "Special Attack", command = specialAttack)
    spAttack.grid(row = 2, column = 2)
    dodge = Button(frame4, text = "Dodge", command = dodging)
    dodge.grid(row = 2, column = 3)
    
def dragonAttack():
    global head, chest, legs, playerHealth, healthAmt, healthLabel
    defenseBonus = 0
    if(head == "Enchanted Hat" or head == "Enchanted Helm" or head == "Fire Hat"):
        defenseBonus = defenseBonus + 1
    if(legs == "Enchanted Pants" or legs == "Enchanted Leggings" or legs == "Fire Pants"):
        defenseBonus = defenseBonus + 1
    if(chest == "Enchanted Shirt" or chest == "Enchanted Chestplate" or chest == "FireShirt"):
        defenseBonus = defenseBonus + 2
    dAttack = [1,2,3,4]
    randomAttack = random.choice(dAttack)
    if (randomAttack == 1 or randomAttack == 4):
        playerHealth = playerHealth - (10 - ( 2 * defenseBonus))
        messagebox.showinfo("Tail Attack!", "The dragon swipes at you with it's mighty tail!")
    if (randomAttack == 2):
        playerHealth = playerHealth - (14 - ( 3 * defenseBonus))
        messagebox.showinfo("Claw Attack!", "The dragon swipes you with its claws!")                               
    if (randomAttack == 3):
        playerHealth = playerHealth - (20 - ( 4 * defenseBonus))
        messagebox.showinfo("Fire Attack!", "The dragon breathes its flames at you!")  
    healthAmt.set("Health: " + str(playerHealth))
    healthLabel = Label(frame4, textvariable = healthAmt)
    if(playerHealth <=0):
        gameOver()
def weakAttack():
    global dragonHealth,frame4,dHealthLabel,dHealthAmt, weapon, turnNumber, turnCount, turnLabel
    attackBonus = 1
    if(weapon == "Enchanted Bow" or weapon == "Enchanted Sword" or weapon == "waterstaff"):
        attackBonus = 1.25
    dragonHealth = dragonHealth - (8 * attackBonus)
    messagebox.showinfo( "Weak Attack", "You hit the dragon using your " + weapon)
    dHealthAmt.set("Dragon Health: " + str(dragonHealth))
    dHealthLabel = Label(frame4, textvariable = dHealthAmt)
    if (dragonHealth <= 0):
        gameOver()
    else:
        dragonAttack()
    turnNumber = turnNumber + 1
    turnCount.set("Turn Number: " + str(turnNumber))
    turnLabel = Label(frame4, textvariable = turnCount)
    frame4.update_idletasks()
def strongAttack():
    global dragonHealth,frame4,dHealthLabel,dHealthAmt, weapon, actionPoints, apAmt, apLabel, turnNumber, turnCount, turnLabel
    attackBonus = 1
    if(weapon == "Enchanted Bow" or weapon == "Enchanted Sword" or weapon == "waterstaff"):
        attackBonus = 1.25
    if(actionPoints == 0):
        messagebox.showinfo("You missed!","You used too much of your stamina and the dragon easily dodged")
    if (actionPoints > 0):
        dragonHealth = dragonHealth - (20 * attackBonus)
        actionPoints = actionPoints - 2.5
        messagebox.showinfo( "Strong Attack", "You prepare yourself and hit the dragon with a mighty blow using your " + weapon)
    dHealthAmt.set("Dragon Health: " + str(dragonHealth))
    dHealthLabel = Label(frame4, textvariable = dHealthAmt)
    apAmt.set("Action Points: " + str(actionPoints))
    apLabel = Label(frame4, textvariable = apAmt)
    if (dragonHealth <= 0):
        gameOver()
    else:
        dragonAttack()
    turnNumber = turnNumber + 1
    turnCount.set("Turn Number: " + str(turnNumber))
    turnLabel = Label(frame4, textvariable = turnCount)
    frame4.update_idletasks()
def specialAttack():
    global dragonHealth,frame4,dHealthLabel,dHealthAmt, weapon, actionPoints, apAmt, apLabel, turnNumber, turnCount, turnLabel
    attackBonus = 1
    if(weapon == "Enchanted Bow" or weapon == "Enchanted Sword" or weapon == "waterstaff"):
        attackBonus = 1.25
    if(actionPoints == 0):
        messagebox.showinfo("You missed!","You used too much of your stamina and the dragon easily dodged")
    if (actionPoints > 0):
        dragonHealth = dragonHealth - (40 * attackBonus)
        actionPoints = actionPoints - 5
        if (weapon == "Enchanted Bow" or weapon == "Compound Bow"):
            messagebox.showinfo( "Special Attack", "You shoot the dragon in the eye! It roars in agony!")
        if (weapon == "Enchanted Sword" or weapon == "Broadsword"):
            messagebox.showinfo("Special Attack", "You slice off one of the dragons claws! It roars in agony!")
        if (weapon == "waterstaff" or weapon == "firestaff"):
            messagebox.showinfo("Special Attack", "You charge up your power and blast the dragon with your magic! It roars in agony!")
    dHealthAmt.set("Dragon Health: " + str(dragonHealth))
    dHealthLabel = Label(frame4, textvariable = dHealthAmt)
    apAmt.set("Action Points: " + str(actionPoints))
    apLabel = Label(frame4, textvariable = apAmt)
    if (dragonHealth <= 0):
        gameOver()
    else:
        dragonAttack()
    turnNumber = turnNumber + 1
    turnCount.set("Turn Number: " + str(turnNumber))
    turnLabel = Label(frame4, textvariable = turnCount)
    frame4.update_idletasks()
def dodging():
    global dragonHealth,frame4,dHealthLabel,dHealthAmt, turnNumber, turnCount, turnLabel
    dodgeChance = [1,2]
    dodgePercent = random.choice(dodgeChance)
    if (dodgePercent == 1):
        dragonHealth = dragonHealth - 10
        dHealthAmt.set("Dragon Health: " + str(dragonHealth))
        dHealthLabel = Label(frame4, textvariable = dHealthAmt)
        messagebox.showinfo("You dodged!","You dodge out of the way of the dragon's attack and it injures itself")
        if (dragonHealth <= 0):
            gameOver()
    if (dodgePercent == 2):
        messagebox.showinfo("You were hit!","You tried dodging but the dragon hit you with its attack!")
        dragonAttack()
    turnNumber = turnNumber + 1
    turnCount.set("Turn Number: " + str(turnNumber))
    turnLabel = Label(frame4, textvariable = turnCount)
    frame4.update_idletasks()
def showInventory():
    global frame3
    frame3 = Frame(newWindow)
    frame3.pack()
    global head, chest, legs, weapon
    hatBonus = ""
    chestBonus = ""
    legBonus = ""
    weaponBonus = ""
    if(head == "Enchanted Hat" or head == "Enchanted Helm" or head == "Fire Hat"):
        hatBonus = " (+ 25 percent protection)"
    if(chest == "Enchanted Shirt" or chest == "Enchanted Chestplate" or chest == "FireShirt"):
        chestBonus = " (+ 50 percent protection)"
    if(legs == "Enchanted Pants" or legs == "Enchanted Leggings" or legs == "Fire Pants"):
        legBonus = " (+ 25 percent protection)"
    if(weapon == "Enchanted Bow" or weapon == "Enchanted Sword" or weapon == "waterstaff"):
        weaponBonus = " (+ 25 percent damage)"
    hatLabel = Label(frame3, text = "The headwear you chose was the " + head + hatBonus)
    hatLabel.pack(side=TOP)
    chestLabel = Label(frame3, text = "The chestwear you chose was the " + chest + chestBonus)
    chestLabel.pack(side=TOP)
    legLabel = Label(frame3, text = "The legwear you chose was the " + legs + legBonus)
    legLabel.pack(side=TOP)
    weaponLabel = Label(frame3, text = "The weapon you chose was the " + weapon + weaponBonus)
    weaponLabel.pack(side=TOP)
    bossButton = Button(frame3, text = "Ready to fight!", command = bossFight)
    bossButton.pack(side = BOTTOM)
def inventory(item, choose):
    global head, chest, legs, weapon
    if(item == "staff"):
        if(choose == 1):
            winsound.PlaySound('equipitem.wav', winsound.SND_ASYNC)
            weapon = "waterstaff"
        elif(choose == 2):
            winsound.PlaySound('equipitem.wav', winsound.SND_ASYNC)
            weapon = "firestaff"
    if(item == "wiztop"):
        if(choose == 1):
            winsound.PlaySound('equipitem.wav', winsound.SND_ASYNC)
            chest = "FireShirt"
        elif(choose == 2):
            winsound.PlaySound('equipitem.wav', winsound.SND_ASYNC)
            chest = "WaterShirt"
    if(item == "wizhat"):
        if(choose == 1):
            winsound.PlaySound('equipitem.wav', winsound.SND_ASYNC)
            head = "Fire Hat"
        elif(choose == 2):
            winsound.PlaySound('equipitem.wav', winsound.SND_ASYNC)
            head = "Water Hat"
    if(item == "wizlegs"):
        if(choose == 1):
            winsound.PlaySound('equipitem.wav', winsound.SND_ASYNC)
            legs = "Fire Pants"
        elif(choose ==2):
            winsound.PlaySound('equipitem.wav', winsound.SND_ASYNC)
            legs = "Water Pants"
    if(item == "sword"):
        if(choose == 1):
            winsound.PlaySound('equipitem.wav', winsound.SND_ASYNC)
            weapon = "Enchanted Sword"
        elif(choose == 2):
            winsound.PlaySound('equipitem.wav', winsound.SND_ASYNC)
            weapon = "Broadsword"
    if(item == "boots"):
        if(choose == 1):
            winsound.PlaySound('equipitem.wav', winsound.SND_ASYNC)
            legs = "Enchanted Leggings"
        elif(choose == 2):
            winsound.PlaySound('equipitem.wav', winsound.SND_ASYNC)
            legs = "Armored Leggings"
    if(item == "chestplate"):
        if(choose == 1):
            winsound.PlaySound('equipitem.wav', winsound.SND_ASYNC)
            chest = "Enchanted Chestplate"
        elif(choose == 2):
            winsound.PlaySound('equipitem.wav', winsound.SND_ASYNC)
            chest = "Steel Chestplate"
    if(item == "helm"):
        if(choose == 1):
            winsound.PlaySound('equipitem.wav', winsound.SND_ASYNC)
             head = "Enchanted Helm"
        elif(choose == 2):
            winsound.PlaySound('equipitem.wav', winsound.SND_ASYNC)
            head = "Steel Helm"
    if(item == "bow"):
        if(choose == 1):
            winsound.PlaySound('equipitem.wav', winsound.SND_ASYNC)
            weapon = "Enchanted Bow"
        elif(choose == 2):
            winsound.PlaySound('equipitem.wav', winsound.SND_ASYNC)
            weapon = "Compound Bow"
    if(item == "archerhat"):
        if(choose == 1):
            winsound.PlaySound('equipitem.wav', winsound.SND_ASYNC)
            head = "Enchanted Hat"
        elif(choose == 2):
            winsound.PlaySound('equipitem.wav', winsound.SND_ASYNC)
            head = "Archer's Hat"
    if(item == "archerpants"):
        if(choose == 1):
            winsound.PlaySound('equipitem.wav', winsound.SND_ASYNC)
            legs = "Enchanted Pants"
        elif(choose == 2):
            winsound.PlaySound('equipitem.wav', winsound.SND_ASYNC)
            legs = "Archer's Pants"
    if(item == "archershirt"):
        if(choose == 1):
            winsound.PlaySound('equipitem.wav', winsound.SND_ASYNC)
            chest = "Enchanted Shirt"
        elif(choose == 2):
            winsound.PlaySound('equipitem.wav', winsound.SND_ASYNC)
            chest = "Archer's Shirt"

def resetGold(item, choose):
    spentGold()
    reset(item, choose)
def spentGold():
    global gold
    gold = gold - 250
def ClearScreen():
    button1.destroy()
    button2.destroy()
    button3.destroy()
def reset(itemchosen, choose):
    goldLabel.destroy()
    frame2.pack_forget()
    inventory(itemchosen, choose)
    if (numberOfDoors2 == 0):
        showInventory()
    if (choice == 1):
        WizardCreateDoors(numberOfDoors2)
    if (choice == 2):
        WarriorCreateDoors(numberOfDoors2)
    if (choice == 3):
        RangerCreateDoors(numberOfDoors2)
def createRooms(item1, item2, itemChoice):
    global frame2
    frame2 = Frame(newWindow)
    frame2.pack()
    pathToImage1 = Image.open(item1)
    pathToImage2 = Image.open(item2)
    photoImage1 = ImageTk.PhotoImage(pathToImage1)
    photoImage2 = ImageTk.PhotoImage(pathToImage2)
    goldLabel.pack(side = TOP)
    selectedItem = itemChoice
    #label1 = Label(frame1,image = photoImage1)
    #label1.image = photoImage1
    #label1.pack(side = RIGHT)
    #label2 = Label(frame1,image= photoImage2)
    #label2.image = photoImage2
    #label2.pack(side = RIGHT)
    if gold >= 250:
        button1 = Button(frame2, image = photoImage1, text = "Gold Price: 250", compound = BOTTOM, command = lambda: resetGold(selectedItem, 1))
        button1.photoImage1 = photoImage1
        button1.pack(side = RIGHT)
    button2 = Button(frame2, image = photoImage2, text = "Gold Price: 0", compound = BOTTOM ,command = lambda: reset(selectedItem, 2))
    button2.photoImage2 = photoImage2
    button2.pack(side = RIGHT)
    #costlabel = Label(frame1, text = "Gold Price: 0")
    #costlabel.pack(side = LEFT)
    #costlabel2 = Label(frame1, text = "Gold Price: 250")
    #costlabel2.pack(side = RIGHT)
chunk = 1024
wf = wave.open('gamemusic.wav', 'rb')
p = pyaudio.PyAudio()

stream = p.open(
    format = p.get_format_from_width(wf.getsampwidth()),
    channels = wf.getnchannels(),
    rate = wf.getframerate(),
    output = True)
data = wf.readframes(chunk)

while data != '':
    stream.write(data)
    data = wf.readframes(chunk)
    
def staffRoom():
    createRooms("waterstaff1.jpg", "fireStaff1.jpg", "staff")
def topRoom():
    createRooms("firetop1.jpg", "waterRobe1.jpg", "wiztop")
def wizardHatRoom():
    createRooms("fireHat1.jpg", "waterHat1.jpg","wizhat")
def bottomRoom():
    createRooms("fireRobe1.jpg", "waterBottom1.jpg","wizlegs")

def swordRoom():
    createRooms("ElementalSword.jpg","MetalSword.jpg","sword")
def legsRoom():
    createRooms("ElementalLegs.jpg","MetalLegs.jpg","boots")
def chestRoom():
    createRooms("ElementalPlate.jpg", "MetalBody.jpg","chestplate")
def helmRoom():
    createRooms("ElementalFullHelm.jpg", "MetalFullHelm.jpg","helm")

def bowRoom():
    createRooms("ElementalBow.jpg", "Bow.jpg","bow")
def RangerHatRoom():
    createRooms("elementalArcherHat.png", "robinHoodHat.jpg","archerhat")
def leggingsRoom():
    createRooms("elementalArcherLegs.png","archerLegs.png","archerpants")
def torsoRoom():
    createRooms("elementalArcherTop.png", "ArcherTop.jpg","archershirt")

randomArray = [1,2,3,4]
randomGold = [1,2,3,4]

def WizardDoorUpdate():
    numberOfDoors1 = numberOfTimesDecremented

    global numberOfDoors2
    numberOfDoors2 = numberOfDoors1  - 1

    randomNumber = random.choice(randomArray)
    goldFind = random.choice(randomGold)

    if randomNumber == 1:
        messagebox.showinfo("Staff","You have entered the staff room")
        if goldFind == 1:
            global gold
            messagebox.showinfo("Gold!!!","You have also found gold in this room")
            gold = gold + 250
        frame.pack_forget()
        randomArray.remove(randomNumber)
        staffRoom()
    if randomNumber == 2:
        messagebox.showinfo("Top","You have entered the top room")
        if goldFind == 1:
            global gold
            messagebox.showinfo("Gold!!!","You have also found gold in this room")
            gold = gold + 250
        frame.pack_forget()
        randomArray.remove(randomNumber)
        topRoom()
    if randomNumber == 3:
        messagebox.showinfo("Bottom","You have entered the bottom room")
        if goldFind == 1:
            global gold
            messagebox.showinfo("Gold!!!","You have also found gold in this room")
            gold = gold + 250
        frame.pack_forget()
        randomArray.remove(randomNumber)
        bottomRoom()
    if randomNumber == 4:
        messagebox.showinfo("Hat","You have entered the hat room")
        if goldFind == 1:
            global gold
            messagebox.showinfo("Gold!!!","You have also found gold in this room")
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
        messagebox.showinfo("Sword","You have entered the sword room")
        winsound.PlaySound('door.wav', winsound.SND_ASYNC)
        if goldFind == 1:
            global gold
            messagebox.showinfo("Gold!!!","You have also found gold in this room")
            winsound.PlaySound('money.wav', winsound.SND_ASYNC)
            gold = gold + 250
        frame.pack_forget()
        randomArray.remove(randomNumber)
        swordRoom()
    if randomNumber == 2:
        messagebox.showinfo("Chest","You have entered the chest room")
        winsound.PlaySound('door.wav', winsound.SND_ASYNC)
        if goldFind == 1:
            global gold
            messagebox.showinfo("Gold!!!","You have also found gold in this room")
            winsound.PlaySound('money.wav', winsound.SND_ASYNC)
            gold = gold + 250
        frame.pack_forget()
        randomArray.remove(randomNumber)
        chestRoom()
    if randomNumber == 3:
        messagebox.showinfo("Leggings","You have entered the leggings room")
        winsound.PlaySound('door.wav', winsound.SND_ASYNC)
        if goldFind == 1:
            global gold
            messagebox.showinfo("Gold!!!","You have also found gold in this room")
            winsound.PlaySound('money.wav', winsound.SND_ASYNC)
            gold = gold + 250
        frame.pack_forget()
        randomArray.remove(randomNumber)
        legsRoom()
    if randomNumber == 4:
        messagebox.showinfo("Helm","You have entered the helm room")
        winsound.PlaySound('door.wav', winsound.SND_ASYNC)
        if goldFind == 1:
            global gold
            messagebox.showinfo("Gold!!!","You have also found gold in this room")
            winsound.PlaySound('money.wav', winsound.SND_ASYNC)
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
        messagebox.showinfo("Bow","You have entered the bow room")
        winsound.PlaySound('door.wav', winsound.SND_ASYNC)
        if goldFind == 1:
            global gold
            messagebox.showinfo("Gold!!!","You have also found gold in this room")
            winsound.PlaySound('money.wav', winsound.SND_ASYNC)
            gold = gold + 250
        frame.pack_forget()
        randomArray.remove(randomNumber)
        bowRoom()
    if randomNumber == 2:
        messagebox.showinfo("Torso","You have entered the shirt room")
        winsound.PlaySound('door.wav', winsound.SND_ASYNC)
        if goldFind == 1:
            global gold
            messagebox.showinfo("Gold!!!","You have also found gold in this room")
            winsound.PlaySound('money.wav', winsound.SND_ASYNC)
            gold = gold + 250
        frame.pack_forget()
        randomArray.remove(randomNumber)
        torsoRoom()
    if randomNumber == 3:
        messagebox.showinfo("Leggings","You have entered the legging's room")
        winsound.PlaySound('door.wav', winsound.SND_ASYNC)
        if goldFind == 1:
            global gold
            messagebox.showinfo("Gold!!!","You have also found gold in this room")
            winsound.PlaySound('money.wav', winsound.SND_ASYNC)
            gold = gold + 250
        frame.pack_forget()
        randomArray.remove(randomNumber)
        leggingsRoom()
    if randomNumber == 4:
        messagebox.showinfo("Hat","You have entered the hat room")
        winsound.PlaySound('door.wav', winsound.SND_ASYNC)
        if goldFind == 1:
            global gold
            messagebox.showinfo("Gold!!!","You have also found gold in this room")
            winsound.PlaySound('money.wav', winsound.SND_ASYNC)
            gold = gold + 250
        frame.pack_forget()
        randomArray.remove(randomNumber)
        RangerHatRoom()

def WizardDoor():
    ClearScreen()
    global choice
    choice = 1
    messagebox.showinfo("wizard door", "You have entered the Wizard door! Choose another door and this will lead you to either the hat door, the top door, the robe door, or the staff door.")
    winsound.PlaySound('door.wav', winsound.SND_ASYNC)
    WizardCreateDoors(4)
def WarriorDoor():
    ClearScreen()
    global choice
    choice = 2
    messagebox.showinfo("warrior door", "You have entered the Warrior door! Choose another door and this will lead you to either the helm door, the chest door, the greaves door, or the sword door.")
    winsound.PlaySound('door.wav', winsound.SND_ASYNC)
    WarriorCreateDoors(4)
def RangerDoor():
    ClearScreen()
    global choice
    choice = 3
    messagebox.showinfo("ranger door", "You have entered the Ranger door! Choose another door and this will lead you to either the hat door, the torso door, the leggings door, or the bow door.")
    winsound.PlaySound('door.wav', winsound.SND_ASYNC)
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
        #labelx = Label(frame, image = img2)
        #labelx.pack(side = RIGHT)
        global wizardButton
        wizardButton = Button(frame, image = img6,command = WizardDoorUpdate)
        wizardButton.img6 = img6
        wizardButton.pack(side = RIGHT)
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
        #labelx = Label(frame, image = img2)
        #labelx.pack(side = RIGHT)
        global warriorButton
        warriorButton = Button(frame, image = img6,command = WarriorDoorUpdate)
        warriorButton.img6 = img6
        warriorButton.pack(side = RIGHT)
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
        #labelx = Label(frame, image = img2)
        #labelx.pack(side = RIGHT)
        global rangerButton
        rangerButton = Button(frame, image = img6, command = RangerDoorUpdate)
        rangerButton.img6 = img6
        rangerButton.pack(side = RIGHT)
        numberOfDoors = numberOfDoors - 1
        numberOfTimesDecremented = numberOfTimesDecremented + 1

newWindow = Tk()
mytext = StringVar()
goldamount = StringVar()
goldamount.set("Gold: " + str(gold))
global goldLabel
messagebox.showinfo("Welcome Adventurer!", "There's a nasty dragon at the end of this dungeon that we need you to clear out. Here is 500 gold, you can buy equipment in the rooms beyond to help you with your battle. Better equipment costs more gold. Good luck and remember, we're all counting on you...")
winsound.PlaySound('money.wav', winsound.SND_ASYNC)
goldLabel = Label(newWindow, textvariable = goldamount)
img1 = Image.open("door5.jpg")
img2 = ImageTk.PhotoImage(img1)
warriorImg = Image.open("fighter.jpg")
warriorImg2 = ImageTk.PhotoImage(warriorImg)
wizardImg = Image.open("wizard.png")
wizardImg2 = ImageTk.PhotoImage(wizardImg)
rangerImg = Image.open("ranger.jpg")
rangerImg2 = ImageTk.PhotoImage(rangerImg)
#label1 = Label(newWindow, image = wizardImg2)
#label1.pack(side = RIGHT)
#label2 = Label(newWindow, image = warriorImg2)
#label2.pack(side = RIGHT)
#label3 = Label(newWindow, image = rangerImg2)
#label3.pack(side = RIGHT)
wizardDoorCount = 4
button1 = Button(newWindow, text = "WIZARD", image = wizardImg2, compound = BOTTOM ,command = WizardDoor)
button1.wizardImg2 = wizardImg2
button1.pack(side = RIGHT)
button2 = Button(newWindow, text = "WARRIOR", image = warriorImg2, compound = BOTTOM, command = WarriorDoor)
button2.warriorImg2 = warriorImg2
button2.pack(side = RIGHT)
button3 = Button(newWindow, text = "RANGER", image = rangerImg2, compound = BOTTOM, command = RangerDoor)
button3.rangerImg2 = rangerImg2
button3.pack(side = RIGHT)

