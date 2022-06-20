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
import time 
import os.path

#TO-DO implement remote access MOH client here 
class SafeEntryMOH(object):
    def __init__(self,location_name,visit_date,checkOut_date):
        # create a gRPC channel to connect to server
        self.channel = grpc.insecure_channel("localhost:50051")
        # indicate the stub that connect to the server 
        self.stub = SafeEntry_pb2_grpc.SafeEntryStub(self.channel)

         # get covid location, date, time
        self.location_name = location_name
        self.visit_date = visit_date
        self.checkOut_date = checkOut_date


        

    def run(self):
        self.updateLocation() #covid_location,covid_date,covid_time

    def updateLocation(self): #,covid_location,covid_date,covid_time
        print("Location: " + self.location_name)

        # get response from server 
        response = self.stub.updateLocation(SafeEntry_pb2.MOHRequest(
            location_name = self.location_name, visit_date = self.visit_date, checkOut_date = self.checkOut_date))
        print("Response Received: ")
        print(str(response.res))

    
if __name__ == "__main__":
    logging.basicConfig()

    # get copy of the lcoation array
    temp = random_location[:]
    location_name = random.choice(temp)
    temp.remove(location_name)
    
    print("\nLocation: " + location_name)
    visit_date = str(input("\nDeclare the check-in date and time visted by a COVID-19 case (Format should be: DD/M/YYYY H:MM AM/PM):\n")) 
    checkOut_date = str(input("Declare check-out date and time visited by a COVID-19 case (Format should be: DD/M/YYYY H:MM AM/PM):\n"))
    #and time (combine date and time tgt)

    # initial user client object
    client = SafeEntryMOH(location_name,visit_date,checkOut_date)

    # main loop
    user_decision=''
    while user_decision != "e" and user_decision != "E": 
        client.run()
        user_decision = str(input("Press E to exit the program or other other button to continue.\n"))