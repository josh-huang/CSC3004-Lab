# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc

import SafeEntry_pb2

import SafeEntry_pb2_grpc

# implement random location array
from location_scrap import random_location

# get time now 


def run():
    
    with grpc.insecure_channel("localhost:50051") as channel:
        
        # indicate the stub 
        stub = SafeEntry_pb2_grpc.SafeEntryStub(channel)
        
        # check in and check out for individual and group 
        user_choice = input("Which function do you wish to perform? ")
        
        if user_choice == "1":
            # check in function 
            pass
            
        elif user_choice == "2":
            # check out function 
            pass
        
        elif user_choice == "3":
            # group check in function 
            pass
        
        elif user_choice == "4":
            # group check out function 
            pass
        
        elif user_choice == "5":
            # display location function  
            pass
        
        # receive sms notification if visited covid places 
        
        response = stub.Add(SafeEntry_pb2.Request(x=5, y=6))
        print("The result of Add Function is: " + str(response.res))

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
