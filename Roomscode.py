randomArray = [1,2,3,4,5,6,7,8]


def ChoiceUpdate():
    
    
    numberOfDoors1 = numberOfTimesDecremented

    global numberOfDoors2
    numberOfDoors2 = numberOfDoors1  - 1

    
    randomNumber = random.choice(randomArray)

    if randomNumber == 1:
        messagebox.showinfo("Fire robe top is checked")
        frame.pack_forget()
        randomArray.remove(randomNumber)
        fireTop()
    if randomNumber == 2:
        messagebox.showinfo("Fire robe bottom is checked")
        frame.pack_forget()
        randomArray.remove(randomNumber)
        fireBottom()
    if randomNumber == 3:
        messagebox.showinfo("Water robe top is checked")
        frame.pack_forget()
        randomArray.remove(randomNumber)
        waterTop()
    if randomNumber == 4:
        messagebox.showinfo("Water robe bottom is checked")
        frame.pack_forget()
        randomArray.remove(randomNumber)
        waterBottom()
    if randomNumber == 5:
        messagebox.showinfo("Fire staff is checked"")
        frame.pack_forget()
        randomArray.remove(randomNumber)
        fireStaff()
    if randomNumber == 6:
        messagebox.showinfo("Water staff is checked")
        frame.pack_forget()
        randomArray.remove(randomNumber)
        waterStaff()
    if randomNumber == 7:
        messagebox.showinfo("Water hat  is checked")
        frame.pack_forget()
        randomArray.remove(randomNumber)
        waterHat()
    if randomNumber == 8:
        messagebox.showinfo("Fire hat is checked")
        frame.pack_forget()
        randomArray.remove(randomNumber)
        fireHat()
