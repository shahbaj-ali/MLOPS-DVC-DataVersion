import pandas as pd
import os 

# Creating a sample DataFrame 
data = {
    "Name":['Alice','Bob','Charlie'],
    'Age':[25,30,35],
    'City':['New York','Los Angeles','Chicago']
}

df = pd.DataFrame(data)

# adding new row in the  dataframe
new_row_loc = {'Name':'GF1', 'Age':20, 'City':'City1'}
df.loc[len(df.index)] = new_row_loc 

# adding new row in the  dataframe
new_row_loc2 = {'Name':'GF2', 'Age':30, 'City':'City2'}
df.loc[len(df.index)] = new_row_loc2 

# Ensuring data directory exists
data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)

# Creatin a file  path
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save the dataframe 
df.to_csv(file_path,index=False)



