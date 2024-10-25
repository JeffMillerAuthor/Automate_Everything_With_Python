
# =============================================================================
# Chapter 3 - Loading Diverse Flat File Formats into SQL.py
#
# Section 1: Load CSV file into SQL
# =============================================================================

import pandas as pd
import pyodbc
from sqlalchemy import create_engine 
import os

# Get the username
pc_username = os.getlogin()

data_directory = r"C:\\Users\\" + pc_username +  "\\Desktop\Automate_Everything_With_Python\\Data Files"


df_patient_diag = pd.read_csv(data_directory + '\\' + 'Patient Diagnosis.csv',
                              converters={'PatientID':str})

# Connect to SQL Server
conn_str = ('Driver={ODBC Driver 17 for SQL Server};'
            'Server=Enter_Your_Server_Name;' # Enter your server name here
            'Database=Automate_Everything_With_Python;'
            'UID=automation_user;'
            'PWD=AutomateEverything2024!;'
            'Trusted_Connection=no')

# Create a connection and cursor
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Create SQLAlchemy engine
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={conn_str}")

# Define the table name
table_name = 'PatientDiagnosis'  # Change this to your desired table name

# Load the DataFrame to the SQL Server table
df_patient_diag.to_sql(table_name, engine, if_exists='replace', index=False)




# =============================================================================
# 
# Section 2: Load TXT file into SQL
# 
# =============================================================================
import pandas as pd
import pyodbc
import os

# Get the username
pc_username = os.getlogin()

data_directory = r"C:\\Users\\" + pc_username +  "\\Desktop\Automate_Everything_With_Python\\Data Files"

df_patient_bio = pd.read_csv(data_directory + '\\' + 'Patient Biographics.txt',
                             sep='\t',
                             converters={'PatientID':str,
                                         'InsuranceID':str})

# Convert date object to datetime 
df_patient_bio['BirthDate'] = pd.to_datetime(df_patient_bio['BirthDate'],format='%m/%d/%Y')

# Server Connection
conn_str = ('Driver={ODBC Driver 17 for SQL Server};'
            'Server=Enter_Your_Server_Name;' # Enter your server name here
            'Database=Automate_Everything_With_Python;'
            'UID=automation_user;'
            'PWD=AutomateEverything2024!;'
            'Trusted_Connection=no')

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Insert DataFrame/csv file into SQL table
for row in df_patient_bio.itertuples():
    cursor.execute('''insert into PatientBiographics (PatientID,PatientName,BirthDate,MaritalStatus,Race,Gender,Phone,InsuranceID)
                    values(?,?,?,?,?,?,?,?)''',
                    row.PatientID,
                    row.PatientName,
                    row.BirthDate,
                    row.MaritalStatus,
                    row.Race,
                    row.Gender,
                    row.Phone,
                    row.InsuranceID)
    
conn.commit()

# Close Connection
conn.close()

# =============================================================================
# 
# Section 3: Load Dirty TXT file into SQL
# 
# =============================================================================
import pandas as pd
import pyodbc
import os

# Get the username
pc_username = os.getlogin()

data_directory = r"C:\\Users\\" + pc_username +  "\\Desktop\Automate_Everything_With_Python\\Data Files"
                       
df_payor = pd.read_csv(data_directory + '\\' + 'Payor.txt',
                          sep='\t',
                          skiprows=3,
                          usecols=[1,2],
                          converters={1:str})

# Set the first row as the header
df_payor.columns = df_payor.iloc[0]
    
# Drop the first row as it's now the header
df_payor = df_payor.drop(df_payor.index[0])
    
conn_str = ('Driver={ODBC Driver 17 for SQL Server};'
            'Server=Enter_Your_Server_Name;' # Enter your server name here
            'Database=Automate_Everything_With_Python;'
            'UID=automation_user;'
            'PWD=AutomateEverything2024!;'
            'Trusted_Connection=no')

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Insert DataFrame/csv file into SQL table
for row in df_payor.itertuples():
    cursor.execute('''insert into Payors (PayorID,Payor)
                    values(?,?)''',
                    row.PayorID,
                    row.Payor)
    
conn.commit()

# Close Connection
conn.close()

# =============================================================================
# 
# Section 4: Load Excel file into SQL
# 
# =============================================================================
import pandas as pd
import pyodbc
import os

# Get the username
pc_username = os.getlogin()

data_directory = r"C:\\Users\\" + pc_username +  "\\Desktop\Automate_Everything_With_Python\\Data Files"

