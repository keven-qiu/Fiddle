from tkinter import *


class BasicView:

    def __init__(self, windowSizeX, windowSizeY, windowTitle, mainWindow=None):
        self.mainWindow = mainWindow
        self.windowTitle = windowTitle
        self.windowSizeY = windowSizeY
        self.windowSizeX = windowSizeX

    def createWindow(self):
        if self.mainWindow is not None:
            window = Toplevel(self.mainWindow)
        else:
            window = Tk()
        window.geometry(f"{self.windowSizeX}x{self.windowSizeY}")
        window.title(self.windowTitle)
        return window

    def getWindowSizeX(self):
        return self.windowSizeX

    def getWindowSizeY(self):
        return self.windowSizeY

    def getWindowSizeTitle(self):
        return self.windowTitle
