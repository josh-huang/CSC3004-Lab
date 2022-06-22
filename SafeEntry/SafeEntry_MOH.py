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
from dateutil import parser


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

        #endless loop
        # visit_Date_valid = self.validate(self.visit_date)
        # checkout_Date_valid = self.validate(self.checkOut_date)
        # while (visit_Date_valid == True and checkout_Date_valid == True):
        #     # get response from server 
        response = self.stub.updateLocation(SafeEntry_pb2.MOHRequest(
            location_name = self.location_name, visit_date = self.visit_date, checkOut_date = self.checkOut_date))
        print("Response Received: ")
        print(str(response.res))
        # else:
        #     print("Inputs dates are not valid, please input the valid date and time.")

# def validate(date_text):
#     # initializing format
#     format = "%d/%m/%Y %H:%M"
#     # checking if format matches the date
#     try:
#         datetime.strptime(date_text, format)
#         return True
#     except ValueError:
#         print("Inputs dates are not valid, please input the valid date and time")
#         return False

    
if __name__ == "__main__":
    logging.basicConfig()
    
    format = "%d/%m/%Y %H:%M"
    
    while True:
        location_name = str(input("\nEnter the location: \n"))
        visit_date = str(input("\nDeclare the check-in date and time visted by a COVID-19 case (Format should be: DD/M/YYYY H:MM):\n")) 
        checkOut_date = str(input("Declare check-out date and time visited by a COVID-19 case (Format should be: DD/M/YYYY H:MM):\n"))
        try:
            datetime.strptime(visit_date, format)
            datetime.strptime(checkOut_date, format)
            break
        except:
            print("\nInputs dates are not valid, please input the valid date and time")
        
    #and time (combine date and time tgt)
    client = SafeEntryMOH(location_name,visit_date,checkOut_date)
    # main loop
    user_decision=''
    while user_decision != "e" and user_decision != "E": 
        client.run()
        user_decision = str(input("Press E to exit the program or other other button to continue.\n"))
    # # main loop
    # user_decision=''
    # while user_decision != "e" and user_decision != "E": 
    #         # initial user client object
    #     try:
    #         visit_Date_valid = SafeEntryMOH.validate(visit_date)
    #         checkout_Date_valid = SafeEntryMOH.validate(checkOut_date)
    #         if (visit_Date_valid == True and checkout_Date_valid == True):
    #             #client = SafeEntryMOH(location_name,visit_date,checkOut_date)
    #             client.run()
    #             user_decision = str(input("Press E to exit the program or other other button to continue.\n"))
    #             print("Declaration passed!")
    #             break
    #         #else:
    #             #cause ENDLESS LOOP
    #             #print("Inputs dates are not valid, please input the valid date and time")
    #             #if visit_date == True and checkout_Date_valid == True:
    #             #client = SafeEntryMOH(location_name,visit_date,checkOut_date)
    #             # initial user client object
    #     except:
    #         print("Declaration failed, please try again")
    #         continue
        
    