from tkinter import *

from BasicView import BasicView
from ExerciseLogic import ExerciseLogic
from colours import LIGHTBLUE


class DailyCheckInView(BasicView):
    answerOne = ""
    answerTwo = ""
    answerThree = ""
    window = None
    frame = None
    exerciseLogic = None

    def __init__(self, windowSizeX, windowSizeY, windowTitle, mainWindow, exerciseLogic):
        super().__init__(windowSizeX, windowSizeY, windowTitle, mainWindow)
        self.exerciseLogic = exerciseLogic

    def clearFrame(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()

    def getDailyWindow(self):
        self.window = self.createWindow()
        self.window.config(padx=50, pady=50, bg=LIGHTBLUE)

        self.frame = Frame(self.window)
        self.frame.pack(side="top", expand=True, fill=BOTH)

        self.questionOne()
        self.frame.place()

    def questionOne(self):
        label_1 = Label(self.frame, text="Question 1", width=20, font=("bold", 30))
        label_2 = Label(self.frame, text="How are you feeling today?", width=20, font=("bold", 30))
        label_1.pack(pady=1)
        label_2.pack(pady=2)

        bad = Button(self.frame, text='Bad', bg="#000000", font=("bold", 30),
                     command=lambda: self.writeAnswerOne("bad"))
        bad.pack(pady=3)

        good = Button(self.frame, text='Good', bg="#000000", font=("bold", 30),
                      command=lambda: self.writeAnswerOne("good"))
        good.pack(pady=4)

        excellent = Button(self.frame, text='Excellent', bg="#000000", font=("bold", 30),
                           command=lambda: self.writeAnswerOne("excellent"))
        excellent.pack(pady=5)

    def questionTwo(self):
        label_1 = Label(self.frame, text="Question 2", width=20, font=("bold", 30))
        label_2 = Label(self.frame, text="Are you well rested?", width=20, font=("bold", 30))
        label_1.pack(pady=1)
        label_2.pack(pady=2)

        poor = Button(self.frame, text='Poor', bg="#000000", font=("bold", 30),
                      command=lambda: self.writeAnswerTwo("poor"))
        poor.pack(pady=3)

        moderate = Button(self.frame, text='Moderate', bg="#000000", font=("bold", 30),
                          command=lambda: self.writeAnswerTwo("moderate"))
        moderate.pack(pady=4)

        good = Button(self.frame, text='Good', bg="#000000", font=("bold", 30),
                      command=lambda: self.writeAnswerTwo("good"))
        good.pack(pady=5)

    def questionThree(self):
        label_1 = Label(self.frame, text="Question 3", width=20, font=("bold", 30))
        label_2 = Label(self.frame, text="Can you push yourself?", width=20, font=("bold", 30))
        label_1.pack(pady=1)
        label_2.pack(pady=2)

        yes = Button(self.frame, text='Yes', bg="#000000", font=("bold", 30),
                     command=lambda: self.writeAnswerThree("yes"))
        yes.pack(pady=3)

        no = Button(self.frame, text='No', bg="#000000", font=("bold", 30),
                    command=lambda: self.writeAnswerThree("no"))
        no.pack(pady=4)

    def writeAnswerOne(self, response):
        self.answerOne = response
        self.clearFrame()
        self.questionTwo()

    def writeAnswerTwo(self, response):
        self.answerTwo = response
        self.clearFrame()
        self.questionThree()

    def writeAnswerThree(self, response):
        self.answerThree = response
        self.clearFrame()
        self.exerciseLogic.setExerciseLevel(ExerciseLogic.calculateExerciseLevel(self.answerTwo, self.answerThree))
        self.window.destroy()
        self.assignExerciseLevelView()

    def assignExerciseLevelView(self):
        level = self.exerciseLogic.exerciseLevel
        exercise = self.exerciseLogic.assignExercise()
        popup = self.createWindow()
        self.frame = Frame(popup)
        self.frame.pack(side="top", expand=True, fill=BOTH)
        label_1 = Label(self.frame, text="Your exercise level is", width=20, font=("bold", 30))
        label_2 = Label(self.frame, text=level, width=20, font=("bold", 30), fg="blue")
        label_3 = Label(self.frame, text="Your daily exercise is", width=20, font=("bold", 30))
        label_4 = Label(self.frame, text=exercise, width=20, font=("bold", 30), fg="red")
        label_1.pack(pady=1)
        label_2.pack(pady=2)
        label_3.pack(pady=3)
        label_4.pack(pady=4)

        exitBtn = Button(self.frame, text='Exit', bg="#000000", font=("bold", 30),
                         command=popup.destroy)
        exitBtn.pack(pady=3)

        self.frame.place()
