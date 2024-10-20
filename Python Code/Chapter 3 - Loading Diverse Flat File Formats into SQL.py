
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

data_directory = r"C:\\Users\\" + pc_username +  "\\Desktop\Automate Everything With Python\\Data Files"


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

data_directory = r"C:\\Users\\" + pc_username +  "\\Desktop\Automate Everything With Python\\Data Files"

df_patient_bio = pd.read_csv(data_directory + '\\' + 'Patient Biographics.txt',
                             sep='\t',
                             converters={'PatientID':str,
                                         'InsuranceID':str})

# Convert date object to datetime 
df_patient_bio['BirthDate'] = pd.to_datetime(df_patient_bio['BirthDate'],format='%m/%d/%Y')

for c in df_patient_bio.columns:
    print(c)


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

data_directory = r"C:\\Users\\" + pc_username +  "\\Desktop\Automate Everything With Python\\Data Files"

df_payor = pd.read_csv(data_directory + '\\' + 'Payor.txt',
                          sep='\t')
                          
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

data_directory = r"C:\\Users\\" + pc_username +  "\\Desktop\Automate Everything With Python\\Data Files"

df_hospital = pd.read_excel(data_directory + '\\' + 'Hospitals.xlsx')

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

data_directory = r"C:\\Users\\" + pc_username +  "\\Desktop\Automate Everything With Python\\Data Files"

conn_str = ('Driver={ODBC Driver 17 for SQL Server};'
            'Server=Enter_Your_Server_Name;' # Enter your server name here
            'Database=Automate_Everything_With_Python;'
            'UID=automation_user;'
            'PWD=AutomateEverything2024!;'
            'Trusted_Connection=no')

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

df_providers = pd.read_excel(data_directory + '\\' + 'Raw Data.xlsx',
                          sheet_name='Providers',
                          converters={'ProviderID':str})

# Get the column names and join them with commas
column_names_string = ','.join(df_providers.columns)

print(column_names_string)

# Insert DataFrame/csv file into SQL table
for row in df_providers.itertuples():
    cursor.execute('''insert into Providers (ProviderID,ProviderName,Phone)
                    values(?,?,?)''',
                    row.ProviderID,
                    row.ProviderName,
                    row.Phone)
    
df_diagnosisdesc = pd.read_excel(data_directory + '\\' + 'Raw Data.xlsx',
                          sheet_name='Diagnosis Descriptions',
                          converters={'DiagCode':str})

# Get the column names and join them with commas
column_names_string = ','.join(df_diagnosisdesc.columns)

print(column_names_string)

# Insert DataFrame/csv file into SQL table
for row in df_diagnosisdesc.itertuples():
    cursor.execute('''insert into DiagnosisDescriptions (DiagCode,DiagDescription)
                    values(?,?)''',
                    row.DiagCode,
                    row.DiagDescription)
    
conn.commit()

# Close Connection
conn.close()

