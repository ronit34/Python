import zipfile
import pandas as pd

# with zipfile.ZipFile("mis_data_all_2_2023_1676278870837.zip","r") as zip_ref:
#     zip_ref.extractall("/home/ronit/Desktop/exract_download_report")


count = 54

df = pd.read_excel('/home/ronit/Desktop/download_report/mis_data_all_2_2023.xlsx')

# header_name = "Total"

# header = df[header_name]

column = df[df['Day'] == 'Time']

data = str(column)
data_splitting = data.split(" ")

print(data_splitting[-1])