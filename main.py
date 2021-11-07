from tkinter import *

from BasicView import BasicView
from DailyCheckInView import DailyCheckInView
from ExerciseLogic import ExerciseLogic
from FitnessBackgroundView import FitnessBackgroundView


class Main(BasicView):
    BLACK = "#000000"
    WHITE = "#FFFFFF"
    window = None

    def __init__(self, windowSizeX, windowSizeY, windowTitle):
        super().__init__(windowSizeX, windowSizeY, windowTitle)
        self.window = self.createWindow()
        self.window.config(padx=50, pady=50, bg=self.WHITE)

        logic = ExerciseLogic()

        fitnessBackgroundView = FitnessBackgroundView(500, 500, "Registration Form", self.window)
        fitBkgBtn = self.createFitnessBackGroundButton(fitnessBackgroundView)

        dailyCheckInView = DailyCheckInView(500, 500, "Daily Check-In", self.window, logic)
        dailyCheckInButton = self.createDailyCheckInButton(dailyCheckInView)

    def createFitnessBackGroundButton(self, fitnessBackgroundView):
        btn = Button(self.window, text="Input Fitness", fg="blue", font=("bold", 30),
                     command=fitnessBackgroundView.getInputForm)
        btn.pack(side=TOP)
        return btn

    def createDailyCheckInButton(self, dailyCheckInView):
        btn = Button(self.window, text="Daily Check-In", fg="blue", font=("bold", 30),
                     command=dailyCheckInView.getDailyWindow)
        btn.pack(side=TOP)
        return btn


if __name__ == '__main__':
    Main(520, 500, "Our Hackathon App")
    mainloop()
