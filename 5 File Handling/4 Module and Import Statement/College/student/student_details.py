import os, sys
#( os and sys module) functionality for interacting with operating system
from os.path import dirname, join, abspath 
#It also imports specific functions (dirname, join, abspath) from the os.path module.
parent_dir_path=abspath(join(dirname(__file__), '..'))  # to create absolute path of  the parent directory of the current script
# print(parent_dir_path)   c:\Users\91830\Python\5 File Handling\4 Module and Import Statement\College
#__file__ will give the path of current script  that is 5 File Handling\4 Module and Import Statement\College\student\student_details.py
# join(dirname(__file__), '..') >> join the current directory(student) with the parent directory or '..' (college)
#abspath() converts the relative path to an absolute path.
#parent_dir_path contains the absolute path of the parent directory of the current script.
sys.path.insert(0,parent_dir_path)
#adds the absolute path of the parent directory to the begining of the system path
#it allows to search modules and packages

from teacher import teacher_details

def student(): 
    print("This is student details")

teacher_details.teacher()