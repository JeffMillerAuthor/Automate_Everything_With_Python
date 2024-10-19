# =============================================================================
# Chapter 9 - Automating Report Collection and Aggregation From Outlook.py
# =============================================================================

import os
import pandas as pd
import win32com.client as win32

# Define the folder path for downloaded emails
desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
downloaded_folder_path = os.path.join(desktop_path, 'Automate_Everything_With_Python', 'Email Downloaded Folder')

# Create the downloaded folder if it doesn't exist
if not os.path.exists(downloaded_folder_path):
    os.makedirs(downloaded_folder_path)

# Initialize Outlook application
outlook = win32.Dispatch('outlook.application')
namespace = outlook.GetNamespace('MAPI')

# Access the inbox
inbox = namespace.GetDefaultFolder(6)  # 6 refers to the inbox folder
messages = inbox.Items

# Initialize a list to store DataFrames
dataframes = []

# Process each email in the inbox
for message in messages:
    if message.Subject.startswith("Monthly Report - ") and message.Attachments.Count > 0:
        # Download each attachment in the email
        for attachment in message.Attachments:
            file_name = attachment.FileName
            save_path = os.path.join(downloaded_folder_path, file_name)
            attachment.SaveAsFile(save_path)
            print(f"Downloaded: {file_name} to {downloaded_folder_path}")

            # Check if the file is an Excel file
            if file_name.endswith('.xlsx'):
                # Load the Excel file into a DataFrame
                df = pd.read_excel(save_path)
                dataframes.append(df)

# Concatenate all DataFrames into a single DataFrame
if dataframes:
    combined_df = pd.concat(dataframes, ignore_index=True)
    combined_df_path = os.path.join(downloaded_folder_path, 'Combined_Report.xlsx')
    combined_df.to_excel(combined_df_path, index=False)
    print(f"Combined DataFrame saved to: {combined_df_path}")
else:
    print("No relevant emails with attachments found.")







