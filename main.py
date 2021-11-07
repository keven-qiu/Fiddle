from tkinter import *

from BasicView import BasicView
from DailyCheckInView import DailyCheckInView
from ExerciseLogic import ExerciseLogic
from FitnessBackgroundView import FitnessBackgroundView


class Main(BasicView):
    window = None

    def __init__(self, windowSizeX, windowSizeY, windowTitle):
        super().__init__(windowSizeX, windowSizeY, windowTitle)
        self.window = self.createWindow()
        self.window.config(padx=50, pady=50, bg="#B5D3E7")

        logic = ExerciseLogic()

        name = Label(self.window, text="Exercise and Day Planner", font=("bold", 30), bg="lightblue")
        name.pack(pady=2)

        fitnessBackgroundView = FitnessBackgroundView(500, 500, "Registration Form", self.window)
        self.createFitnessBackGroundButton(fitnessBackgroundView)

        dailyCheckInView = DailyCheckInView(500, 500, "Daily Check-In", self.window, logic)
        self.createDailyCheckInButton(dailyCheckInView)

    def createFitnessBackGroundButton(self, fitnessBackgroundView):
        btn = Button(self.window, text="Input Fitness", fg="blue", font=("bold", 30),
                     command=fitnessBackgroundView.getInputForm)
        btn.pack(pady=3)
        return btn

    def createDailyCheckInButton(self, dailyCheckInView):
        btn = Button(self.window, text="Daily Check-In", fg="blue", font=("bold", 30),
                     command=dailyCheckInView.getDailyWindow)
        btn.pack(pady=4)
        return btn


if __name__ == '__main__':
    Main(500, 500, "Exercise and Day Planner")
    mainloop()
