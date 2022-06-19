from __future__ import print_function
from http.client import ResponseNotReady

import logging
from tabnanny import check

import grpc

import SafeEntry_pb2

import SafeEntry_pb2_grpc

from location_scrap import random_location

from datetime import datetime

import random

import csv

from csv import DictWriter

import pandas as pd


class SafeEntryClient(object):
    def __init__(self, name, id):
        # create a gRPC channel to connect to server
        self.channel = grpc.insecure_channel("localhost:50051")
        # indicate the stub that connect to the server 
        self.stub = SafeEntry_pb2_grpc.SafeEntryStub(self.channel)
        # get user name and user id 
        self.user_name = name
        self.user_id = id
        self.temp = random_location[:]
        with open(f'client_file/{self.user_name}.csv', mode='w') as csv_file:
            self.fieldnames = ['Client_id', 'Client_name', 'Location', 'Check In Time', 'Check Out Time', 'Current Check In status']
            writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
            writer.writeheader()
        
    def run(self):
        user_choice = str(input("\n\nWhich function do you wish to perform?\n [1]. Check in\n [2]. Check out\n [3]. Group Check in\n [4]. Group Check out\n [5]. Display the history of visited locations\n"))
            
        # user choose Check in function 
        if user_choice == "1":
            # call local check in function
            self.checkIn()
       
        # user choose Check out function 
        elif user_choice == "2":
            # user check out location in the current location array 
            self.checkOut()
        
        # user choose Group check in function 
        elif user_choice == "3":
            # group check in function 
            self.groupCheckIn()
        
        # user choose Group check out function 
        elif user_choice == "4":
            # group check out function 
            self.groupCheckOut()
        
        # user choose display location history function 
        elif user_choice == "5":
            # display location function  
            self.getAllLocation()
    
    # individual check in function
    def checkIn(self):
        # user check in location (use random location to simulate)
        user_location = random.choice(self.temp)
        self.temp.remove(user_location)
        # get current time 
        current_time = self.getCurrentTime()
        # store the client check in and check out details in the {request.name} csv file 
        with open(f'client_file/{self.user_name}.csv', mode='a', newline='') as csv_file:
            writer_object = DictWriter(csv_file, fieldnames=self.fieldnames)
            writer_object.writerow({'Client_id': f'{self.user_id}', 'Location': f'{user_location}','Client_name': f'{self.user_name}', 'Check In Time': f'{current_time}', 'Current Check In status': 0})
        # get response from server 
        response = self.stub.checkIn(SafeEntry_pb2.CheckInRequest(name=self.user_name, id=self.user_id, location=user_location, check_in_time=current_time))
        print("Response Received: ")
        print(str(response.res))
        
    # individual check out function 
    def checkOut(self):
        # call current time function 
        current_time = self.getCurrentTime()
        current_check_in_location = []
        # select one of the current location to perform check out function 
        df = pd.read_csv(f'client_file/{self.user_name}.csv')
        for index, row in df.loc[df['Current Check In status'] == 0].iterrows():
            current_check_in_location.append(row['Location'])
        check_out_location = random.choice(current_check_in_location)
        
        for index, row in df.loc[df['Current Check In status'] == 0].iterrows():
            if row['Location'] == check_out_location:
                df.loc[index, 'Check Out Time'] = current_time
                df.loc[index, 'Current Check In status'] = 1
        # drop dataframe Unname column 
        df.drop(df.filter(regex="Unname"),axis=1, inplace=True)
        df.to_csv(f'client_file/{self.user_name}.csv')
        
        # get response from server 
        response = self.stub.checkOut(SafeEntry_pb2.CheckOutRequest(name=user_name, id=user_id, location=check_out_location, check_out_time=current_time))
        print("Response Received: ")
        print(str(response.res))
        
    # group check out function 
    def groupCheckIn(self):
        user_location = random.choice(random_location)

        # get current time 
        current_time = self.getCurrentTime()
        
        # get response from server 
        response = self.stub.checkIn(SafeEntry_pb2.GroupCheckInRequest(name=user_name, id=user_id, location=user_location, check_in_time=current_time))
        print("Response Received: ")
        print(str(response.res))
    
    # group check out function 
    def groupCheckOut(self):
        pass
        
    # function to return all the location that visited by the client 
    def getAllLocation(self):
        location_request = SafeEntry_pb2.GroupCheckInRequest(name=self.user_name, id=self.user_id)
        response = self.stub.getLocation(location_request)
        
        for reply in response:
            print(reply)
            
    # get current time function
    def getCurrentTime(self):
        now = datetime.now()
        # get current time  
        current_time = now.strftime("%d/%m/%Y %H:%M:%S")
        return current_time


if __name__ == "__main__":
    logging.basicConfig()
    # get user creditienal 
    user_name = str(input('Enter your name: '))
    user_id = int(input('Enter your id: '))
    # initial user client object
    client = SafeEntryClient(user_name, user_id)
    # main loop
    user_decision=''
    while user_decision != "e" and user_decision != "E": 
        client.run()
        user_decision = str(input("Press E to exit the program or other button to continue.\n"))
        
    