
# =============================================================================
# Chapter 1 - Extracting Files From Github.py
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
    
    
 
    
    
