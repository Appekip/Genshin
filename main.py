import random
import tkinter
from tkinter import *

#Variables used with the old while loop
#state = False
#wishes= int(input("How many wishes do you want to do? \nType here: "))

threeStarPool = []
fourStarPool = []
fourStarRateUpPool = []
fiveStarPool = []
fiveStarRateUpPool = []

class player:
        wishCounter = 0
        pityCounter = 0
        fourStarPityCounter = 0
        threeStarCounter = 0
        fourStarCounter = 0
        fiveStarCounter = 0
        outOfPityFives = 0
        outOfPityFours = 0
        rateUpPityFour = 0
        rateUpPityFive = 0
        dropHistory = []

#Drops class
class gachaDrop:
    def __init__(self, n, t, r, ru):
        self.name = n
        self.type = t
        self.rarity = r
        self.rateUp = ru

def generateThrees():

    threeStarPool.append(gachaDrop("Slingshot", "Weapon", "Three Stars ***", False))
    threeStarPool.append(gachaDrop("Raven Bow", "Weapon", "Three Stars ***", False))
    threeStarPool.append(gachaDrop("Thirilling Tales", "Weapon", "Three Stars ***", False))
    threeStarPool.append(gachaDrop("Black Tassel", "Weapon", "Three Stars ***", False))
    threeStarPool.append(gachaDrop("Bloodtainted Greatsword", "Weapon", "Three Stars ***", False))
    threeStarPool.append(gachaDrop("Skyrider Sword", "Weapon", "Three Stars ***", False))
    threeStarPool.append(gachaDrop("Cool Steel", "Weapon", "Three Stars ***", False))
    threeStarPool.append(gachaDrop("Sharpshooter's Oath", "Weapon", "Three Stars ***", False))
    threeStarPool.append(gachaDrop("Emerald Orb", "Weapon", "Three Stars ***", False))
    threeStarPool.append(gachaDrop("Magic Guide", "Weapon", "Three Stars ***", False))
    threeStarPool.append(gachaDrop("Debate Club", "Weapon", "Three Stars ***", False))
    threeStarPool.append(gachaDrop("Ferrous Shadow", "Weapon", "Three Stars ***", False))
    threeStarPool.append(gachaDrop("Harbinger of Dawn", "Weapon", "Three Stars ***", False))

