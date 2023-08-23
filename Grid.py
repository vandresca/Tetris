class Grid:
    
    __SIZE_GRID = 20
    
    def __init__(self):
        self.initPermamentPieces()

    def updatePiece(self, piece):
        self.__piece = piece

    def initPermamentPieces(self):
        self.__gridPermanentPieces= [0]*self.__SIZE_GRID
        for x in range(self.__SIZE_GRID):
            self.__gridPermanentPieces[x] = [0]*self.__SIZE_GRID

    def setPermanentPiece(self, piece):
        pValues = piece.getValues()
        x = piece.getPositionX();
        y = piece.getPositionY();
        for i in range(0, len(pValues)):
            for j in range(0, len(pValues[i])):
                if pValues[i][j]==1 :
                    row = y + i
                    col = x + j
                    self.__gridPermanentPieces[row][col] = [piece.getColor()]

    def isGameOver(self):
        for col in range(len(self.__gridPermanentPieces[0])):
            if self.__gridPermanentPieces[0][col]!=0:
                return True
        return False

    def getGridPermanentPieces(self):
        return self.__gridPermanentPieces
    
    def collision(self, mode):
            x = self.__piece.getPositionX()
            y = self.__piece.getPositionY()
            width= self.__piece.getPieceWidth()
            height= self.__piece.getPieceHeight()
            pValues = self.__piece.getValues()  
            for i in range(height):
                for j in range(width):
                    if (x+j) < (self.__SIZE_GRID-1) and (y+i) < (self.__SIZE_GRID-1):
                        if ((mode=="Down" or mode=="Rotate")
                           and pValues[i][j] != 0 
                           and self.__gridPermanentPieces[y + i + 1][x + j] != 0):
                            return True
                        if ((mode=="Right" or mode=="Rotate")
                            and pValues[i][j] != 0 
                            and self.__gridPermanentPieces[y + i][x + j + 1] != 0):
                            return True
                        if ((mode=="Left" or mode=="Rotate")
                            and pValues[i][j] != 0 
                            and self.__gridPermanentPieces[y + i][x + j - 1] != 0):
                            return True
                        
            return False 

    def collisionOnFall(self):
        x = self.__piece.getPositionX()
        y = self.__piece.getPositionY()
        width= self.__piece.getPieceWidth()
        height= self.__piece.getPieceHeight()
        pValues = self.__piece.getValues()  
        for i in range(height):
            for j in range(width):
                if (y+i) < (self.__SIZE_GRID-1):
                    if pValues[i][j] != 0 and self.__gridPermanentPieces[y + i + 1][x + j] != 0:
                        return True              
        return False       
    
    def __completeLines(self):
        complete = True
        rowsComplete = []
        for row in range(len(self.__gridPermanentPieces)):
            complete = True
            for col in range(len(self.__gridPermanentPieces[row])):
                if(self.__gridPermanentPieces[row][col]==0):
                    complete = False
                    break
            if complete:
                rowsComplete.append(row)        
        return rowsComplete
    
    def deleteCompleteLines(self, addpoints):
        blankRow = [0]*self.__SIZE_GRID
        for row in self.__completeLines():
            self.__gridPermanentPieces.pop(row)
            self.__gridPermanentPieces.insert(0,blankRow)
            addpoints(90)
        
    def down(self, refresh):
        if(self.__piece.isPermitedDown()):
            self.__piece.setPositionY(self.__piece.getPositionY()+1)
            refresh()

    def left(self, refresh):
        if(self.__piece.isPermitedLeft()):
            self.__piece.setPositionX(self.__piece.getPositionX()-1)
            refresh()

    def right(self, refresh):
        if(self.__piece.isPermitedRight()):
            self.__piece.setPositionX(self.__piece.getPositionX()+1)
            refresh()
       
    def rotate(self, refresh):
        if(self.__piece.isPermitedRotate()):
            self.__piece.rotate();
            refresh()