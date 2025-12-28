# read raw data from Excel file 

import pandas as pd # type: ignore
import os
import glob
import win32com.client
from datetime import datetime,timedelta

# Save inventory excel file from email attachment 

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

inbox = outlook.GetDefaultFolder(6)  # Inbox folder
messages = inbox.Items

one_week_ago = (datetime.now() - timedelta(days=7)).strftime("%m/%d/%Y %H:%M %p")

# Restrict: ReceivedTime >= one_week_ago
filter_str = f"[UnRead] = True AND [ReceivedTime] >= '{one_week_ago}'"
recent_messages = messages.Restrict(filter_str)

save_path = r"C:\Users\ParisaFarhand\Documents\My Doc\Training\Power BI\Inventory Analysis"

for msg in recent_messages:
    try:
        msg_date = datetime.fromtimestamp(int(msg.ReceivedTime.timestamp()))
        print(msg.SenderEmailAddress, msg.Subject, msg.UnRead)
        if "Piece Inv. View bi" in msg.Subject and msg.UnRead:
            for att in msg.Attachments:
                att.SaveAsFile(os.path.join(save_path, att.FileName))
                msg.UnRead = False
                msg.save()
    
    except Exception as e:
        # Some items (meeting requests, reports) may not have normal properties
        pass

# Open latest unread excel file
folder_path = r"C:\Users\ParisaFarhand\Documents\My Doc\Training\Power BI\Inventory Analysis"
pattern = os.path.join(folder_path, "Piece Inv. View bi*.xlsx")

# List all matching files
files = glob.glob(pattern)

if not files:
    print("No matching files found.")
else:
    latest_file = max(files, key=os.path.getmtime)
    creation_date = datetime.datetime.fromtimestamp(os.path.getctime(latest_file))
    formatted_date = creation_date.strftime("%Y-%m-%d")
    
    print("Latest file found:")
    print(latest_file, formatted_date)

df = pd.read_excel(latest_file)
