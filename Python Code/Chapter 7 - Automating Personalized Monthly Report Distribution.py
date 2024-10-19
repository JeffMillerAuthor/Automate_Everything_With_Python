
# =============================================================================
# Chapter 7 - Automating Personalized Monthly Report Distribution.py
# =============================================================================

import os
import pandas as pd
import win32com.client as win32
from datetime import datetime

# Define paths
desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
data_files_path = os.path.join(desktop_path, 'Automate Everything With Python', 'Data Files')
email_table_path = os.path.join(data_files_path, 'Email Table.xlsx')
report_folder_path = os.path.join(desktop_path, 'Automate Everything With Python', 'Automated Reports')

# Load the "Email Table.xlsx" into a DataFrame
df_email = pd.read_excel(email_table_path)

# Get the current month's folder path
current_month_folder_name = datetime.now().strftime('%Y-%m Reports')
current_month_folder_path = os.path.join(report_folder_path, current_month_folder_name)

# Initialize Outlook application
outlook = win32.Dispatch('outlook.application')

# Process each Excel file in the current month's folder
for file_name in os.listdir(current_month_folder_path):
    if file_name.endswith('.xlsx'):
        # Extract the 4-digit ID from the file name
        try:
            id_number = file_name.split('-')[1].strip().split()[0]
        except IndexError:
            print(f"Skipping file: {file_name}, unable to extract ID.")
            continue
        
        # Find the corresponding email address in the DataFrame
        email_row = df_email[df_email['ID'].astype(str) == id_number]
        if not email_row.empty:
            recipient_email = email_row['Email Address'].values[0]
            first_name = email_row['FirstName'].values[0]
            last_name = email_row['LastName'].values[0]
            
            # Create a new email
            mail = outlook.CreateItem(0)
            mail.Subject = f"Monthly Report - {current_month_folder_name}"
            mail.Body = f"Please find the attached report for: {first_name} {last_name}."
            mail.To = recipient_email
            
            # Attach the file to the email
            file_path = os.path.join(current_month_folder_path, file_name)
            mail.Attachments.Add(file_path)
            print(f"Attached file: {file_name} for ID: {id_number} to {recipient_email}")
            
            # Send the email
            mail.Send()
            print(f"Email sent to {recipient_email} for file: {file_name}")
        else:
            print(f"No email found for ID: {id_number}, skipping file: {file_name}")

