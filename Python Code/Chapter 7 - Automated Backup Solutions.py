# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:58:48 2024

@author: Jeff Miller
"""
# =============================================================================
# 
# =============================================================================

import os
import shutil
from datetime import datetime

# Define paths
desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
python_code_path = os.path.join(desktop_path, 'Automate Everything With Python', 'Python Code')
backup_folder_path = os.path.join(desktop_path, 'Automate Everything With Python','Python Backup Files')

# Create the backup folder if it doesn't exist
if not os.path.exists(backup_folder_path):
    os.makedirs(backup_folder_path)

# Create a subfolder with the current date
current_date = datetime.now().strftime('%Y-%m-%d')
date_folder_path = os.path.join(backup_folder_path, current_date)

if not os.path.exists(date_folder_path):
    os.makedirs(date_folder_path)

# Copy all Python files to the date folder
for file_name in os.listdir(python_code_path):
    if file_name.endswith('.py'):  # Check for Python files
        src_file_path = os.path.join(python_code_path, file_name)
        dest_file_path = os.path.join(date_folder_path, file_name)
        shutil.copy(src_file_path, dest_file_path)
        print(f"Copied: {file_name} to {date_folder_path}")

print(f"Backup completed successfully in {date_folder_path}.")
