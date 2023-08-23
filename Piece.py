from TypePiece import *
import random

class Piece:

    __positionX=0
    __positionY=-1
    __SIZE_GRID=20

    __pieceHashMap = dict({
        1: TypePiece.LPIECE,
        2: TypePiece.LMPIECE,
        3: TypePiece.IPIECE,
        4: TypePiece.TPIECE,
        5: TypePiece.SQUAREPIECE,
        6: TypePiece.NPIECE,
        7: TypePiece.ZPIECE
    })

    __indexColor = 0
    
    __colors = dict({
        1: '#00FF00',
        2: '#00FFFF',
        3: '#FF00FF',
        4: '#FFF000',
        5: '#000FFF',
        6: '#F0000F',
        7: '#FFAC1C',
        8: 'silver'
    })


    def __init__(self):
        self.randomPiece()

    def randomPiece(self):
        self.__indexColor +=1
        random_number = random.randint(1, 7)
        self.__piece= self.__pieceHashMap[random_number]
        self.__color = self.__colors.get((self.__indexColor%8)+1)
        self.__positionX=0
        self.__positionY=-1
       
    def rotate(self):
        self.__piece = list(zip(*self.__piece))[::-1]

    def getColor(self):
        return self.__color
                
    def getValues(self) ->[]:
        return self.__piece
    
    def getPositionX(self)->int:
        return self.__positionX
    
    def getPositionY(self) -> int:
        return self.__positionY;
    
    def setPositionX(self, x):
        self.__positionX = x;
    
    def setPositionY(self, y):
        self.__positionY = y;

    def getPieceWidth(self)->int:
        return len(self.__piece[0]);

    def getPieceHeight(self)->int:
        return len(self.__piece);
    
    def isPermitedDown(self)->bool:
        return (self.getPieceHeight()+self.getPositionY()+1)<= self.__SIZE_GRID;
    
    def isPermitedLeft(self)->bool:
        return self.getPositionX()-1 >= 0;
    
    def isPermitedRight(self)->bool:
        return (self.getPieceWidth()+self.getPositionX()+1)<= self.__SIZE_GRID;
    
    def isPermitedRotate(self)->bool:
        if (self.getPieceWidth()> self.getPieceHeight()):
            return self.isPermitedDown()
        else:
            return self.isPermitedRight()
