from __future__ import print_function

import logging

import grpc

import SafeEntry_pb2

import SafeEntry_pb2_grpc

from location_scrap import random_location

from datetime import datetime

import random

all_location = []

current_location = []

def run():
    
    with grpc.insecure_channel("localhost:50051") as channel:
        
        # get user name and id 
        user_name = str(input('Enter your name: '))
        user_id = int(input('\nEnter your id: '))
        
        # indicate the stub 
        stub = SafeEntry_pb2_grpc.SafeEntryStub(channel)
        
        while True: 
        # check in and check out for individual and group 
            user_choice = str(input("\nWhich function do you wish to perform?\n [1]. Check in\n [2]. Check out\n [3]. Group Check in\n [4]. Group Check out\n [5]. Display all the locations\n"))
            
            # user choose Check in function 
            if user_choice == "1":
                # user check in location (use random location to simulate)
                user_location = random.choice(random_location)
                # append the location in all_location and current_location array 
                all_location.append(user_location)
                current_location.append(user_location)
                # get current time 
                current_time = getCurrentTime()
                response = stub.checkIn(SafeEntry_pb2.CheckInRequest(name=user_name, id=user_id, location=user_location, check_in_time=current_time))
                print(str(response.res))
            
            # user choose Check out function 
            elif user_choice == "2":
                # user check out location in the current location array 
                check_out_location = random.choice(current_location)
                current_time = getCurrentTime()
                current_location.remove(check_out_location)
                response = stub.checkIn(SafeEntry_pb2.CheckInRequest(name=user_name, id=user_id, location=check_out_location, check_in_time=current_time))
                print(str(response.res))
            
            # user choose Group check in function 
            elif user_choice == "3":
                # group check in function 
                pass
            
            # user choose Group check out function 
            elif user_choice == "4":
                # group check out function 
                pass
            
            # user choose display location history function 
            elif user_choice == "5":
                # display location function  
                pass
            
            # receive sms notification if visited covid places 
        

        response = stub.Multiply(SafeEntry_pb2.Request(x=5, y=6))
        print("The result of Add Function is: " + str(response.res))

        
# function to return all the location that visited by the client 
def getAllLocation():
    # get location from the list 
    for i in all_location:
        print(str(i)+'\n')

def getCurrentTime():
    now = datetime.now()
        # get current time  
    current_time = now.strftime("%H:%M:%S")
    return current_time

if __name__ == "__main__":
    logging.basicConfig()
    run()
