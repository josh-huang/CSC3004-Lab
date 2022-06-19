import pandas as pd
location=[]
df = pd.read_csv(f'client_file/Notail.csv')
print(df.loc[df['Current Check In status'] == 0])

for index, row in df.iterrows():
    print(index, row['Current Check In status'])
    
for index, row in df.loc[df['Current Check In status'] == 0].iterrows():
    location.append(row['Location'])
print(location)