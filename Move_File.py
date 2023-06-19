from fileinput import filename
import os 
import shutil
from tabnanny import filename_only
import time

from_dir = "C:/Users/ashis/Downloads"
to_dir = "C:/Users/ashis/Documents/Downloaded_Files"


dir_tree = {
    ',txt','.doc','.docx','.pdf'
}

list_Of_Files=os.listdir(from_dir)
print(list_Of_Files)

for FileName in list_Of_Files:
    name,ext=os.path.splitext(FileName)
    print(name,ext)


path1= from_dir+'/'+filename
path2=to_dir+'/' + "Document_Files"
path3=to_dir+ '/' + "Document_Files" + '/' + filename

if os.path.exists(path2): 
    print("Moving " + filename + "....") 
    shutil.move(path1, path3)  
else: 
    os.makedirs(path2) 
    print("Moving " + filename + "....") 
    shutil.move(path1, path3) 
                    
    