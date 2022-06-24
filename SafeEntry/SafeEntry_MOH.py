from __future__ import print_function
from http.client import ResponseNotReady
import logging
from tabnanny import check
import grpc
import SafeEntry_pb2
import SafeEntry_pb2_grpc
from location_scrap import random_location
from datetime import datetime
from csv import DictWriter
import pandas as pd
import time 
from dateutil import parser


class SafeEntryMOH(object):
    def __init__(self,location_name,visit_date,checkOut_date):
        # create a gRPC channel to connect to server
        self.channel = grpc.insecure_channel("localhost:50051")
        # indicate the stub that connect to the server 
        self.stub = SafeEntry_pb2_grpc.SafeEntryStub(self.channel)

         # declare covid location, date, time
        self.location_name = location_name
        self.visit_date = visit_date
        self.checkOut_date = checkOut_date

    # run update location function 
    def run(self):
        self.updateLocation() #covid_location,covid_date,covid_time

    def updateLocation(self): #,covid_location,covid_date,covid_time
        print("Location: " + self.location_name)
        # receive response from server
        response = self.stub.updateLocation(SafeEntry_pb2.MOHRequest(
            location_name = self.location_name, visit_date = self.visit_date, checkOut_date = self.checkOut_date))
        print("Response Received: ")
        print(str(response.res))

    
if __name__ == "__main__":
    logging.basicConfig()
    # declare the format of the date 
    format = "%d/%m/%Y %H:%M"
    # main loop 
    user_decision=''
    while user_decision != "e" and user_decision != "E":
        while True:
            # user input location name, visit date and checkout date of the covid location 
            location_name = str(input("\nEnter the location: \n"))
            visit_date = str(input("\nDeclare the check-in date and time visted by a COVID-19 case (Format should be: DD/M/YYYY H:MM):\n")) 
            checkOut_date = str(input("Declare check-out date and time visited by a COVID-19 case (Format should be: DD/M/YYYY H:MM):\n"))
            # validation check for visit date and checkout date format 
            try:
                datetime.strptime(visit_date, format)
                datetime.strptime(checkOut_date, format)
                break
            except:
                print("\nInputs dates are not valid, please input the valid date and time")
        
        #and time (combine date and time tgt)
        client = SafeEntryMOH(location_name,visit_date,checkOut_date)
        # main loop
        client.run()
        user_decision = str(input("Press E to exit the program or other other button to continue.\n"))
    