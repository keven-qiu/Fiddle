from tkinter import *

import colours
from BasicView import BasicView
from DailyCheckInView import DailyCheckInView
from ExerciseLogic import ExerciseLogic
from FitnessBackgroundView import FitnessBackgroundView


class Main(BasicView):
    window = None

    def __init__(self, windowSizeX, windowSizeY, windowTitle):
        super().__init__(windowSizeX, windowSizeY, windowTitle)
        self.window = self.createWindow()
        self.window.config(padx=50, pady=50, bg=colours.PURPLE)

        logic = ExerciseLogic()

        name = Label(self.window, text="Fiddle", font=("bold", 50), bg=colours.PURPLE, fg=colours.YELLOW)
        name.pack(pady=2)

        fitnessBackgroundView = FitnessBackgroundView(400, 600, "Registration Form", self.window)
        self.createFitnessBackGroundButton(fitnessBackgroundView)

        dailyCheckInView = DailyCheckInView(400, 600, "Daily Check-In", self.window, logic)
        self.createDailyCheckInButton(dailyCheckInView)

    def createFitnessBackGroundButton(self, fitnessBackgroundView):
        btn = Button(self.window, text="Input Fitness", bg=colours.BLACK, fg=colours.YELLOW, font=("bold", 30),
                     command=fitnessBackgroundView.getInputForm)
        btn.pack(pady=3)
        return btn

    def createDailyCheckInButton(self, dailyCheckInView):
        btn = Button(self.window, text="Daily Check-In", bg=colours.BLACK, fg=colours.YELLOW, font=("bold", 30),
                     command=dailyCheckInView.getDailyWindow)
        btn.pack(pady=4)
        return btn


if __name__ == '__main__':
    Main(400, 600, "Welcome to Fiddle")
    mainloop()
