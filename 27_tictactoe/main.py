from Tkinter import *
import sys
from lib import board
from lib import player

#Game


class inputWindow(object):
    def __init__(self, master, message):
        top=self.top=Toplevel(master)
        self.l=Label(top,text = message)
        self.value = ""
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.b=Button(top,text='Ok',command=self.accept)
        self.b.pack()
        
    def accept(self):
        self.value=self.e.get()
        self.top.destroy()

class popupWindow(object):
    def __init__(self, master, message):
        top=self.top=Toplevel(master)
        self.l=Label(top,text = message)
        self.l.pack()
        self.b=Button(top,text='Ok',command=self.close)
        self.b.pack()
        
    def close(self):
        self.top.destroy()


class main:
   
    def __init__(self,master):
        self.frame = Frame(master)
        self._master = master
        self.frame.pack(fill="both", expand=True)
        self.label=Label(self.frame, text='Tic Tac Toe Game', height=6, bg='white', fg='blue')
        self.label.pack(fill="both", expand=True)
        self.canvas = Canvas(self.frame, width=300, height=300)
        self.canvas.pack(fill="both", expand=True)
        self.Start=Button(self.frame, text='Start New Game', height=4, command=self.start,bg='gray', fg='black')
        self.Start.pack(fill="both", expand=True)   
        self._creatBoard()

    def start(self):
        self.canvas.delete(ALL)
        self.label['text']=('Tic Tac Toe Game')

        inputX = inputWindow(self._master, "Please enter name for X player:")
        self._master.wait_window(inputX.top)

        if inputX.value == "":
            return

        p1 = player.player(inputX.value, "X")

        inputO = inputWindow(self._master, "Please enter name for O player:")
        self._master.wait_window(inputO.top)

        if inputO.value == "":
            return

        p2 = player.player(inputO.value, "O")
        self._gameBoard = board.board()
        self._gameBoard.start(p1, p2)

        self.canvas.bind("<ButtonPress-1>", self.playGame)  
        self._creatBoard()
        self.Start["state"] = DISABLED


    def end(self):
        self.canvas.unbind("<ButtonPress-1>")
        self.Start["state"] = "normal"
        
    
    def _creatBoard(self):
        self.canvas.create_rectangle(0,0,300,300, outline="black")
        self.canvas.create_rectangle(100,300,200,0, outline="black")
        self.canvas.create_rectangle(0,100,300,200, outline="black")
        self.canvas. create_line( 0, 0, 0, 300, width=6, fill="black")
        self.canvas. create_line( 0, 0, 300, 0, width=6, fill="black")

    def drawCross(self, x, y):
        self.canvas. create_line( x+20, y+20, x-20, y-20, width=4, fill="black")
        self.canvas. create_line( x-20, y+20, x+20, y-20, width=4, fill="black")

    def drawCircle(self, x, y):
        self.canvas.create_oval( x+25, y+25, x-25, y-25, width=4, outline="black")
        
    def playGame(self,event):
        for k in range(0,300,100):
            for j in range(0,300,100):
                if event.x in range(k,k+100) and event.y in range(j,j+100):
                   try:
                        X=(2*k+100)/2
                        Y=(2*j+100)/2
                        X1=int(k/100)
                        Y1=int(j/100)
                        val = self._gameBoard.play(X1, Y1)
                        if val == "X":
                            self.drawCross(X, Y)
                        else:
                            self.drawCircle(X, Y) 
                        
                        winMsg = self._gameBoard.winner()
                        if winMsg is not None:
                            self.label['text'] = winMsg
                            self.end()

                            
                   except Exception as e:
                       errorPopup = popupWindow(self._master, e.message)
                       self._master.wait_window(errorPopup.top)
                        
    

                

root=Tk()
app=main(root)
root.mainloop()