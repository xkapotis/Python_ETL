import pyodbc
import pandas as pd
from sql_queries import queries

#### DBs variables
datawarehouse_name = "your_dw_name"
source_name = "your_source_db_name"


##### connections ######
source_cnxn = pyodbc.connect(    "Driver={SQL Server Native Client 11.0};"
"Server=@@@@@@@@@@@@@@@;"
"Database="+source_name+";"
"UID=@@@@@@@@;"
"PWD=@@@@@@@@@;"
"Trusted_Connection=yes;"
)

target_cnxn = pyodbc.connect(       "Driver={SQL Server Native Client 11.0};"
    "Server=@@@@@@@@@@@@;"
    "Database="+datawarehouse_name+";"
    "UID=@@@@@@@;"
    "PWD=@@@@@@@;"
    "Trusted_Connection=yes;"
    )

##### connections ######

source_cursor_cnxn = source_cnxn.cursor()
target_cursor_cnxn = target_cnxn.cursor()

######## Queries ##########
queries(source_cnxn, target_cursor_cnxn)

###### Close Connection ######
source_cnxn.close()







