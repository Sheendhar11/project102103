import os 
import shutil

from_dir = "C:/Users/ashis/Downloads"
to_dir = "C:/Users/ashis/Documents/Downloaded_Files"

list_Of_Files=os.listdir(from_dir)
print(list_Of_Files)

for FileName in list_Of_Files:
    name,ext=os.path.splitext(FileName)
    print(name,ext)