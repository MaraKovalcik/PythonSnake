#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from tkinter import *
from Board import *

class Snake(Frame):

    def __init__(self):
        super().__init__()
        self.master.title('Awesome snake')
        self.board = Board()
        self.pack()


def main():
    root = Tk()

    def restart():
        """Restarts the current program.
        Note: this function does not return. Any cleanup action (like
        saving data) must be done before calling this function."""
        python = sys.executable
        os.execl(python, python, *sys.argv)

    resetButton = Button(root, text='New game', width=30, command=restart, fg="green").pack()
    nib = Snake()
    exitButton = Button(root, text='Exit game', width=30, command=root.destroy, fg="red")
    exitButton.pack()
    root.mainloop()




if __name__ == '__main__':
    main()