# Write to Azure SQL
# SQL connection
server = "rissa-server.database.windows.net"
database = "Inventory"
username = "***"
password = "***"
driver = "ODBC Driver 18 for SQL Server"

retries = 3
delay = 3
for attempt in range(1, retries + 1):
    try:
        engine = create_engine(
            f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}"
        )
    except Exception as e:
        print(f"Attempt {attempt} failed: {e}")
        time.sleep(delay)
        
if attempt == retries + 1:
    raise Exception("All connection attempts failed")
    exit()

# Write to table
df.to_sql("pieceinventory", engine, if_exists="append", index=False)
