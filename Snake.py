#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Board import *

class Snake(Frame):

    def __init__(self):
        super().__init__()
        self.master.title('Awesome snake')
        self.board = Board()
        self.pack()


def main():
    root = Tk()
    nib = Snake()
    root.mainloop()


if __name__ == '__main__':
    main()