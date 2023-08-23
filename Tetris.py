 
"""
 *
 * Autor: Víctor Andrés
 * Fecha: 18-8-2023
 * Instrucciones: 
 *      - Instala la libreria tkinter ->  brew install python-tk@3.11
 * Mueve la pieza con las flechas y rotla con la tecla de espacio
 * Para salir de la aplicación utiliza la tecla Ctrl
"""

from Graphic import *
from Piece import *
import time

#Code execute when we click on start button       
def onClickStart():
    global playOn
    global graphic
    if not playOn and not graphic.isGameOver(): 
        playOn= True
        graphic.initThread(setInterval)
        graphic.getThread().start()
        graphic.setTextBtnStop()
        

def onClickRestart():
    global playOn
    global graphic
    playOn= True
    graphic.getGrid().initPermamentPieces()
    graphic.getPiece().randomPiece()
    graphic.initThread(setInterval)
    graphic.getThread().start()
    graphic.setTextBtnStop()
    graphic.setTextPointsTo0()

#Code execute when we click on Stop button
def onClikStop():
    global playOn
    if playOn: 
        playOn= False
        graphic.setTextBtnStart()

#Execute each time in a interval of 2 seconds, provieded
#playOn be True
def setInterval():
    global playOn
    global graphic
    while playOn:
        if playOn:
            graphic.showScenes()
        if graphic.isGameOver():
            playOn = False
            graphic.showGameOverLabel()
        time.sleep(2)
        setInterval()
        

if __name__ == "__main__":
    end = False
    playOn = False
    

    #Create Grpahic object and initialize
    graphic = Graphic()
    graphic.initThread(setInterval)
    graphic.setClickRestart(onClickRestart)
    graphic.setClickStart(onClickStart)
    graphic.setClickStop(onClikStop)
    
    #call 
    graphic.showScenes()
    graphic.onLoop()
    
    