def generateFours():
    fourStarRateUpPool.append(gachaDrop("Candace", "Character", "Four Stars ****", True))
    fourStarRateUpPool.append(gachaDrop("Kuki Shinobu", "Character", "Four Stars ****", True))
    fourStarRateUpPool.append(gachaDrop("Sayu", "Character", "Four Stars ****",True))

    fourStarPool.append(gachaDrop("Candace", "Character", "Four Stars ****", True))
    fourStarPool.append(gachaDrop("Kuki Shinobu", "Character", "Four Stars ****", True))
    fourStarPool.append(gachaDrop("Sayu", "Character", "Four Stars ****", True))
    fourStarPool.append(gachaDrop("Collei", "Character", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Dori", "Character", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Yun Jin", "Character", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Shikanoin Heizou", "Character", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Kujou Sara", "Character", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Gorou", "Character", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Thoma", "Character", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Yanfei", "Character", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Rosaria", "Character", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Xinyan", "Character", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Diona", "Character", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Sucrose", "Character", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Chongyun", "Character", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Noelle", "Character", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Bennet", "Character", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Fischl", "Character", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Ningguang", "Character", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Xinqiu", "Character", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Beidou", "Character", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Xiangling", "Character", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Razor", "Character", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Barbara", "Character", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Rust", "Weapon", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Favonius Warbow", "Weapon", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Eye of Perception", "Weapon", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Sacrificial Fragments", "Weapon", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("The Widsith", "Weapon", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Favounius Codex", "Weapon", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Favounius Lance", "Weapon", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Dragon's Bane", "Weapon", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Rainslasher", "Weapon", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Sacrificial Greatsword", "Weapon", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("The Bell", "Weapon", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Lion's Roar", "Weapon", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Sacrificial Sword", "Weapon", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("The Flute", "Weapon", "Four Stars ****",False))
    fourStarPool.append(gachaDrop("Favounius Sword", "Weapon", "Four Stars ****",False))

def generateFives():
    fiveStarRateUpPool.append(gachaDrop("Cyno", "Character", "Five Stars *****", True))

    fiveStarPool.append(gachaDrop("Cyno", "Character", "Five Stars *****", True))
    fiveStarPool.append(gachaDrop("Keqing", "Character", "Five Stars *****",False))
    fiveStarPool.append(gachaDrop("Diluc", "Character", "Five Stars *****",False))
    fiveStarPool.append(gachaDrop("Qiqi", "Character", "Five Stars *****",False))
    fiveStarPool.append(gachaDrop("Jean", "Character", "Five Stars *****",False))
    fiveStarPool.append(gachaDrop("Mona", "Character", "Five Stars *****",False))
    fiveStarPool.append(gachaDrop("Tighnari", "Character", "Five Stars *****",False))

def generateDrops():
    #Should only happen once per run!!!
        print("Generating drops")
        generateThrees()
        generateFours()
        generateFives()

def pityCheck():
    if player.pityCounter == 89:
        return True
    else:return False

def fourStarPityCheck():
    if player.fourStarPityCounter == 9:
        return True
    else:return False

def gachaPull():
    fiftyfifty = random.randint(0,1)
    player.wishCounter += 1
    player.pityCounter += 1
    player.fourStarPityCounter +=1
    drop = random.randint(0, 599)
    print(drop, "was the random number")
    print("Number of wishes done", player.wishCounter)

    if pityCheck():
        print("Wish happens, pity at ", player.pityCounter)
        print("-----------Pity 5 star happens--------------\n Wishes at, ", player.wishCounter)
        if player.rateUpPityFive != 0:
            player.dropHistory.append(fiveStarRateUpPool[0])
            player.rateUpPityFive = 0
            player.pityCounter = 0
            player.fourStarPityCounter = 0
            addText(fiveStarRateUpPool[0])
            player.fiveStarCounter +=1
        else:
            if fiftyfifty == 0:
                player.dropHistory.append(fiveStarRateUpPool[0])
                player.rateUpPityFive = 0
                player.rateUpPityFour = 0
                player.pityCounter = 0
                player.fourStarPityCounter = 0
                addText(fiveStarRateUpPool[0])
                player.fiveStarCounter +=1
            else:
                r = random.randint(0, 6)
                player.dropHistory.append(fiveStarPool[r])
                player.rateUpPityFive = 1
                player.pityCounter = 0
                player.fourStarPityCounter = 0
                addText(fiveStarPool[r])
                player.fiveStarCounter +=1
        return
    elif fourStarPityCheck():
        print("Wish happens, pity at ", player.fourStarPityCounter)
        print("----Pity 4 star happens----")
        if player.rateUpPityFour != 0:
            print("Rate Up")
            r = random.randint(0, 2)
            player.dropHistory.append(fourStarRateUpPool[r])
            player.rateUpPityFour = 0
            player.fourStarPityCounter = 0
            addText(fourStarRateUpPool[r])
            player.fourStarCounter +=1
        else:
            if fiftyfifty == 0:
                r = random.randint (0, 2)
                player.dropHistory.append(fourStarRateUpPool[r])
                player.rateUpPityFour = 0
                player.fourStarPityCounter = 0
                addText(fourStarRateUpPool[r])
                player.fourStarCounter +=1
            else:
                r = random.randint(0, 39)
                player.dropHistory.append(fourStarPool[r])
                player.rateUpPityFour = 1
                player.fourStarPityCounter = 0
                addText(fourStarPool[r])
                player.fourStarCounter +=1

        return
    else:print("Wish happens, pity at ", player.pityCounter)
    if drop <= 5:

        if player.rateUpPityFive != 0:
                print("-----Rate Up Pity Five Star-----")
                player.dropHistory.append(fiveStarRateUpPool[0])
                player.rateUpPityFive = 0
                player.pityCounter = 0
                player.fourStarPityCounter = 0
                addText(fiveStarRateUpPool[0])
                player.fiveStarCounter +=1
                player.outOfPityFives +=1
        else:
                print("-----Wow a FIVE STAR-----")
                r = random.randint(0,6)
                player.dropHistory.append(fiveStarPool[r])
                player.rateUpPityFive = True
                player.pityCounter = 0
                player.fourStarPityCounter = 0
                addText(fiveStarPool[r])
                player.fiveStarCounter +=1
                player.outOfPityFives +=1
    elif drop >= 569:

        if player.rateUpPityFour == True:
            print("-----Rate Up Pity Four Star-----")
            r = random.randint(0, 2)
            player.dropHistory.append(fourStarRateUpPool[r])
            player.rateUpPityFour = False
            addText(fourStarRateUpPool[r])
            player.fourStarCounter +=1
            player.outOfPityFours +=1
        else:
            print("----Wow a FOUR STAR----")
            r = random.randint(0, 39)
            player.dropHistory.append(fourStarPool[r])
            player.rateUpPityFour = True
            addText(fourStarPool[r])
            player.fourStarCounter +=1
            player.outOfPityFours +=1
    else:
        r = random.randint(0, 12)
        player.dropHistory.append((threeStarPool[r]))
        print("Just a", threeStarPool[r].name, " meh")
        addText(threeStarPool[r])
        player.threeStarCounter +=1

def printOut():
    print("\nIn total", player.wishCounter, "wishes done.", "\nFive Star pity's at:",player.pityCounter,"\nFour Star pity's at:", player.fourStarPityCounter, "\n\n-----All wishes-----")
    for x in player.dropHistory:
        print(x.name,",", x.type, ", Rarity:",x.rarity)

def printOut4():
    print("\nIn total", player.wishCounter, "wishes done.", "\nFive Star pity's at:", player.pityCounter,
          "\nFour Star pity's at:", player.fourStarPityCounter, "\n\n-----All wishes-----")
    for x in player.dropHistory:
        if x.rarity == "Five Stars *****" or x.rarity == "Four Stars ****":
            print(x.name, ",", x.type, ", Rarity ,", x.rarity)
    else:
        return

def printOut5():
    print("\nIn total", player.wishCounter, "wishes done.", "\nFive Star pity's at:", player.pityCounter,
          "\nFour Star pity's at:", player.fourStarPityCounter, "\n\n-----All wishes-----")
    for x in player.dropHistory:
        if x.rarity == "Five Stars *****":
            return(x.name, ",", x.type, ", Rarity ,", x.rarity)
    else:
        return

def gachaPullTen():
    for x in range (0, 10):
        gachaPull()

def gachaPullNine():
    for x in range (0, 90):
        gachaPull()

def addText(te):
    T.insert(END, te.name + " ")
    T.insert(END, te.type + " ")
    T.insert(END, te.rarity + "\n")

def histPrint():
    T.delete('1.0', END)
    for x in player.dropHistory:
        T.insert(END, x.name + " ")
        T.insert(END, x.type + " ")
        T.insert(END, x.rarity + "\n")

def histPrintFours():
    T.delete('1.0', END)
    for x in player.dropHistory:
        if x.rarity == "Four Stars ****":
            T.insert(END, x.name + " ")
            T.insert(END, x.type + " ")
            T.insert(END, x.rarity + "\n")
    else:
        return

def histPrintFives():
    T.delete('1.0', END)
    for x in player.dropHistory:
        if x.rarity == "Five Stars *****":
            T.insert(END, x.name + " ")
            T.insert(END, x.type + " ")
            T.insert(END, x.rarity + "\n")
    else:
        return

def clearText():
    T.delete('1.0', END)

def statPrint():
    T.delete('1.0', END)
    T.insert(END, player.wishCounter)
    T.insert(END, " Wishes done\n")
    T.insert(END, player.fiveStarCounter)
    T.insert(END, " Five Stars pulled ")
    T.insert(END, player.outOfPityFives)
    T.insert(END, " were out of Pity\n")
    T.insert(END, player.fourStarCounter)
    T.insert(END, " Four Stars pulled ")
    T.insert(END, player.outOfPityFours)
    T.insert(END, " were out of Pity\n")
    T.insert(END, player.threeStarCounter)
    T.insert(END, " Three stars pulled\n")
    T.insert(END, "Five star pity at: ")
    T.insert(END, player.pityCounter)

    if player.rateUpPityFive != 0:
        T.insert(END, "\nNext Five star will be a rate UP!")
    else:
        return

def clearHistory():
    player.dropHistory.clear()
    player.wishCounter = 0
    player.pityCounter = 0
    player.fourStarPityCounter = 0
    player.threeStarCounter = 0
    player.fourStarCounter = 0
    player.fiveStarCounter = 0
    player.outOfPityFives = 0
    player.outOfPityFours = 0
    player.rateUpPityFour = 0
    player.rateUpPityFive = 0

def printCharaDupes():
    T.delete('1.0', END)

generateDrops()

root = Tk()

bg = "#301934"

root.title("Genshin Gacha Simulator")

root.geometry("1280x720")

root.configure(bg=bg)

canvasLeft = tkinter.Canvas(root, bg=bg, highlightthickness=0)
canvasLeft.pack(side=tkinter.LEFT, pady=20)

canvas = tkinter.Canvas(canvasLeft, bg=bg, highlightthickness=0)
canvas.pack(pady=5)

title = Label(canvas, text="Genshin Simulator", font=("Arial", 25),bg=bg, bd=0,fg="white")
title.pack(pady=5)

wishBtn = tkinter.Button(canvas, text="Wish X 1", bg="#ADD8E6", command=gachaPull, font=("Arial", 15))
wishBtn.pack(pady=5, side=tkinter.LEFT)

wishBtn10 = tkinter.Button(canvas, text="Wish X 10", bg="#ADD8E6", command=gachaPullTen, font=("Arial", 15))
wishBtn10.pack(pady=5, side=tkinter.LEFT)

wishBtn90 = tkinter.Button(canvas, text="Wish X 90", bg="#ADD8E6", command=gachaPullNine, font=("Arial", 15))
wishBtn90.pack(pady=5, side=tkinter.LEFT)

canvas2 = tkinter.Canvas(canvasLeft, bg=bg, highlightthickness=0)
canvas2.pack(pady=5)

histBtn = tkinter.Button(canvas2, text="Full history", bg="#ADD8E6", command=histPrint, font=("Arial", 15))
histBtn.pack(pady=5, side=tkinter.RIGHT)

histBtn4 = tkinter.Button(canvas2, text="4 Star History", bg="#ADD8E6", command=histPrintFours, font=("Arial", 15))
histBtn4.pack(pady=5, side=tkinter.RIGHT)

histBtn5 = tkinter.Button(canvas2, text="5 Star History", bg="#ADD8E6", command=histPrintFives, font=("Arial", 15))
histBtn5.pack(pady=5, side=tkinter.RIGHT)

canvas3 = tkinter.Canvas(root, bg=bg, highlightthickness=0)
canvas3.pack(pady=5)

historyLabel = Label(canvas3, text="Whishes", font=("Arial", 25),bg=bg, bd=0,fg="white")
historyLabel.pack(pady=5)

clearBtn = tkinter.Button(canvas3, text="Clear Text", font=("Arial", 15), bg="#ADD8E6", command=clearText)
clearBtn.pack(pady=5, side=tkinter.RIGHT)

statsBtn = tkinter.Button(canvas3, text="Statistics", font=("Arial", 15), bg="#ADD8E6", command=statPrint)
statsBtn.pack(pady=5, side=tkinter.LEFT)

statClearBtn = tkinter.Button(canvas3, text="Reset all", font=("Arial", 15), bg="#ADD8E6", command=clearHistory)
statClearBtn.pack(pady=5, side=tkinter.RIGHT)

canvas4 = tkinter.Canvas(root, bg=bg, highlightthickness=0)
canvas4.pack(pady=5)

T = tkinter.Text(canvas4, height=100, width=100)

T.pack()

photo = PhotoImage(file="Genshin_SimuRezizd.gif")

photoLabel = Label(canvasLeft,image=photo)

photoLabel.pack(pady=5)

root.mainloop()

#Not in use anymore, just an old leftover from a text based console gui
#while (state):

 #   if player.wishCounter < wishes:
      #  gachaPull()
  #  else:
   #     print("\n \nWhat do you want to do next?\n Type 1 to continue:\n Type 2 to print your Wish history: \n Type 3 To only print 4 and 5 Star history: \n Type 4 to only print 5 Star history: \n Type 5 to exit:")
    #    d = int(input(" Type here: "))
     #   if d == 1:
      #      resume = int(input("Input the number of wishes you want to do. "))
       #     wishes = wishes + resume
        #elif d == 2:
         #   printOut()
        #elif d == 3:
         #   printOut4()
        #elif d == 4:
         #   printOut5()
        #elif d == 5:
         #   state = False







