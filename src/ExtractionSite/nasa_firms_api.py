import numpy as np
import pandas as pd
import requests
from datetime import date
from io import StringIO
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config.settings import NASA_FIRMS_API_KEY

url_data = f"https://firms.modaps.eosdis.nasa.gov/api/area/csv/{NASA_FIRMS_API_KEY}/MODIS_NRT/world/1/{date.today()}"
def extract_data_modis():

    response = requests.get(url_data)

    if response.status_code == 200:
        print("SUCCESS")
        csv_data = response.text
        df = pd.read_csv(StringIO(csv_data))
        return df
    else:
        print("ERROR IN STATUS CODE")

if __name__ == "__main__":
    # Call the function (note the parentheses!)
    fire_data = extract_data_modis()
    
    if fire_data is not None:
        print("\nDataFrame Info:")
        print(fire_data.info())
        print("\nFirst few rows:")
        print(fire_data.head())
        print(f"\nColumns: {list(fire_data.columns)}")
    else:
        print("Failed to retrieve data")