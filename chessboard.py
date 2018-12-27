#Edit in 2018/12/23
#Author: James Hoi
#Email: jameshoi@foxmail.com
#Description: A class for Reversi chessboard

#chessboard import
from __future__ import print_function
from enum import Enum, unique

#Some normal import
import sys

#chessboard setting
Sum_Rows = 8
Sum_Columns = 8

@unique
class ChessType(Enum):
    none = '-'
    white = 'O'
    black = 'X'

Interval_chess = 3

#class definition
class Chessboard(object):
    def __init__(self,sum_rows,sum_columns,interval):
        self.sum_rows = sum_rows
        self.sum_columns = sum_columns
        self.interval = interval
        self.turn = ChessType.black.name
        self.chessboard = None
        self.win = None

    def generatespace(self, num):
        space = ''
        for i in range(num): space += ' '
        return space

    def print(self):
        space = self.generatespace(self.interval)
        print(' ',end=space)
        for num_row in range(self.sum_rows):
            print(num_row+1, end=space)
        print('')

        num_column = 1
        for lines in self.chessboard:
            print(num_column, end=space)
            for chess in lines:
                print(chess.value, end=space)
            num_column += 1
            print('')

        print('black'+'('+ChessType.black.value+')'+':',end='')
        print(self.sum_chess(ChessType.black),end=space)
        print('white'+'('+ChessType.white.value+')'+':', end='')
        print(self.sum_chess(ChessType.white),end=space)
        print(self.turn,end='\'s turn\n')

    def sum_chess(self,chesstype):
        sum = 0
        if self.chessboard != None:
            for rows in self.chessboard:
                sum += rows.count(chesstype)
        return sum

    def inputchessboard(self,chessboard):
        if self.chessboard != None:
            if self.chessboard != chessboard: self.changed = True
            else: self.changed = False
        else: self.changed = True
        self.chessboard = chessboard

    def isFinished(self):
        if self.chessboard != None:
            if self.sum_chess(ChessType.white)+self.sum_chess(ChessType.black)==64:
                if self.sum_chess(ChessType.black)> self.sum_chess(ChessType.white): self.win = ChessType.black.name
                else: self.win = ChessType.white.name
                return True
            else: return False
        else: return False

    def outofrange(self,row,column):
        if not row.isdigit() or not column.isdigit(): return True
        if not 0<int(row)<=self.sum_rows or not 0<int(column)<=self.sum_columns: return True
        return False

def main():
    cb = Chessboard(Sum_Rows,Sum_Columns,Interval_chess)
    chessboard = [[ChessType.none]*8,[ChessType.none]*8,[ChessType.none]*8,[ChessType.none]*8,[ChessType.none]*8,
                  [ChessType.none]*8,[ChessType.none]*8,[ChessType.none]*8]
    cb.inputchessboard(chessboard)
    cb.print()

if __name__ == '__main__':
    sys.exit(main())