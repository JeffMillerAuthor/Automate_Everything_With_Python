# Test what libraries are installed
import pandas

libraries = ["pandas", "pyodbc","sqlalchemy","openpyxl","dateutil","win32com"]
             

for lib in libraries:
    try:
        __import__(lib)
        print(f"{lib} is installed")
    except ImportError:
        print(f"{lib} is NOT installed")




# Importing Required Libraries
import pandas as pd
from datetime import datetime

# Creating a dictionary of data
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'City': ['New York', 'Paris', 'Berlin', 'London']}

# Creating a DataFrame
df = pd.DataFrame(data)

# Retrieving the current date
current_date = datetime.now().date()

# Adding a new column to the DataFrame with the current date
df['Date Retrieved'] = current_date

# Print DataFrame
print(df)


