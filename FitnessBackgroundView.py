from abc import ABC
from tkinter import *

from BasicView import BasicView


class FitnessBackgroundView(BasicView, ABC):
    LEVELS = ["Low", "Moderate", "High"]
    selectedLevel = ""
    exerciseHours = 0  # TODO: get exercise hours

    def __init__(self, windowSizeX, windowSizeY, windowTitle, mainWindow):
        super().__init__(windowSizeX, windowSizeY, windowTitle, mainWindow)

    def getInputForm(self):
        def displaySelectedLevel(choice):
            self.selectedLevel = value_inside.get()

        root = self.createWindow()
        label_0 = Label(root, text="Exercise Survey", width=20, font=("bold", 20))
        label_0.place(x=self.getWindowSizeX() / 8, y=self.getWindowSizeY() / 8)

        label_1 = Label(root, text="FullName", width=20, font=("bold", 10))
        label_1.place(x=self.getWindowSizeX() / 8, y=2 * (self.getWindowSizeY() / 8))
        entry_1 = Entry(root)
        entry_1.place(x=2 * self.getWindowSizeX() / 8, y=2 * (self.getWindowSizeY() / 8))

        value_inside = StringVar(root)
        value_inside.set("Choose Exercise Level")
        question_menu = OptionMenu(root, value_inside, *self.LEVELS, command=displaySelectedLevel)
        question_menu.place(x=self.getWindowSizeX() / 8, y=3 * (self.getWindowSizeY() / 8))
        question_menu.pack(expand=True)

        def getSelectedLevel(self):
            return self.selectedLevel

        v1 = DoubleVar()

        def hourSlider(self):
            sel = "Hours: " + str(v1.get())
            l1.config(text=sel, font=("Courier", 14))

        l1 = Label(root)
