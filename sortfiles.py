from os.path import join, expanduser
from pathlib import Path
import shutil
import glob
import tkinter
import os
from glob import glob

home = expanduser("~")
sortpath = home + '/Sortium'

# photos destination
photo_dest = home + '/Pictures'
docum_dest = home + '/Documents'

# array of destinations
photo_ext = '*.gif', '*.png', '*.jpg'
docum_ext = '*.txt', '*.docx', '*.pdf'


def moveit(extension, destination):
    all_files = []
    for ext in extension:
        all_files.extend(glob(join(sortpath, ext)))

    for sort_files in all_files:
        shutil.move(sort_files, destination)


#photo_files = []
#for ext in photo_ext:
#    photo_files.extend(glob(join(sortpath, ext)))

#for files in photo_files:
#    shutil.move(files, photo_dest)

#docum_files = []
#for ext in (docum_ext):
#    docum_files.extend(glob(join(sortpath, ext)))
#
#for files in docum_files:
#    shutil.move(files, photo_dest)

#file_type = \
#    [docum_files,
#     photo_files]

#file_destination = \
#    [docum_dest,
#     photo_dest]

moveit(photo_ext,photo_dest)
