from random import randint
from sys import argv
from rich import print
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
    Space("At any rate, life is hard [red]-150[/red] points",-150),
    Space("Naturally attractive [green]+200[/green] points",200),
    Space("Deodorant spray ran out [yellow]-50[/yellow] points",-50),
    Space("Hayasaka cleans the room [green]+100[/green] points",100),
    Space("The clothes you bought don't suit you [yellow]-80[/yellow] points",-80),
    Space("Recive a rice cracker from Igarashi-san [green]+100[/green]",100),
    Space("The toilet broke [red]-120[/red] points",-120),
    Space("Go back to sleep [green]+200[/green] points",-200),
    Space("Orie praises your voice [green]+100[/green] points",100),
    Space("Save money for food [cyan]+80[/cyan] points",80),
    Space("Pay for Yasuda's living expenses [red]-500[/red] points",-500),
    Space("You've been doxed on social media [red]-140[/red] points",-140),
    Space("You get woken up on a day off [red]-200[/red] points",-200),
    Space("Several hot days in a row [yellow]-70[/yellow] points",-70),
    Space("Sugimura pays for you [green]+100[/green] points",100),
    Space("Everyone respects you in class [green]+120[/green] points",120),
    Space("Sucking up tapioca balls is so tiring [yellow]-50[/yellow] points",-50),
    Space("You're victorious in a ball sports tournament [green]+200[/green] points",200),
    Space("A manga you borrowed was interesting [cyan]+80[/cyan] points",80),
    Space("Work [red]-250[/red] points",-250),
    Space("You wake up as a girl one morning [white]±0[/white] points",0),
    Space("[bold blink]GOAL![/bold blink]",0)]

#Test that board was created properly
'''
for space in board:
    print(space.getText() + " : " + str(space.getValue()))
'''

def rollDice():
    die = randint(1,6)
    if die == 1:
        print("[bold]\u2680[/bold]")
    elif die == 2:
        print("[bold]\u2681[/bold]")
    elif die == 3:
        print("[bold]\u2682[/bold]")
    elif die == 4:
        print("[bold]\u2683[/bold]")
    elif die == 5:
        print("[bold]\u2684[/bold]")
    elif die == 6:
        print("[bold]\u2685[/bold]")
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
                print("\n[bold]%s[/bold] press a key to roll the dice" % player.getName())
                getch()
            else:
                input("\n[bold]%s[/bold] press ENTER to roll the dice" % player.getName())
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
                    print("[bold blink]GOAL![/bold blink]")
                    player.finished()

ranking = sorted(players, key=lambda player: player.getScore(), reverse=True)
print("\n---------------------------------------------------")
for p in ranking:
    score = p.getScore()
    if score <= -100:
        print("[bold]%s[/bold]: [red]%d[/red]" % (p.getName(), score))
    elif score < 0:
        print("[bold]%s[/bold]: [yellow]%d[/yellow]" % (p.getName(), score))
    elif score < 100:
        print("[bold]%s[/bold]: [cyan]%d[/cyan]" % (p.getName(), score))
    elif score >= 100:
        print("[bold]%s[/bold]: [green]%d[/green]" % (p.getName(), score))
    else:
        print("[bold]%s[/bold]: %d" % (p.getName(), score))
