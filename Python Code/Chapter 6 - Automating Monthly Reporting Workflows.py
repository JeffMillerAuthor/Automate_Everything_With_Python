# =============================================================================
# Chapter 6 - Automating Monthly Reporting Workflows.py
# =============================================================================

import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
import shutil

# Define the base path for the report folders
desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
report_folder_path = os.path.join(desktop_path, 'Automate_Everything_With_Python', 'Automated Reports')

# Define the source path where the Excel files are located
source_path = report_folder_path  # Assuming the Excel files are on the desktop

# Get the current date
current_date = datetime.now()

# Create monthly folders for the next 12 months
for i in range(12):
    # Calculate the folder name in the format 'yyyy-mm Reports'
    folder_name = (current_date + relativedelta(months=i)).strftime('%Y-%m Reports')
    
    # Create the full path for the folder
    folder_path = os.path.join(report_folder_path, folder_name)
    
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")
    else:
        print(f"Folder already exists: {folder_path}")
    
    # Find and copy any files ending with 'Morning Readings.xlsx'
    for file_name in os.listdir(source_path):
        if file_name.endswith("Morning Readings.xlsx"):
            # Construct the source file path
            source_file_path = os.path.join(source_path, file_name)
            
            # Create the new file name with the datestamp
            datestamp = current_date.strftime('%Y-%m-%d')
            new_file_name = f"{file_name[:-5]} {datestamp}.xlsx"
            
            # Construct the destination file path
            destination_file_path = os.path.join(folder_path, new_file_name)
            
            # Copy the file to the destination folder
            shutil.copy2(source_file_path, destination_file_path)
            print(f"Copied {file_name} to {destination_file_path}")
