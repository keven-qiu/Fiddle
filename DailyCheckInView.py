from tkinter import *

from BasicView import BasicView


class DailyCheckInView(BasicView):
    def __init__(self, windowSizeX, windowSizeY, windowTitle, mainWindow):
        super().__init__(windowSizeX, windowSizeY, windowTitle, mainWindow)

    def getDailyWindow(self):
        window = self.createWindow()

        frame = Frame(window)

        def clearFrame():
            for widgets in frame.winfo_children():
                widgets.destroy()

        label_1 = Label(frame, text="FullName", width=20, font=("bold", 10))
        label_1.place(x=self.getWindowSizeX() / 8, y=2 * (self.getWindowSizeY() / 8))
        entry_1 = Entry(frame)
        entry_1.place(x=2 * self.getWindowSizeX() / 8, y=2 * (self.getWindowSizeY() / 8))

        frame.place()
