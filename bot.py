from TowerBot.frontend import TowerConfig
from tkinter import *

debug = True


class mainBot:

    @classmethod
    def openTower(self):
        #self.main.withdraw()
        TC = TowerConfig
        TC.configWindow()


    @classmethod
    def openEoW(self):
        pass



    @classmethod
    def mainWindow(self):
        self.main = Tk()

        self.main.title('AoWe Bot')
        self.main.geometry('350x800+100+100')

        title_label = Label(self.main, text="This is an in-working project that's promise to have a bot for each event in the game", wraplength=200, justify=CENTER, width=45, height=5)
        title_label.grid(row=1, column=1, sticky='ew')

        Option_label = Label(self.main, text='Choose what event to bot.', height=7)
        Option_label.grid(column=1, row=3)

        tower_button = Button(self.main, text='Tower Bot', command=self.openTower)
        tower_button.grid(row=4, column=1)

        explotarionofWarrior_button = Button(self.main, text='Exploration of Warrior', command=self.openEoW)
        explotarionofWarrior_button.grid(row=5, column=1)

        self.main.mainloop()


mBot=mainBot()
mBot.mainWindow()