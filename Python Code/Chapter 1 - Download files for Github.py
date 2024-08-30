# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 05:17:22 2024

@author: Jeff Miller
"""

# =============================================================================
# 
# =============================================================================
    
    
import os
import subprocess

# Define the GitHub repository URL
repo_url = "https://github.com/JeffMillerAuthor/Automate_Everything_With_Python"

# Set the desktop path and destination path
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
repo_name = repo_url.split("/")[-1]  # Keep the original repository name
destination_path = os.path.join(desktop_path, repo_name)

# Check if the destination path already exists
if not os.path.exists(destination_path):
    # Clone the repository to the destination path
    subprocess.run(["git", "clone", repo_url, destination_path], check=True)
    print(f"Repository cloned successfully to {destination_path}")
else:
    print(f"The folder '{destination_path}' already exists on your desktop.")
    
# =============================================================================
#     
# =============================================================================
    

import os
import subprocess

# Define the GitHub repository URL and the destination path
repo_url = "https://github.com/JeffMillerAuthor/Automate_Everything_With_Python"
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
repo_name = repo_url.split("/")[-1]
destination_path = os.path.join(desktop_path, repo_name)

# Function to clone the repository
def clone_repo(repo_url, destination_path):
    try:
        # Clone the repository to the destination path
        subprocess.run(["git", "clone", repo_url, destination_path], check=True)
        print(f"Repository cloned successfully to {destination_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e}")

# Check if the destination path already exists
if not os.path.exists(destination_path):
    clone_repo(repo_url, destination_path)
else:
    print(f"The folder '{destination_path}' already exists on your desktop.")