# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 04:52:54 2024

@author: Jeff Miller
"""

# =============================================================================
# Download SQL files from GitHub
# =============================================================================


import requests
import os



def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Folder created: {path}")
    else:
        print(f"Folder already exists: {path}")

def download_file_from_github(url, local_filename):
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(local_filename, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully: {local_filename}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

# Get the path to the user's desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Create the main folder
main_folder = os.path.join(desktop_path, "Automate Everything With Python")
create_folder(main_folder)

# Create the SQL Code folder
sql_folder = os.path.join(main_folder, "SQL Code")
create_folder(sql_folder)

# List of files to download
files_to_download = ['CDC Covid19 Staff Tables.sql',
                     'dbo.DiagnosisDescriptions.Table.sql',
                     'dbo.Hospital.Table.sql',
                     'dbo.PatientAssessments.Table.sql',
                     'dbo.PatientBiographics.Table.sql',
                     'dbo.PatientCovidLabTest.Table.sql',
                     'dbo.PatientDiagnosis.Table.sql',
                     'dbo.Payors.Table.sql',
                     'dbo.Providers.Table.sql']

# Base GitHub raw content URL
base_url = 'https://github.com/JeffMillerAuthor/Automate_Everything_With_Python/tree/627d19f0d61327160b84329b0cdf348fa6ef45a4/SQL%20Code/'


# Download each file
for file_name in files_to_download:
    # Create the full GitHub URL for the file
    github_raw_url = base_url + requests.utils.quote(file_name)
    
    # Create the local file path
    local_filename = os.path.join(sql_folder, file_name)
    
    # Download the file
    download_file_from_github(github_raw_url, local_filename)


# =============================================================================
# Download Data files from GitHub
# =============================================================================

import requests
import os

# Base URL (GitHub raw content)
base_url = 'https://github.com/JeffMillerAuthor/Automate_Everything_With_Python/raw/main/Data%20Files/'

# List of files to download
files = ['Hospitals.xlsx',
         'Patient Biographics.txt',
         'Patient Diagnosis.csv',
         'Payor.txt',
         'Raw Data.xlsx']

# Create the SQL Code folder
data_folder = os.path.join(main_folder, "Data Files")
create_folder(data_folder)


# Get the user's desktop path
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), r'Desktop\Automate Everything With Python\Data Files')
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), r'Desktop\Automate Everything With Python\Data Files')

# Loop through each file and download it
for file_name in files:
    # Construct the full URL to the file
    file_url = base_url + file_name.replace(" ", "%20")  # Replace spaces with %20 for URL encoding
    
    # Specify the file path where you want to save the file
    file_path = os.path.join(desktop, file_name)
    
    # Download the file
    response = requests.get(file_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Write the content to the file
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"{file_name} downloaded successfully and saved to: {file_path}")
    else:
        print(f"Failed to download {file_name}. Status code: {response.status_code}")