columns_to_drop = ['Description', 'Description 2', 'Lot', 'Bay', 'Net Wgt', 'Tag ID', 
                   'Sub Lot', 'Group ID', 'Count Qty Committed', 'Count Qty Uncommitted']

# Drop the specified columns
df = df.drop(columns=columns_to_drop)

# Replace the example warehouse names with the actual warehouses whose rows you want to delete
warehouses_to_delete = ['2510ROYAL','8470HWY50','707BARLOW','137HORNER','2COLONY',
 '20HEREFORD','25BRAMTREE','50KENVIEW','ALDERGROVE','RICHMOND','255HOLIDAY',
 'DELTA','HMG-BRAMPT','CALG7405', 'CALG-HD2','CALG-HD-CD','90GLOVERRD','ON',
 'EDMONTON','OLYMPIA','BRAMPTON','6044-20ST','CALGARY','TORONTO','TEST1']
# Drop rows where the 'Warehouse' column is in the list of warehouses to delete
df = df[~df['Whse'].isin(warehouses_to_delete)]

clients_to_delete = ['ZZ10','ZZ11','ZZ12','ZZ18','ZZ21','ZZ23','ZZ38']
# Drop rows where the 'Warehouse' column is in the list of warehouses to delete
df = df[~df['Client'].isin(clients_to_delete)]

import re

# Filter rows where the 'Bin' column starts with a digit
# The regex '^\\d' checks if the string starts with a digit.
df = df[df['Bin'].astype(str).apply(lambda x: bool(re.match('^\\d', x)))]

# Remove all characters except words and digits from the 'Bin' column
df['Bin'] = df['Bin'].astype(str).apply(lambda x: re.sub(r'[^a-zA-Z0-9]', '', x))

# Create a new column 'WHCode' by taking the first two characters of the 'Bin' column
df['WHCode'] = df['Bin'].astype(str).str[:2]

# Create a new column 'WHCode' by taking the first two characters of the 'Bin' column
df['Aisle'] = df['Bin'].astype(str).str[2:4]

# Create a new column 'WHCode' by taking the first two characters of the 'Bin' column
df['Column'] = df['Bin'].astype(str).str[4:6]

# Create a new column 'WHCode' by taking the first two characters of the 'Bin' column
df['Row'] = df['Bin'].astype(str).str[6:7]

#Create a new column 'WHCode' by taking the first two characters of the 'Bin' column
df['Level'] = df['Bin'].astype(str).str[7:]

# Remove rows where 'WHCode' is not purely numeric
df = df[df['WHCode'].astype(str).str.isnumeric()]

# Remove rows where the 'Aisle' column contain a non-letter value
df = df[df['Aisle'].astype(str).str.isalpha()]

# Remove rows where the 'Column' column contains a non-digit value
df = df[df['Column'].astype(str).str.isdigit()]

# Convert 'Receipt Date' and 'Inventory Entry Date' to datetime objects
df['Code Date'] = pd.to_datetime(df['Code Date'], errors='coerce')
df['Receipt Date'] = pd.to_datetime(df['Receipt Date'], errors='coerce')
df['Inventory Entry Date'] = pd.to_datetime(df['Inventory Entry Date'], errors='coerce')

# Format the datetime objects to a short date string (YYYY-MM-DD)
df['Code Date'] = df['Code Date'].dt.strftime('%Y-%m-%d').fillna('')
df['Receipt Date'] = df['Receipt Date'].dt.strftime('%Y-%m-%d').fillna('')
df['Inventory Entry Date'] = df['Inventory Entry Date'].dt.strftime('%Y-%m-%d').fillna('')

df['CurrentDate'] = creation_date

df.rename(columns={'Code Date': 'CodeDate', 'Qty on Hand': 'Qty', 'Count Unit':'Unit',
                   'Alt 1 Qty':'Alt1Qty','Alt 1 Qty Unit':'Alt1Unit',
                   'Inventory Entry Date':'EntryDate', 'Header Ref':'HeaderRef',
                   'Receipt Date':'ReceiptDate','Piece No':'PieceNo',
                   'Inv Status':'Status'}, inplace=True)
