"""
This class is only used for visualization of False 3D.
3D Chess Board written in Visual Python
Author: Shaun Press
"""

import visual as vis

class Board:
    'Class for chess board and pieces'
    def __init__(self):
        self.frame = vis.frame()
        'Builds board and places pieces'
        self.squares = []
        for i in range(64):
            self.squares.append(None)
        self.makeBoard()
        self.placePieces()
        vis.scene.center=(3.5,0,3.5)

    def addPiece(self,x,y,piece):
        self.squares[y*8+x] = piece

    def movePiece(self,fx,fy,tx,ty):
        'Takes piece from square fx,fy and moves to tx,ty'
        'Checks if piece exists on square'
        piece = self.squares[fy*8+fx]
        if piece == None:
            print 'eh?'
            return
        topiece = self.squares[ty*8+tx]
        if topiece != None:
            topiece.setvisible(0)
        piece.move((tx,0,ty))
        self.squares[ty*8+tx] = piece
        self.squares[fy*8+fx] = None

    def parseString(self,pMove):
        'Accepts input in long algebraic ie e2e4'
        'Columns are a-h, rows are 1-8'
        'Bottom left square is a1 top right h9 etc' 
        fx = 7-(ord(pMove[0])-ord('a'))
        fy = ord(pMove[1])-ord('1')
        tx = 7-(ord(pMove[2])-ord('a'))
        ty = ord(pMove[3])-ord('1')
        self.movePiece(fx,fy,tx,ty)

    def makeBoard(self):
        for i in range(8):
            for j in range(8):
                if (i+j) % 2 == 1:
                    sColor = vis.color.blue
                else: sColor = vis.color.white
                vis.box(frame = self.frame, pos=(i,-0.1,j),length=1,height=0.1,width=1,color=sColor)

    def placePieces(self):
        for i in range(8):
            self.addPiece(i,1,Pawn((i,0,1),vis.color.white , self.frame))
            self.addPiece(i,6,Pawn((i,0,6),vis.color.red, self.frame))

        self.addPiece(0,0,Rook((0,0,0),vis.color.white, self.frame))
        self.addPiece(7,0,Rook((7,0,0),vis.color.white, self.frame))
        self.addPiece(0,7,Rook((0,0,7),vis.color.red, self.frame))
        self.addPiece(7,7,Rook((7,0,7),vis.color.red, self.frame))
        #self.addPiece(1,0,Knight((1,0,0),vis.color.white, self.frame))
        #self.addPiece(6,0,Knight((6,0,0),vis.color.white, self.frame))
        #self.addPiece(1,7,Knight((1,0,7),vis.color.red, self.frame))
        #self.addPiece(6,7,Knight((6,0,7),vis.color.red, self.frame))
        self.addPiece(2,0,Bishop((2,0,0),vis.color.white, self.frame))
        self.addPiece(5,0,Bishop((5,0,0),vis.color.white, self.frame))
        self.addPiece(2,7,Bishop((2,0,7),vis.color.red, self.frame))
        self.addPiece(5,7,Bishop((5,0,7),vis.color.red, self.frame))
        self.addPiece(4,0,Queen((4,0,0),vis.color.white, self.frame))
        self.addPiece(4,7,Queen((4,0,7),vis.color.red, self.frame))
        self.addPiece(3,0,King((3,0,0),vis.color.white, self.frame))
        self.addPiece(3,7,King((3,0,7),vis.color.red, self.frame))

        
class Piece:
    'A parent class for all the piece subclasses'
    def __init__(self):
        self.base = None

    def move(self,newPos):
        self.base.pos = newPos

    def setvisible(self,state):
        'Makes more complex shapes invisible'
        if hasattr(self.base,'objects'):
            for obj in self.base.objects:
                obj.visible = state
        else:
            self.base.visible = state
        
#All the classes for pieces
#Simply describes how they are drawn
            
class Pawn(Piece):
    def __init__(self,spos,sColor, fr):
        self.base = vis.cone(frame=fr, pos=spos,radius=0.4,axis=(0,1,0),color=sColor)

class Rook(Piece):
    def __init__(self,spos,sColor, fr):
        self.base = vis.cylinder(frame = fr, pos=spos,radius=0.4,length=1,axis=(0,1,0),color=sColor)

class Knight(Piece):
    def __init__(self,spos,sColor, fr):
        self.base = vis.frame(frame = fr, sepos=spos)
        vis.box(frame=self.base,pos=(0,0.4,0),width=0.4,length=0.8,height=0.4,axis=(0,1,0),color=sColor)
        vis.cone(frame=self.base,pos=(0,0.6,0),radius=0.2,axis=(0,1,0),color=sColor)

class Bishop(Piece):
    def __init__(self,spos,sColor, fr):
        self.base = vis.frame(pos=spos, frame=fr)
        vis.cylinder(frame=self.base,pos=(0,0,0),radius=0.2,length=0.8,axis=(0,1,0),color=sColor)
        vis.cone(frame=self.base,pos=(0,0.8,0),radius=0.2,axis=(0,1,0),color=sColor)
class Queen(Piece):
    def __init__(self,spos,sColor, fr):
        self.base = vis.frame(pos=spos, frame=fr)
        vis.cylinder(frame=self.base,pos=(0,0,0),radius=0.4,length=1.0,axis=(0,1,0),color=sColor)
        vis.sphere(frame=self.base,radius=0.4,pos=(0,1.4,0),color=sColor)

class King(Piece):
    def __init__(self,spos,sColor, fr):
        self.base = vis.frame(pos=spos, frame=fr)
        vis.cylinder(frame=self.base,pos=(0,0,0),radius=0.4,length=1.2,axis=(0,1,0),color=sColor)
        vis.box(frame=self.base,height=0.6,width=0.6,length=0.6,pos=(0,1.5,0),color=sColor)

if __name__ == "__main__":            
    thisBoard = Board()
    #example move
    #thisBoard.parseString('e2e4')
