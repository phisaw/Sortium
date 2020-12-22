from pathlib import Path
from finder_sidebar_editor import FinderSidebar
from os.path import expanduser
import shutil
import glob
import tkinter
import os
from glob import glob

from os.path import join


class Functions:
    home = expanduser("~")
    sortpath = home + '/Sortium'

    photo_ext = \
        '*.gif', \
        '*.png', \
        '*.jpg'

    docum_ext = \
        '*.txt', \
        '*.docx', \
        '*.pdf'

    # photos destination
    photo_dest = home + '/Pictures'
    docum_dest = home + '/Documents'

    def moveit(self, sortpath, extension, destination):
        all_files = []
        for ext in extension:
            all_files.extend(glob(join(sortpath, ext)))

        for sort_files in all_files:
            shutil.move(sort_files, destination)

    def add_sidebar(self):
        sidebar = FinderSidebar()
        sidebar.add('/Users/philip/Sortium')

    def rem_sidebar(self):
        sidebar = FinderSidebar()
        sidebar.remove('Sortium')

    def settings_window(self):
        pass

    def createdir(self, sortpath):
        if not Path(sortpath).exists():
            print('creating ' + sortpath)
            os.makedirs(sortpath)
        else:
            print(sortpath + ' exists')
