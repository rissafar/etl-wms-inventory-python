from extract import extract_inventory
from transform import clean_inventory
from load import load_inventory

def run():
    df = extract_inventory()
    df_clean = clean_inventory(df)
    load_inventory(df_clean)

if __name__ == "__main__":
    run()
