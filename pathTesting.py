import os
from pathlib import Path
from os.path import expanduser




home = expanduser("~")


sortpath = home + '/sortim'


class Directories:

    def createdir(self):
        if not Path(sortpath).exists():
            os.makedirs(sortpath)
        else:
            print('path exists')

dir = Directories()

dir.createdir()
