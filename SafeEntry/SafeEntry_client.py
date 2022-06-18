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


class SafeEntryClient(object):
    def __init__(self, name, id):
        # create a gRPC channel to connect to server
        self.channel = grpc.insecure_channel("localhost:50051")
        # indicate the stub that connect to the server 
        self.stub = SafeEntry_pb2_grpc.SafeEntryStub(self.channel)
        # get user name and user id 
        self.user_name = name
        self.user_id = id
        
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
        user_location = random.choice(random_location)
        # append the location in all_location and current_location array 
        # self.all_location.append(user_location)
        # self.current_location.append(user_location)
        # get current time 
        current_time = self.getCurrentTime()
        # store the client check in and check out details in the {request.id}_{request.name}_history text file 
        with open(f"client_file/{self.user_id}_{self.user_name}_history.txt", "a+") as file_object:
            # Move read cursor to the start of file.
            file_object.seek(0)
            # If file is not empty then append '\n'
            data = file_object.read(100)
            if len(data) > 0 :
                file_object.write("\n")
            # Append text at the end of file
            file_object.write(f"{user_location}  {current_time}  Check In")
        # store the client current locations in the {request.id}_{request.name}_current text file    
        with open(f"client_file/{self.user_id}_{self.user_name}_current.txt", "a+") as file_object:
            # Move read cursor to the start of file.
            file_object.seek(0)
            # If file is not empty then append '\n'
            data = file_object.read(100)
            if len(data) > 0 :
                file_object.write("\n")
            # Append text at the end of file
            file_object.write(f"{user_location}")
        # store the client all locations in the {request.id}_{request.name}_all text file    
        with open(f"client_file/{self.user_id}_{self.user_name}_all.txt", "a+") as file_object:
            # Move read cursor to the start of file.
            file_object.seek(0)
            # If file is not empty then append '\n'
            data = file_object.read(100)
            if len(data) > 0 :
                file_object.write("\n")
            # Append text at the end of file
            file_object.write(f"{user_location}")
        # get response from server 
        response = self.stub.checkIn(SafeEntry_pb2.CheckInRequest(name=user_name, id=user_id, location=user_location, check_in_time=current_time))
        print("Response Received: ")
        print(str(response.res))
        
    # individual check out function 
    def checkOut(self):
        # call current time function 
        current_time = self.getCurrentTime()
        current_check_in_location = []
        # select one of the current location to perform check out function 
        with open(f"client_file/{self.user_id}_{self.user_name}_current.txt", "r+") as file_object:
            lines = file_object.readlines()
            for line in lines:
                current_check_in_location.append(line)
        # with open(f"client_file/{self.user_id}_{self.user_name}_history.txt", "r+") as file_object:
        #     lines = file_object.readlines()
        #     for line in lines:
        #         if "Check Out" not in line:
        #             current_check_in_location.append(line.split("  ",1)[0])
        # 
        with open(f"client_file/{self.user_id}_{self.user_name}_history.txt", "a") as file_object1:
            check_out_location = random.choice(current_check_in_location)
            file_object1.seek(0)
            # file_object1.write("\n")
            file_object1.write(f"\n{check_out_location}  {current_time}  Check Out")
            
        with open(f"client_file/{self.user_id}_{self.user_name}_current.txt", "r") as file_object2:
            lines = file_object2.readlines()
        
        with open(f"client_file/{self.user_id}_{self.user_name}_current.txt", "w") as file_object3:
            for line in lines:
                if str(check_out_location) not in line:
                    file_object3.writelines(line)
                    
        # get response from server 
        response = self.stub.checkOut(SafeEntry_pb2.CheckOutRequest(name=user_name, id=user_id, location=check_out_location, check_out_time=current_time))
        print("Response Received: ")
        print(str(response.res))
        
    # group check out function 
    def groupCheckIn(self):
        user_location = random.choice(random_location)
        # append the location in all_location and current_location array 
        self.all_location.append(user_location)
        self.current_location.append(user_location)
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
        location_request = SafeEntry_pb2.GroupCheckInRequest(name=user_name)
        response = self.stub.getLocation(location_request)
        
        for reply in response:
            print(reply + '\n')
            
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
    # main loop
    user_decision=''
    while user_decision != "e" and user_decision != "E": 
        client.run()
        user_decision = str(input("Press E to exit the program or other other button to continue.\n"))
        
    