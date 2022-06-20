from concurrent import futures
import logging
import grpc
import SafeEntry_pb2
import SafeEntry_pb2_grpc
from location_scrap import random_location
from datetime import datetime
import csv
from csv import DictWriter
import pandas as pd
import os.path
import time

# two files to be created: client_info.csv and location_file.csv
# [client_info.csv]: 'Client ID': client ID, 'Client Name': client name, 'Location': checked in lcoation name, 
# 'Check In Time': checked in time, 'Check Out Time: blank if no check out from client', 'Current Check in Status': 0 indicates only 
# [location_info.csv]: 'Location': location name

class SafeEntry(SafeEntry_pb2_grpc.SafeEntryServicer):
    
    def __init__(self):
        # initate the field name for both csv file 
        self.fieldnames = ['Unname', 'Client ID', 'Client Name', 'Location', 'Check In Time', 'Check Out Time', 'Current Check In status']
        self.fieldnames2 = ['Unname', 'Location', 'Checked In Client ID', 'Check In Time', 'Check Out Time', 'Current Location Covid Status', 'Covid Affected Date and Time']
        
    # individual check in function 
    def checkIn(self, request, context):
        try:
            # print out the request message
            print("Check in request received: ")
            print(request)
            
            # Check if files exists
            file_exists_client = os.path.isfile(f'server_file/client_info.csv')
            file_exists_location = os.path.isfile(f'server_file/location_info.csv')
            
            # append client check in infomation in the client_info.csv
            with open(f'server_file/client_info.csv', mode='a', newline='') as csv_file:
                # if file not exists, write header 
                if not file_exists_client: 
                    writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
                    writer.writeheader()
                # write the client info into client_info file     
                writer_object = DictWriter(csv_file, fieldnames=self.fieldnames)
                writer_object.writerow({'Client ID': f'{request.id}', 'Location': f'{request.location}','Client Name': f'{request.name}', 'Check In Time': f'{request.check_in_time}', 'Current Check In status': 0})
            
            # append location check in infomation in the client_info.csv
            with open(f'server_file/location_info.csv', mode='a', newline='') as csv_file:
                # if file not exists, write header
                if not file_exists_location: 
                    writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames2)
                    writer.writeheader()
                # write the client info into location_info file   
                writer_object = DictWriter(csv_file, fieldnames=self.fieldnames2)
                writer_object.writerow({'Checked In Client ID': f'{request.id}', 'Location': f'{request.location}', 'Check In Time': f'{request.check_in_time}', 'Current Location Covid Status': 0})
            
            # reply message to be sent to client 
            reply_message = 'Check In ' + request.location + ' successful' 
        
        except: 
            # reply message to be sent to client 
            reply_message = 'Check In ' + request.location + ' failed' 
            
        return SafeEntry_pb2.CheckInReply(res=reply_message)
    
    
    # individual check out function 
    def checkOut(self, request, context):
        # print out the request message
        try: 
            print("Check out request received: ")
            print(request)
            # add the check out details in client_info.txt
            df = pd.read_csv(f'server_file/client_info.csv')
            for index, row in df.iterrows():
                if row['Location'] == request.location and row['Client ID'] == request.id:
                    df.loc[index, 'Check Out Time'] = request.check_out_time
                    df.loc[index, 'Current Check In status'] = 1
            # drop dataframe Unname column 
            df.drop(df.filter(regex="Unname"),axis=1, inplace=True)
            df.to_csv(f'server_file/client_info.csv')
                    
            df_location = pd.read_csv(f'server_file/location_info.csv')
            for index, row in df_location.iterrows():
                if row['Location'] == request.location and row['Checked In Client ID'] == request.id:
                    df_location.loc[index, 'Check Out Time'] = request.check_out_time
            # drop dataframe Unname column 
            df_location.drop(df_location.filter(regex="Unname"),axis=1, inplace=True)
            df_location.to_csv(f'server_file/location_info.csv')
                                
            reply_message = 'Check out ' + request.location + ' successful'
            
        except:
            reply_message = 'Check out ' + request.location + ' failed'
           
        return SafeEntry_pb2.CheckOutReply(res=reply_message)
            
    
    # group check in function 
    def groupCheckIn(self, request_iterator, context):
        try: 
            for request in request_iterator:
                # print out the request message
                print("Check out request received: ")
                print(request)
                check_in_location = request.location
                # Check if files exists in the folder
                file_exists_client = os.path.isfile(f'server_file/client_info.csv')
                file_exists_location = os.path.isfile(f'server_file/location_info.csv')
                
                # append client check in infomation in the client_info.csv
                with open(f'server_file/client_info.csv', mode='a', newline='') as csv_file:
                    
                    if not file_exists_client: 
                        writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
                        writer.writeheader()
                        
                    writer_object = DictWriter(csv_file, fieldnames=self.fieldnames)
                    writer_object.writerow({'Client ID': f'{request.id}', 'Location': f'{request.location}','Client Name': f'{request.name}', 'Check In Time': f'{request.check_in_time}', 'Current Check In status': 0})
                
                # append location check in infomation in the client_info.csv
                with open(f'server_file/location_info.csv', mode='a', newline='') as csv_file:
                    
                    if not file_exists_location: 
                        writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames2)
                        writer.writeheader()
                        
                    writer_object = DictWriter(csv_file, fieldnames=self.fieldnames2)
                    writer_object.writerow({'Checked In Client ID': f'{request.id}', 'Location': f'{request.location}', 'Check In Time': f'{request.check_in_time}', 'Current Location Covid Status': 0})
            # reply message to be sent to client 
            reply_message = 'Group Check In ' + check_in_location + ' successful' 
        except: 
            # reply message to be sent to client 
            reply_message = 'Group Check In ' + check_in_location + ' failed' 
        return SafeEntry_pb2.GroupCheckInReply(res=reply_message)
    
    # group check out function 
    def groupCheckOut(self, request_iterator, context):
        try:
            for request in request_iterator:
                # print out the request message
                print("Check out request received: ")
                print(request)
                
                df = pd.read_csv(f'server_file/client_info.csv')
                for index, row in df.iterrows():
                    if row['Location'] == request.location and row['Client ID'] == request.id:
                        df.loc[index, 'Check Out Time'] = request.check_out_time
                        df.loc[index, 'Current Check In status'] = 1
                # drop dataframe Unname column 
                df.drop(df.filter(regex="Unname"),axis=1, inplace=True)
                df.to_csv(f'server_file/client_info.csv')
                    
                df_location = pd.read_csv(f'server_file/location_info.csv')
                for index, row in df_location.iterrows():
                    if row['Location'] == request.location and row['Checked In Client ID'] == request.id:
                        df_location.loc[index, 'Check Out Time'] = request.check_out_time
                # drop dataframe Unname column 
                df_location.drop(df_location.filter(regex="Unname"),axis=1, inplace=True)
                df_location.to_csv(f'server_file/location_info.csv')
            
            # reply message to be sent to client 
            reply_message = 'Group Check Out successful' 
        except:
            # reply message to be sent to client 
            reply_message = 'Group Check Out failed' 
        return SafeEntry_pb2.GroupCheckOutReply(res=reply_message)
    
    # MOH update location 
    def updateLocation(self, request, context):
        # TO-DO implement update location function here 
        print("Update location status request received: ")
        print(request)
        
        # update location covid status to 1 and added affected date 
        df_location = pd.read_csv(f'server_file/location_info.csv')
        for index, row in df_location.iterrows():
            if row['Location'] == request.location:
                df_location.loc[index, 'Current Location Covid Status'] = 1
                df_location.loc[index, 'Covid Affected Date and Time'] = request.visit_date
        # drop dataframe Unname column 
        df_location.drop(df_location.filter(regex="Unname"),axis=1, inplace=True)
        df_location.to_csv(f'server_file/location_info.csv')
        
        return SafeEntry_pb2.MOHReply(res='Update information have been received.')
    
    # send sms notification to the clients who has visited covid places
    def getNotification(self, request, context):
        pass
    
    # get all the location that visited by the client
    def getLocation(self, request, context):
        # print out the get location request message
        print("Get location request received: ")
        print(request)
        
        user_all_location = []
        # read csv file and append all the location in the user_all_location array 
        df = pd.read_csv(f'server_file/client_info.csv')
        for index, row in df.loc[df['Client Name'] == request.user_name].iterrows():
            user_all_location.append(row['Location'])
        
        for i in user_all_location:
            locationReply = SafeEntry_pb2.LocationReply()
            locationReply.location_name = i
            yield locationReply
            time.sleep(2)
             
    # get current time function
    def getCurrentTime(self):
        now = datetime.now()
            # get current time  
        current_time = now.strftime("%d/%m/%Y %H:%M:%S")
        return current_time

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5), maximum_concurrent_rpcs=10)
    #add SafeEntry Servicier to the server
    SafeEntry_pb2_grpc.add_SafeEntryServicer_to_server(SafeEntry(), server)            
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()