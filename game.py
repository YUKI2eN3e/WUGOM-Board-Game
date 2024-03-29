from random import randint
from sys import argv
from platform import system
if system() == "Windows":
    from msvcrt import getch

mode = ""
try:
    arg = argv[1].lower()
    arg = arg.replace("-","")
    if arg == "l" or arg == "long":
        mode = "LONG"
    elif arg == "s" or arg == "short":
        mode = "SHORT"
except:
    mode = input("Do you want to play Long or Short mode> ").upper()
if mode == "L":
    mode = "LONG"
elif mode == "S":
    mode = "SHORT"
#Test mode set correctly
#print(mode)

class Space:
    def __init__(self, text, value):
        self.text = text
        self.value = value
    def getText(self):
        return self.text
    def getValue(self):
        return self.value
    

board = [Space("START!",0),
    Space("At any rate, life is hard -150 points",-150),
    Space("Naturally attractive +200 points",200),
    Space("Deodorant spray ran out -50 points",-50),
    Space("Hayasaka cleans the room +100 points",100),
    Space("The clothes you bought don't suit you -80 points",-80),
    Space("Recive a rice cracker from Igarashi-san +100",100),
    Space("The toilet broke -120 points",-120),
    Space("Go back to sleep +200 points",-200),
    Space("Orie praises your voice +100 points",100),
    Space("Save money for food +80 points",80),
    Space("Pay for Yasuda's living expenses -500 points",-500),
    Space("You've been doxed on social media -140 points",-140),
    Space("You get woken up on a day off -200 points",-200),
    Space("Several hot days in a row -70 points",-70),
    Space("Sugimura pays for you +100 points",100),
    Space("Everyone respects you in class +120 points",120),
    Space("Sucking up tapioca balls is so tiring -50 points",-50),
    Space("You're victorious in a ball sports tournament +200 points",200),
    Space("A manga you borrowed was interesting +80 points",80),
    Space("Work -250 points",-250),
    Space("You wake up as a girl one morning ±0 points",0),
    Space("GOAL!",0)]

#Test that board was created properly
'''
for space in board:
    print(space.getText() + " : " + str(space.getValue()))
'''

def rollDice():
    die = randint(1,6)
    if die == 1:
        print("\u2680")
    elif die == 2:
        print("\u2681")
    elif die == 3:
        print("\u2682")
    elif die == 4:
        print("\u2683")
    elif die == 5:
        print("\u2684")
    elif die == 6:
        print("\u2685")
    return die

class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.position = 0
        self.playing = True
    def getName(self):
        return self.name
    def getScore(self):
        return self.score
    def updateScore(self, points):
        self.score = self.score + points
    def getPosition(self):
        return self.position
    def updatePosition(self, position):
        self.position = position
    def isPlaying(self):
        return self.playing
    def finished(self):
        self.playing = False

num_players = int(input("How many players are there> "))
players = []
p = 0
while p < num_players:
    name = input("Player %d enter your name> " % (p+1))
    players.append(Player(name))
    p += 1

#Test players have been created
'''
for player in players:
    print(player.getName() + " : " + str(player.getScore()))
'''

def isPlaying():
    for player in players:
        if player.isPlaying():
            return True

while isPlaying():
    for player in players:
        if player.isPlaying():
            if system() == "Windows":
                print("\n%s press a key to roll the dice" % player.getName())
                getch()
            else:
                input("\n%s press ENTER to roll the dice" % player.getName())
            die = rollDice()
            if mode == "LONG":
                if player.getPosition() + die <= len(board)-1:
                    player.updatePosition(player.getPosition()+die)
                    print(board[player.getPosition()].getText())
                    player.updateScore(board[player.getPosition()].getValue())
                    if player.getPosition() == len(board)-1:
                        #print("GOAL!")
                        player.finished()
                elif player.getPosition() + die > len(board)-1:
                    player.updatePosition((player.getPosition()+die) - len(board))
                    print(board[player.getPosition()].getText())
                    player.updateScore(board[player.getPosition()].getValue())
            if mode == "SHORT":
                if player.getPosition() + die < len(board)-1:
                    player.updatePosition(player.getPosition()+die)
                    print(board[player.getPosition()].getText())
                    player.updateScore(board[player.getPosition()].getValue())
                else:
                    print("GOAL!")
                    player.finished()

ranking = sorted(players, key=lambda player: player.getScore(), reverse=True)
print("\n---------------------------------------------------")
for p in ranking:
    print("%s: %d" % (p.getName(), p.getScore()))
