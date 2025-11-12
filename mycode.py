import pandas as pd
import os 

# Creating a sample DataFrame 
data = {
    "Name":['Alice','Bob','Charlie'],
    'Age':[25,30,35],
    'City':['New York','Los Angeles','Chicago']
}

df = pd.DataFrame(data)

# Ensuring data directory exists
data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)

# Creatin a file  path
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save the dataframe 
df.to_csv(file_path,index=False)
