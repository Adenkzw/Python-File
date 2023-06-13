# '*' is for all the files and directories
# '*.*' is for all files in current directories
# '*.py' is for all python files
# path.mkdir() make directory or rmdir() is remove
#path.glob() search for files and directories in the current path
from pathlib import Path

#path = Path('LearningEG/RWAFilesEG/emp.txt')
#print(path.exists())

path = Path()
for file in path.glob('*'):
    print(file)