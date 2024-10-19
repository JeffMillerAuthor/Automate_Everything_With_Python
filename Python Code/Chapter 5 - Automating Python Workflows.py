# =============================================================================
# Chapter 5 - Automating Python Workflows.py
# =============================================================================

import subprocess
import sys
import os

# Define paths
desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
report_folder_path = os.path.join(desktop_path, 'Automate Everything With Python', 'Python Code')

# Name of the script to execute
script_name = "Chapter 3 - Create Respective File for Report User.py"
script_to_execute = os.path.join(report_folder_path, script_name)

try:
    # Execute the script using subprocess
    result = subprocess.run([sys.executable, script_to_execute], capture_output=True, text=True, check=True)
    
    # Print the output
    print(f"Script '{script_name}' executed successfully.")
    print("Output:")
    print(result.stdout)
    
except subprocess.CalledProcessError as e:
    print(f"An error occurred while executing the script: {e}")
    print("Error output:")
    print(e.stderr)
except FileNotFoundError:
    print(f"The script '{script_to_execute}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
