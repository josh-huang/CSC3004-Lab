from __future__ import print_function

import logging

import grpc

import SafeEntry_pb2

import SafeEntry_pb2_grpc

from location_scrap import random_location

from datetime import datetime


def run():
    
    with grpc.insecure_channel("localhost:50051") as channel:
        
        now = datetime.now()
        
        # get current time  
        current_time = now.strftime("%H:%M:%S")
        
        # get user name and id 
        user_name = str(input('Enter your name: '))
        user_id = int(input('\nEnter your id: '))
        
        # indicate the stub 
        stub = SafeEntry_pb2_grpc.SafeEntryStub(channel)
        
        # check in and check out for individual and group 
        user_choice = input("\nWhich function do you wish to perform?\n [1]. Check in\n [2]. Check out\n [3]. Group Check in\n [4]. Group Check out\n [4]. Display all the locations\n")
        
        # user choose Check in function 
        if user_choice == "1":
            # check in function 
            response = stub.checkIn(SafeEntry_pb2.CheckInRequest(name=user_name, id=user_id, ))
            print(str(response.res))
        
        # user choose Check out function 
        elif user_choice == "2":
            # check out function 
            response = stub.checkIn(SafeEntry_pb2.CheckInRequest(name=user_name, id=user_id, ))
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
        

        response = stub.Sub(SafeEntry_pb2.Request(x=5, y=6))
        print("The result of Add Function is: " + str(response.res))

        response = stub.Multiply(SafeEntry_pb2.Request(x=5, y=6))
        print("The result of Add Function is: " + str(response.res))

        response = stub.Divide(SafeEntry_pb2.Request(x=5, y=6))
        print("The result of Add Function is: " + str(response.res))
        
# function to return all the location that visited by the client 
def getLocation():
    # get location from the list 
    for i in location_list:
        print(i)


if __name__ == "__main__":
    logging.basicConfig()
    run()
