#! ./venv/Scripts/python
'''
'''
import requests
import vlc
import threading
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import tix
from tkinter import filedialog
from tkinter import dialog
from PIL import Image
from PIL import ImageTk
from io import BytesIO
from selenium import webdriver
from pathlib import Path
from bs4 import BeautifulSoup as BS



class Root:
    '''
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.tk = tk.Tk()
    
    def load_menu(self):
        '''
        '''
        # Main menu
        self.menubar = tk.Menu(self.tk)

        # add file menu to main menu
        self.file_menu = tk.Menu(self.menubar)
        self.file_menu.add_command(label="Quit")
        self.menubar.add_cascade(label='File', menu=self.file_menu)

        # Add Main menu to frame.
        self.tk.config(menu=self.menubar)
    
    def load_frames(self):
        '''
        '''


def main():
    '''
    '''

if __name__ == '__main__':
    main()