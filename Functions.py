from pathlib import Path
from finder_sidebar_editor import FinderSidebar
from os.path import expanduser
import shutil
import glob
import os
from glob import glob

from os.path import join


class Functions:
    home = expanduser("~")
    sortpath = home + '/Sortium'

#extensions of files
    photo_ext = \
        '*.gif', \
        '*.png', \
        '*.jpg', \
        '*.psd',\
        '*.raw',\
        '*.jpeg',\
        '*.pdf',\
        '*.icns'

    docum_ext = \
        '*.txt', \
        '*.docx', \
        '*.xml', \
        '*.doc', \
        '*.odt', \
        '*.rtf', \
        '*.pdf', \
        '*.xlsx', \
        '*.csv', \
        '*.json', \
        '*.pptx'

    music_ext = \
        '*.wav', \
        '*.mp3', \
        '*.mp4', \
        '*.aac', \
        '*.wma', \
        '*.flac', \
        '*.m4a'

    # files destination
    photo_dest = home + '/Pictures'
    docum_dest = home + '/Documents'
    music_dest = home + '/Music'

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
