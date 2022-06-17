from __future__ import print_function

import logging

import grpc

import SafeEntry_pb2

import SafeEntry_pb2_grpc

from location_scrap import random_location

from datetime import datetime

import random


class SafeEntryClient(object):
    def __init__(self, name, id):
        # create a gRPC channel to connect to server
        self.channel = grpc.insecure_channel("localhost:50051")
        # indicate the stub that connect to the server 
        self.stub = SafeEntry_pb2_grpc.SafeEntryStub(self.channel)
        # get user name and user id 
        self.user_name = name
        self.user_id = id
        # initate one arrays to store all locations visited by client and one array to store current locations
        self.all_location = []
        self.current_location = []
        
    def run(self):
        user_choice = str(input("\nWhich function do you wish to perform?\n [1]. Check in\n [2]. Check out\n [3]. Group Check in\n [4]. Group Check out\n [5]. Display all the locations\n"))
            
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
        user_location = random.choice(random_location)
        # append the location in all_location and current_location array 
        self.all_location.append(user_location)
        self.current_location.append(user_location)
        # get current time 
        current_time = self.getCurrentTime()
        response = self.stub.checkIn(SafeEntry_pb2.CheckInRequest(name=user_name, id=user_id, location=user_location, check_in_time=current_time))
        print(str(response.res))
        
    # individual check out function 
    def checkOut(self):
        check_out_location = random.choice(self.current_location)
        current_time = self.getCurrentTime()
        self.current_location.remove(check_out_location)
        response = self.stub.checkIn(SafeEntry_pb2.CheckInRequest(name=user_name, id=user_id, location=check_out_location, check_in_time=current_time))
        print(str(response.res))
        
    # group check out function 
    def groupCheckIn(self):
        pass
    
    # group check out function 
    def groupCheckOut(self):
        pass
        
    # function to return all the location that visited by the client 
    def getAllLocation(self):
        # get location from the list 
        for i in self.all_location:
            print(str(i)+'\n')
            
    # get current time function
    def getCurrentTime(self):
        now = datetime.now()
            # get current time  
        current_time = now.strftime("%H:%M:%S")
        return current_time


if __name__ == "__main__":
    logging.basicConfig()
    # get user creditienal 
    user_name = str(input('Enter your name: '))
    user_id = int(input('Enter your id: '))
    # initial user client object
    client = SafeEntryClient(user_name, user_id)
    while True: 
        client.run()
        
    