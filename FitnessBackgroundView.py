from abc import ABC
from tkinter import *

import colours
from BasicView import BasicView
from colours import LIGHTBLUE


class FitnessBackgroundView(BasicView, ABC):
    LEVELS = ["low", "moderate", "high"]

    window = None

    selectedLevel = ""
    exerciseHours = 0.0
    fullName = ""

    def __init__(self, windowSizeX, windowSizeY, windowTitle, mainWindow):
        super().__init__(windowSizeX, windowSizeY, windowTitle, mainWindow)

    def getInputForm(self):
        def displaySelectedLevel(choice):
            self.selectedLevel = value_inside.get()

        self.window = self.createWindow()
        self.window.config(padx=50, pady=50, bg=LIGHTBLUE)
        frame = Frame(self.window)
        frame.pack(side="top", expand=True, fill=BOTH)
        label_0 = Label(frame, text="Exercise Survey", width=20, font=("bold", 20))
        label_0.pack(pady=1)

        label_1 = Label(frame, text="Full Name", width=20, font=("bold", 20))
        label_1.pack(padx=1, pady=2)
        entry_1 = Entry(frame)
        entry_1.pack(padx=2, pady=2)
        entry_1.focus()

        value_inside = StringVar(frame)
        value_inside.set("Choose Exercise Level")
        question_menu = OptionMenu(frame, value_inside, *self.LEVELS, command=displaySelectedLevel)
        question_menu.pack(pady=3, expand=True)

        labelHours = Label(frame, text="Hours of Exercise/Day", width=20, font=("bold", 20))
        labelHours.pack(pady=4)
        v = DoubleVar()
        scale = Scale(frame, variable=v, from_=0.0, to=8.0, orient=HORIZONTAL)
        scale.pack(anchor=CENTER)

        button = Button(frame, text='Save', bg=colours.BLACK,
                        command=lambda: self.saveEntries(entry_1.get(), value_inside.get(), v.get()), font=("bold", 20))
        button.pack(pady=5)

        frame.place()

    def getSelectedLevel(self):
        return self.selectedLevel

    def saveEntries(self, name, level, hours):
        self.fullName = name
        self.selectedLevel = level
        self.exerciseHours = hours
        self.window.destroy()
