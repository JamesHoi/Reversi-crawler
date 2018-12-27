#Edit in 2018/12/24
#Author: James Hoi
#Email: jameshoi@foxmail.com
#Description: A crawler for getting chessboard online

#Selenium import
from selenium import webdriver

#beautifulsoup import
from bs4 import BeautifulSoup

#Some normal import
import time
import sys

#chessboard import
import chessboard as cb


#crawler setting
url = 'http://www.webgamesonline.com/reversi/'

class Crawler(object):
    def __init__(self,url):
        self.browser = webdriver.Firefox()
        self.browser.get(url)
        time.sleep(2)

    def getchessboard(self):
        chessboard = []
        line = []
        for each in self.soup.find_all('img'):
            if each.get('id')!= None:
                if each.get('id')[0] == 'I':
                    line.append(self.analysis(each.get('src')))
                    if len(line) == cb.Sum_Columns:
                        chessboard.append(line.copy())
                        line.clear()
        return chessboard

    def analysis(self,str):
        if str == 'images/image_1.png': return cb.ChessType.black
        elif str == 'images/image_2.png': return cb.ChessType.white
        elif str == 'images/base.png': return cb.ChessType.none

    def inputchess(self,column,row):
        self.browser.find_element_by_id('I'+str(column-1)+'-'+str(row-1)).click()

    def sum_chess(self,chesstype):
        if chesstype==cb.ChessType.black: num = 1
        elif chesstype==cb.ChessType.white: num = 2
        return self.browser.find_element_by_id('score'+str(num)).text

    def turn(self):
        text = self.browser.find_element_by_id('TurnId').text
        if text == '   Your turn   ': return cb.ChessType.black.name
        elif text == 'Computer turn': return cb.ChessType.white.name

def main():
    chessboard = cb.Chessboard(cb.Sum_Rows,cb.Sum_Columns,cb.Interval_chess)
    crawler = Crawler(url)
    crawler.soup = BeautifulSoup(crawler.browser.page_source, 'lxml')
    chessboard.inputchessboard(crawler.getchessboard())
    chessboard.print()
    crawler.browser.close()

if __name__ == '__main__':
    sys.exit(main())