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

    # photos destination
    photo_dest = home + '/Pictures'
    docum_dest = home + '/Documents'

    # array of destinations

    photo_files = []
    for ext in ('*.gif', '*.png', '*.jpg'):
        photo_files.extend(glob(join(sortpath, ext)))

    docum_files = []
    for ext in ('*.txt', '*.docx', '*.pdf'):
        docum_files.extend(glob(join(sortpath, ext)))

    file_type = \
        [docum_files,
         photo_files]

    file_destination = \
        [docum_dest,
         photo_dest]

    def sort(self, file_type, file_destination):

        for types, file_destination in zip(file_type, file_destination):
            for list in types:
                for files in glob.glob(list):
                    print(files)
                    #shutil.move(files, file_destination)

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


func = Functions


print(func.file_type)
print(func.file_destination)
