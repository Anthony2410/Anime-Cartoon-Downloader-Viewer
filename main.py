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

def get_headers():
    '''
    '''
    return {
        'User-Agent': ''
    }

def get_html(*args, **kwargs):
    '''
    '''
    try:
        if kwargs.get('js'):
            with webdriver.Firefox() as driver:
                driver.get(args[0])
                if kwargs.get('obj'):
                    return BS(driver.page_source, 'html.parser')
                else:
                    return driver.page_source
        else:
            r = requests.get(args[0], headers=get_headers())
            if r.status_code == 200:
                if kwargs.get('obj'):
                    return BS(r.text, 'html.parser')
                else:
                    return r.text
    except Exception as e:
        print(e)

def get_image(*args):
    '''
    '''
    try:
        r = requests.get(args[0], headers=get_headers())
        if r.status_code == 200:
            return Image.open(BytesIO(r.content))
    except Exception as e:
        print(e)

def download_file(*args, **kwargs):
    '''
    '''
    try:
        r = requests.get(args[0], headers=get_headers(), stream=True)
        if r.status_code == 200:
            with open(kwargs.get('file'), 'wb') as f:
                for chunk in r.iter_content(
                    chunk_size=kwargs.get('chuck_size', 128)):
                    f.write(chunk)
    except Exception as e:
        print(e)



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