df_hospital = pd.read_excel(data_directory + '\\' + 'Hospitals.xlsx',
                             skiprows=2,
                             converters={'ClinicID':str,
                                        'Zip':str})[['ClinicID','ClinicName','City','State','Zip']]

conn_str = ('Driver={ODBC Driver 17 for SQL Server};'
            'Server=Enter_Your_Server_Name;' # Enter your server name here
            'Database=Automate_Everything_With_Python;'
            'UID=automation_user;'
            'PWD=AutomateEverything2024!;'
            'Trusted_Connection=no')

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Insert DataFrame/csv file into SQL table
for row in df_hospital.itertuples():
    cursor.execute('''insert into Hospital (ClinicID,ClinicName,City,State,Zip)
                    values(?,?,?,?,?)''',
                    row.ClinicID,
                    row.ClinicName,
                    row.City,
                    row.State,
                    row.Zip)
    
conn.commit()

# Close Connection
conn.close()


# =============================================================================
# 
# Section 5: Load Excel files into SQL from specific worksheet
# 
# =============================================================================
import pandas as pd
import pyodbc
import os

# Get the username
pc_username = os.getlogin()

data_directory = r"C:\\Users\\" + pc_username +  "\\Desktop\Automate_Everything_With_Python\\Data Files"

conn_str = ('Driver={ODBC Driver 17 for SQL Server};'
            'Server=Enter_Your_Server_Name;' # Enter your server name here
            'Database=Automate_Everything_With_Python;'
            'UID=automation_user;'
            'PWD=AutomateEverything2024!;'
            'Trusted_Connection=no')

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Load excel file
df_providers = pd.read_excel(data_directory + '\\' + 'Raw Data.xlsx',
                          sheet_name='Providers',
                          converters={'ProviderID':str})

# Insert DataFrame into SQL table
for row in df_providers.itertuples():
    cursor.execute('''insert into Providers (ProviderID,ProviderName,Phone)
                    values(?,?,?)''',
                    row.ProviderID,
                    row.ProviderName,
                    row.Phone)

# Load excel file    
df_diagnosisdesc = pd.read_excel(data_directory + '\\' + 'Raw Data.xlsx',
                          sheet_name='Diagnosis Descriptions',
                          converters={'DiagCode':str})

# Insert DataFrame into SQL table
for row in df_diagnosisdesc.itertuples():
    cursor.execute('''insert into DiagnosisDescriptions (DiagCode,DiagDescription)
                    values(?,?)''',
                    row.DiagCode,
                    row.DiagDescription)

# Load excel file    
df_diagnosisdesc = pd.read_excel(data_directory + '\\' + 'Raw Data.xlsx',
                          sheet_name='Patient Assessments',
                          converters={'ProviderID':str,
                                      'ClinicID':str,
                                      'PatientID':str})

# Insert DataFrame into SQL table
for row in df_diagnosisdesc.itertuples():
    cursor.execute('''insert into PatientAssessments (PostPeriod,DateEntered,ProviderID,ClinicID,
                   DateTimeAssessment,PatientID,PatientName,Temperature,Pulse_Oximeter,SOB,Cough,
                   Abdominal_Pain,Diarrhea_Or_Other_Gi_Upset,Nausea,Loss_Of_Taste,
                   Red_Shadowed_Eyes_Or_Pink_Eye,Tingling_Sensation_Of_Face_Or_Hands,Sore_Throat,
                   Chills_And_Or_Repeated_Shaking_With_Chills,Muscle_Pain,Loss_Of_Smell,Headache)
                    values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                    row.PostPeriod,
                    row.DateEntered,
                    row.ProviderID,
                    row.ClinicID,
                    row.DateTimeAssessment,
                    row.PatientID,
                    row.PatientName,
                    row.Temperature,
                    row.Pulse_Oximeter,
                    row.SOB,
                    row.Cough,
                    row.Abdominal_Pain,
                    row.Diarrhea_Or_Other_Gi_Upset,
                    row.Nausea,
                    row.Loss_Of_Taste,
                    row.Red_Shadowed_Eyes_Or_Pink_Eye,
                    row.Tingling_Sensation_Of_Face_Or_Hands,
                    row.Sore_Throat,
                    row.Chills_And_Or_Repeated_Shaking_With_Chills,
                    row.Muscle_Pain,
                    row.Loss_Of_Smell,
                    row.Headache)
    
conn.commit()

# Close Connection
conn.close()
