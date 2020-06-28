from random import randint

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
    return randint(1,6)

class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0
    def getName(self):
        return self.name
    def getScore(self):
        return self.score
    def updateScore(self, points):
        self.score = self.score + points

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