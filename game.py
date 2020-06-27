class Space:
    def __init__(self, text, value):
        self.text = text
        self.value = value
    def getText(self):
        return self.text
    def getValue(self):
        return self.value
    

board = [Space("Start",0),
    Space("At any rate, life is hard -150 points",-150),
    Space("Naturally attractive +200 points",200),
    Space("Deodorant spray ran out -50 points",-50)]

for space in board:
    print(space.getText() + " : " + str(space.getValue()))