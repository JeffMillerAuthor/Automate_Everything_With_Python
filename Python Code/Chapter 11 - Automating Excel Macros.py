# =============================================================================
# Chapter 11 - Automating Excel Macros.py
# =============================================================================

import os
import win32com.client as win32

# Define the path to the workbook
desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
excel_models_path = os.path.join(desktop_path, 'Automate_Everything_With_Python', 'Excel Models')
workbook_path = os.path.join(excel_models_path, 'PCP Compensation Model.xlsm')

# Initialize Excel application
excel = win32.Dispatch('Excel.Application')
excel.Visible = False  # Run Excel in the background

# Open the workbook
workbook = excel.Workbooks.Open(workbook_path)

# Run the macro
excel.Application.Run("'PCP Compensation Model.xlsm'!GenerateStatements")

# Save and close the workbook
workbook.Save()
workbook.Close()

# Quit Excel
excel.Quit()

print(f"Macro 'GenerateStatements' executed successfully in {workbook_path}.")
