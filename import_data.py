import pandas as pd
from models import Device 

def import_device_from_excel(file_path):
    
    df = pd.read_excel(file_path)


    for index, row in df.iterrows():
        device = Equipment(
            deviceName=row['Name'],
            deviceType=row['Type'],
            quantity=row['Quantity'],
            audit=row['Audit'],
            location=row['Location'],
            status=row['Status']

        )
        device.save()

if __name__ == "__main__":
    import_device_from_excel("Equipment_Inventory.xlsx")
