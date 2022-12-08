import pyodbc
import pandas as pd
import glob

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=localhost\SQLEXPRESS;'
                      'Database=Datascrapping;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

print('It Started..')
for index,sheet in enumerate(glob.glob("url original assets/vest_Designer*.xlsx")):
    # print(index)
    # print(sheet)
    # quit()
    df = pd.read_excel(sheet)

    for ind,val in enumerate(df['New column 0 Url']):
        cursor.execute(f'''insert into dbo.SourceUrl (Item_url,Category)
        values('{val}','designer')''')
        cursor.commit()
    print(f'\nSheet {index+1} is Done..')
    # quit()
print('Its Over..')




