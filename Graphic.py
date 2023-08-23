import tkinter as tk
import threading
import sys
from Grid import *
from Piece import *

class Graphic:

    __cells = []
    __canvas = any
    __SIZE_GRID=20
    __playOn=False

    def __init__(self):
        self.__grid = Grid()
        self.__piece = Piece()
        self.__window = tk.Tk()
        self.__window.wm_title("Tetris")
        self.__window.geometry("510x650")
        self.__setHeader()
        self.__setGrid()
        self.__setKeyEvents()
        self.__grid.updatePiece(self.__piece)

    def onLoop(self):
        self.__window.mainloop()

    def getPiece(self):
        return self.__piece

    def getGrid(self):
        return self.__grid

    def showScenes(self):
        if(self.__piece.isPermitedDown() and not self.__grid.collisionOnFall()):
            self.__grid.down(self.__refresh)
        else:
            self.__grid.setPermanentPiece(self.__piece)
            self.__addPoints(10)
            self.__piece.randomPiece()
            self.__refresh

    def showGameOverLabel(self):
        self.__labelGameOver.config(text="Game Over")

    def getThread(self):
        return self.__thread

    def initThread(self, function):
        self.__thread = threading.Thread(target=function)
        self.__thread.daemon = True
    
    def setClickRestart(self, function):
        self.__start = tk.Button(self.__panedButtons, text="Reiniciar", command=function)
        self.__start.pack(side="left")

    def setClickStart(self, function):
        self.__start = tk.Button(self.__panedButtons, text="Comenzar", command=function)
        self.__start.pack(side="left")

    def setClickStop(self, function):
        self.__stop = tk.Button(self.__panedButtons, text="Parar", command=function)
        self.__stop.pack(side="right")

    def setTextBtnStop(self):
        self.__playOn=True

    def setTextBtnStart(self):
        self.__playOn=False
    
    def setTextPointsTo0(self):
        self.__labelPoints.configure(text=0)

    def isGameOver(self):
        return self.__grid.isGameOver()

    def __setHeader(self):
        self.__setWelcome()
        self.__setIntructions()
        self.__setPanelButtons()
        self.__setPointsPanel()
        self.__setGameOver()
        
    
    def __setWelcome(self):
        __welcome = tk.Label(self.__window, text="Bienvenido al juego del Tetris!!")
        __welcome.pack()

    def __setIntructions(self):
        __instruction1 = tk.Label(self.__window, text="Mueve la pieza con los cursores")
        __instruction1.pack()
        __instruction2 = tk.Label(self.__window, text="Rota la pieza con la tecla espacio")
        __instruction2.pack()
        __instruction3 = tk.Label(self.__window, text="Sal de la aplicación con la tecla escape")
        __instruction3.pack()
    
    def __setPanelButtons(self):
        self.__panedButtons = tk.Menubutton(self.__window)
        self.__panedButtons.pack(pady=3)

    def __setPointsPanel(self):
        self.__panedPoints = tk.PanedWindow(self.__window, background="silver")
        self.__panedPoints.pack(pady=3)
        labelPointsText = tk.Label(self.__panedPoints, text="Puntos:  ")
        labelPointsText.pack(side="left")
        self.__labelPoints = tk.Label(self.__panedPoints, text="0")
        self.__labelPoints.pack(side="left")

    def __setGameOver(self):
        self.__labelGameOver = tk.Label(self.__window, text=" ")
        self.__labelGameOver.config(font=("Arial", 32, "bold"))
        self.__labelGameOver.pack(pady=3)

    def __setGrid(self):
        self.__panedWindow = tk.PanedWindow(self.__window)
        self.__panedWindow.pack(fill=tk.BOTH, expand=True, side="top")
        self.__canvas = tk.Canvas(self.__panedWindow)
        self.__canvas.pack(fill=tk.BOTH, expand=True, padx=50, pady=5)
        for row in range(self.__SIZE_GRID):
            for col in range(self.__SIZE_GRID):
                x = col * self.__SIZE_GRID
                y = row * self.__SIZE_GRID
                width= (col+1)*self.__SIZE_GRID
                height=(row+1)*self.__SIZE_GRID
                cell =  self.__canvas.create_rectangle(x, y, width, height, width=1, fill="black", outline="black")
                self.__cells.append(cell)
            
    def __setKeyEvents(self):
        self.__window.bind("<Down>", self.__onPress)
        self.__window.bind("<Left>", self.__onPress)
        self.__window.bind("<Right>", self.__onPress)
        self.__window.bind("<space>", self.__onPress)
        self.__window.bind("<Escape>", self.__onPress)

    def __onPress(self,event):
        if self.__playOn:
            if event.keysym == "Down" and not self.__grid.collision("Down"): 
                self.__grid.down(self.__refresh)
            if event.keysym == "Left" and not self.__grid.collision("Left"): 
                self.__grid.left(self.__refresh)
            if event.keysym == "Right" and not self.__grid.collision("Right"): 
                self.__grid.right(self.__refresh)
            if event.keysym == "space" and not self.__grid.collision("Rotate"): 
                self.__grid.rotate(self.__refresh)
            if event.keysym == "Escape": sys.exit()

    def __refresh(self):
        self.__resetGrid()
        self.__printPieces()
        self.__grid.deleteCompleteLines(self.__addPoints)
    
    def __addPoints(self, points):
        score = int(self.__labelPoints.cget("text"))+points
        self.__labelPoints.configure(text=score)


    def __resetGrid(self):       
        for i in range(1, (self.__SIZE_GRID**2)+1):
            cell = self.__canvas.find_withtag(f"{i}")
            self.__canvas.itemconfig(cell, fill="black", outline="black") 

    def __printPieces(self):
        self.__printActualPiece(self.__piece)
        self.__printPermanentPieces()

    def __printActualPiece(self, piece):
        pValues = piece.getValues()
        x = piece.getPositionX();
        y = piece.getPositionY();
        for i in range(0, len(pValues)):
            for j in range(0, len(pValues[i])):
                if pValues[i][j]==1 :
                    row = y + i
                    col = x + j
                    position = (row*self.__SIZE_GRID)+col+1
                    cell = self.__canvas.find_withtag(f"{position}")
                    self.__canvas.itemconfig(cell, fill=piece.getColor(), outline="black") 

    def __printPermanentPieces(self):
        permanentPieces = self.__grid.getGridPermanentPieces()
        for i in range(0, len(permanentPieces)):
            for j in range(0, len(permanentPieces[i])):
                if permanentPieces[i][j]!=0:
                    position = (i*self.__SIZE_GRID)+j + 1
                    cell = self.__canvas.find_withtag(f"{position}")
                    self.__canvas.itemconfig(cell, fill=permanentPieces[i][j], outline="black") 
    
    