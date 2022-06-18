from __future__ import print_function

import logging

import grpc

import SafeEntry_pb2

import SafeEntry_pb2_grpc

from location_scrap import random_location

#TO-DO implement remote access MOH client here 
class SafeEntryMOH(object):
    def __init__(self):
        # create a gRPC channel to connect to server
        self.channel = grpc.insecure_channel("localhost:50051")
        # indicate the stub that connect to the server 
        self.stub = SafeEntry_pb2_grpc.SafeEntryStub(self.channel)
        
    def updateLocation(self):
        pass
    
if __name__ == "__main__":
    logging.basicConfig()
    # initial user client object
    client = SafeEntryMOH()
    # main loop
    user_decision=''
    while user_decision != "e" and user_decision != "E": 
        client.run()
        user_decision = str(input("Press E to exit the program or other other button to continue.\n"))