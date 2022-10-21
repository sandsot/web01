import pyodbc

def dbconn():
    server = '127.0.0.1' 
    database = 'DoItSQL' 
    username = 'sa' 
    password = 'qwer1234'

    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
    return conn