# =============================================================================
# Chapter 10 - Creating Consilidated Text Backup of Python Script.py
# =============================================================================

import pandas as pd
import os
import datetime as datetime

desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
automate_everything_path = os.path.join(desktop_path, 'Automate_Everything_With_Python')
python_code_path = os.path.join(desktop_path, 'Automate_Everything_With_Python', 'Python Code')
backup_folder_path = os.path.join(desktop_path, 'Automate_Everything_With_Python','Python Backup Files')

# Create the backup folder if it doesn't exist
if not os.path.exists(backup_folder_path):
    os.makedirs(backup_folder_path)

# Create a subfolder with the current date
current_date = datetime.datetime.now().strftime('%Y-%m-%d')
date_folder_path = os.path.join(backup_folder_path, current_date)



##### Gather all files #
all_py_files = os.listdir(python_code_path)

# remove unwanted files
all_py_files = [x for x in all_py_files if '.py' in x]
# allfiles = [x for x in allfiles if 'Completed' not in x]

##### iterate on all files and append to dataframe #
for f in all_py_files:
      with open(python_code_path + '\\' + f,'r') as py_file: 
          py_content = py_file.read() 
          with open(backup_folder_path + '\\' + 'Python Log ' + current_date + '.txt','a') as txt_file: 
              txt_file.write(py_content)

print('Catologing Python script is finished!!!')
