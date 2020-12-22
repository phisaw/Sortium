from os.path import join, expanduser
import shutil
import glob
from glob import glob


home = expanduser("~")
sortpath = home + '/Sortium'

# files destination
photo_dest = home + '/Pictures'
docum_dest = home + '/Documents'

# extensions of files
photo_ext = \
    '*.gif', \
    '*.png', \
    '*.jpg'

docum_ext = \
    '*.txt', \
    '*.docx', \
    '*.pdf'


def moveit(extension, destination):
    all_files = []
    for ext in extension:
        all_files.extend(glob(join(sortpath, ext)))

    for sort_files in all_files:
        shutil.move(sort_files, destination)

moveit(photo_ext, photo_dest)
moveit(docum_ext, docum_dest)
