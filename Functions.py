from pathlib import Path
from finder_sidebar_editor import FinderSidebar
import shutil
import glob
import tkinter
import os

class Functions:
    # sortixSource = Path('/Users/philip/Desktop/sortium')
    # pattern of files to sort
    file_txt = '/Users/philip/sortium/*.txt'
    file_png = '/Users/philip/sortium/*.png'
    # destination for the files
    txt_dest = Path('/Users/philip/sortium/txtfiles')
    png_dest = Path('/Users/philip/sortium/pngfiles')
    # array of file types
    file_type = \
        [file_txt,
         file_png]
    # array of destinations
    file_destination = \
        [txt_dest,
         png_dest]

    def sort(self, file_type, file_destination):

        for types, file_destination in zip(file_type, file_destination):
            for files in glob.glob(types):
                shutil.move(files, file_destination)

    def add_sideBar(self):
        sidebar = FinderSidebar()
        sidebar.add('/Users/philip/sortium')

    def rem_sideBar(self):
        sidebar = FinderSidebar()
        sidebar.remove('sortium')

    def settings_window(self):
        pass
