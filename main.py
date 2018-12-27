#Edit in 2018/12/26
#Author: James Hoi
#Email: jameshoi@foxmail.com
#Description: A copy from Reversi online

import sys
import time
from goto import with_goto

import crawler
import chessboard as cb

#definition
chessboard = cb.Chessboard(cb.Sum_Rows,cb.Sum_Columns,cb.Interval_chess)
crawler_chess = crawler.Crawler(crawler.url)
lasttime = 0
clock = 0

def update():
    global lasttime, clock
    crawler_chess.soup = crawler.BeautifulSoup(crawler_chess.browser.page_source, 'lxml')
    crawler_chess.pressid('Pass')
    chessboard.turn = crawler_chess.turn()
    chessboard.inputchessboard(crawler_chess.getchessboard())
    if lasttime != 0: clock += time.perf_counter()-lasttime;
    if not chessboard.changed and clock >= 4:
        return True
    lasttime = time.perf_counter()
    return False

def getinput(str):
    value = None
    while 1==1:
        value = input(str)
        if value!='': return value

@with_goto
def main():
    global lasttime, clock
    while not chessboard.isFinished():
        if update() or (chessboard.turn == cb.ChessType.black.name and chessboard.changed):
            chessboard.print()
            label .getinput
            row = getinput('which row?')
            column = getinput('which column?')
            if(chessboard.outofrange(row,column)): goto .getinput
            if chessboard.chessboard[int(row)-1][int(column)-1] == cb.ChessType.none:
                crawler_chess.inputchess(int(column),int(row))
            else: print('There already has a chess in this location!')
            while chessboard.turn != cb.ChessType.white.name:
                if update():
                    print('You can\'t move to this location!')
                    break
                else:
                    iswaitting = False
                    lasttime = 0
                    clock = 0
        elif not iswaitting:
            chessboard.print()
            print('computer is thinking...')
            iswaitting = True
    print(chessboard.win,end=' win!')
    crawler_chess.browser.close()

if __name__ == '__main__':
    sys.exit(main())