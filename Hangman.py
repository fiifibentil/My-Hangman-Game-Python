from graphics import *
import time
#The classes below were created to assist me in drawing the hangman and pole objects of my game.
class Hangman:
    def __init__(self):
        self.center=Point(120,90)
        self.radius=10
    def drawhead(self):
        head=Circle(self.center,self.radius)
        head.draw(win)
    def drawbody(self):
        body=Line(Point(120,101),Point(120,141))
        body.draw(win)
    def drawlefthand(self):
        lefthand=Line(Point(120,102),Point(96,110))
        lefthand.draw(win)
    def drawrighthand(self):
        righthand=Line(Point(120,102),Point(141,110))
        righthand.draw(win)
    def drawleftleg(self):
        leftleg=Line(Point(120,141),Point(99,155))
        leftleg.draw(win)
    def drawrightleg(self):
        rightleg=Line(Point(120,141),Point(140,155))
        rightleg.draw(win)
class Pole:
    def __init__(self):
        self.base=Point(39,171)
        self.height=Point(39,8)
    def drawpoleheight(self):
        height=Line(self.base,self.height)
        height.draw(win)
    def drawpolelength(self):
        length=Line(self.height,Point(120,8))
        length.draw(win)
    def drawrope(self):
        rope=Line(Point(120,8),Point(120,80))
        rope.draw(win)
    def drawpolebase(self):
        base=Line(Point(13,171),Point(70,171))
        base.draw(win)
win=GraphWin('Hangman Game')
hangman=Hangman()
pole=Pole()

#The functions below is used in terminating the game, depending on whether the player wins or loses.
def lostgame():
    time.sleep(0.5)
    win.close()
    print("Game Over")
    print("The word you were trying to guess was '{}' and it is a/an {}".format(word,hint))
    global z
    z=tries
def wingame():
    time.sleep(0.5)
    win.close()
    print("Congratulations!!!! You Won.")
    print("The word you succesfully guessed was '{}' and it is a/an {}".format(word,hint))
    global z
    z=tries

#This portion of the code below is responsible for obtaining a random word from the text file with the help of the randrange function.
from random import *
wordfile=open("words.txt",'r')
wordstring=wordfile.read()
wordlist=wordstring.split('\n')
randomindex=randrange(0,len(wordlist))
line=wordlist[randomindex]
k=line.split(',')
word=k[0]
hint=k[1]
print(hint)
wronguess=0

#The portion of the code below is responsible for displaying the hint and hidden word to the user.
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphList = []
for i in alphabet:
    alphList.append(i)

staticWordList = [] 
dashList = [] 
for i in word:
    staticWordList.append(i)
    dashList.append("-")

def toString(item):
    itemList = ""

    for i in item:
        itemList += i

    return itemList
print(toString(dashList))

tries = 0
wrongs = 0
z=len(word)+99

#This portion of the code is the actual game logic.
#The while loop keeps the game running until the user has reached the maximum number of wrong guesses
while tries < z:
    alreadyGuessed = False
    guess = input("Enter a letter: ").lower()

    if guess not in word:
        alreadyGuessed = True
        wronguess += 1
        

    for i in range(staticWordList.count(guess)):
        guessIndex = staticWordList.index(guess)
        staticWordList[guessIndex] = "*"
        dashList[guessIndex] = guess
#I get an index error whenever the player inputs a letter that has already been guessed, to prevent this i used "try and except"
    try:
        guessAlphIndex = alphList.index(guess)
        alphList[guessAlphIndex] = "&"
    except:
        print("Already guessed")

    alreadyGuessed = False

    print(toString(dashList))

    tries += 1

#This portion of the code below draws the hangman.
    if wronguess==1:
        pole.drawpolebase()
    if wronguess==2:
        pole.drawpoleheight()
    if wronguess==3:
        pole.drawpolelength()
    if wronguess==4:
        pole.drawrope()
    if wronguess==5:
        hangman.drawhead()
    if wronguess==6:
        hangman.drawbody()
    if wronguess==7:
        hangman.drawlefthand()
    if wronguess==8:
        hangman.drawrighthand()
    if wronguess==9:
        hangman.drawleftleg()
    if wronguess==10:
        hangman.drawrightleg()
        lostgame()
    if staticWordList.count('*')==len(word):
        wingame()
