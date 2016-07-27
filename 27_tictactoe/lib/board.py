import player

#Define exceptions
class InvalidStateError(Exception):
    def __init__(self, msg):
        super(InvalidStateError, self).__init__(msg)

class OccupiedCellError(Exception):
    def __init__(self, msg):
        super(OccupiedCellError, self).__init__(msg)


#board class
class board(object):
    def __init__(self):
        self._matrix = [["empty","empty","empty"],["empty","empty","empty"],["empty","empty","empty"]]
        self._clean()

 
    def start(self, p1, p2):
           if not(type(p1) == player.player and type(p2) == player.player):
               raise TypeError("Start method must accept only player objects")
           if p1.GetIdentity() == p2.GetIdentity():
               raise ValueErrpr("Start method must accept only player objects")
           self._p1 = p1
           self._p2 = p2
           self._nowPlaying = p1
           self._clean()
           

    def _clean(self):
        for i in range (3):
            for j in range (3):
                self._matrix[i][j] = "empty"
        self._count = 0

    def play(self, row, column):
        #Row boundary checking
        if not(row >= 0 and row < 3):
            raise IndexError("Row is out of bounce!")  
        #Column boundary checking
        if not(column >= 0 and column < 3):
            raise IndexError("Column is out of bounce!") 
        #Check if game is over
        if self._count == 9:
            raise InvalidStateError("Game is over!")
        if self._matrix[row][column] != "empty":
            raise OccupiedCellError("Cell %d,%d is occupied" % (row, column))

        #Mark the cell
        self._matrix[row][column] = self._nowPlaying.GetIdentity()
        self._count += 1

        #Switch players
        if self._nowPlaying.GetIdentity() == self._p1.GetIdentity():
            self._nowPlaying = self._p2
        else:
            self._nowPlaying = self._p1

        #Return the identity of the marked cell 
        return self._matrix[row][column]

    #Return the value of a cell
    def val(self, row, column):
        return self._matrix[row][column]

    #Check if the is one row with all equal values that are not empty
    def _checkRows(self):
        for row in range(3):
            if self._matrix[row][0] != "empty" and self._matrix[row][0] == self._matrix[row][1] and self._matrix[row][0] == self._matrix[row][2]:
                return self._matrix[row][0]
        return None

    #Check if there is one column with all equal values that are not empty
    def _checkColumns(self):
        for column in range(3):
            if self._matrix[0][column] != "empty" and self._matrix[0][column] == self._matrix[1][column] and self._matrix[0][column] == self._matrix[2][column]:
                return self._matrix[0][column]
        return None

      #Check if there is one diagonal with all equal values that are not empty
    def _checkDiagonals(self):
        if self._matrix[0][0] != "empty" and self._matrix[0][0] == self._matrix[1][1] and self._matrix[0][0] == self._matrix[2][2]:
            return self._matrix[0][0]
        elif self._matrix[0][2] != "empty" and self._matrix[0][2] == self._matrix[1][1] and self._matrix[0][2] == self._matrix[2][0]:
            return self._matrix[1][1]
        return None

    #Declare winner
    def _declareWinner(self, val):
        if self._p1.GetIdentity() == val:
            return "Player %s wins!!!" % (self._p1.GetName())
        return "Player %s wins!!!" % (self._p2.GetName())

    def winner(self):
        
        #Check the rows 
        val = self._checkRows()
        if val is not None:
            self._count = 9
            return self._declareWinner(val)

        #Check the columns
        val = self._checkColumns()
        if val is not None:
            self._count = 9
            return self._declareWinner(val)

        #Check the diagonals
        val = self._checkDiagonals()
        if val is not None:
            self._count = 9
            return self._declareWinner(val)

        if self._count == 9:
            return "Game ended in a draw!!!"

        return None

