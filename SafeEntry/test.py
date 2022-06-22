# import pandas as pd
# # location=[]
# # df = pd.read_csv(f'client_file/Notail.csv')
# # print(df.loc[df['Current Check In status'] == 0])

# # for index, row in df.iterrows():
# #     print(index, row['Current Check In status'])
    
# # for index, row in df.loc[df['Current Check In status'] == 0].iterrows():
# #     location.append(row['Location'])
# # print(location)
# df = pd.read_csv(f'server_file/client_info.csv')
# for index, row in df.iterrows():
#     print(row['Location'])
#     print(row['Client ID'])
# import pywhatkit
# pywhatkit.sendwhatmsg("+6597156459", 'Hello:)', 2, 41, wait_time=10)'
from datetime import datetime
from datetime import timedelta 
now = datetime.now()
# get current time  
current_time = now.strftime("%H:%M:%S") 
now += timedelta(seconds=60) 
future_time = now.strftime("%H:%M:%S")
future_hour = future_time.split(':')[0].lstrip('0')
future_minutes = future_time.split(':')[1].lstrip('0')
print(future_minutes) 

