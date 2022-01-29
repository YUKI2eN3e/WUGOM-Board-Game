from rich import print
from rich.console import Console
from rich.table import Table

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

def makeTable(board):
	table = Table(title="WUGOM Board Game", show_header=False, show_lines=True)
	table.add_row("",board[5].getText(),"","",board[0].getText())
	table.add_row(board[6].getText(),"",board[4].getText(),"",board[1].getText())
	table.add_row(board[7].getText(),"","",board[3].getText(),board[2].getText())
	table.add_row("",board[8].getText(),"","","")
	table.add_row(board[9].getText(),"","","","")
	table.add_row("",board[10].getText(),board[11].getText(),board[12].getText(),"")
	table.add_row(board[18].getText(),board[17].getText(),"","",board[13].getText())
	table.add_row(board[19].getText(),board[20].getText(),board[16].getText(),"",board[14].getText())
	table.add_row(board[22].getText(),board[21].getText(),"",board[15].getText(),"")
	return table
console = Console()
console.print(makeTable(board))