from __future__ import print_function
from asyncio import run
from concurrent.futures import thread
from http.client import ResponseNotReady
import logging
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
import threading
from time import sleep

# client check in and check out info will be stored in seperate file with id and name on the file's title 

class SafeEntryClient(object):
    
    def __init__(self, name, id, user_phone):
        # create a gRPC channel to connect to server
        self.channel = grpc.insecure_channel("localhost:50051")
        # indicate the stub that connect to the server 
        self.stub = SafeEntry_pb2_grpc.SafeEntryStub(self.channel)
        # get user name, user id and user phone 
        self.user_name = name
        self.user_id = id
        self.user_phone = user_phone
        # get copy of the lcoation array
        self.temp = random_location[:]
        # initiate the client info file and write header to it 
        self.fieldnames = ['Client_id', 'Client_name', 'Client_phone', 'Location', 'Check In Time', 'Check Out Time', 'Current Check In status']
        
    # run loop   
    def run(self):
        # get choice from user 
        user_choice = 0
        while True:
            user_choice = str(input(f"\nHello {self.user_name}\nWhich function do you wish to perform?\n [1]. Check in\n [2]. Check out\n [3]. Group Check in\n [4]. Group Check out\n [5]. Display the history of visited locations\n [6]. Exit\nEnter your Choice here: "))
            if int(user_choice) > 6 or int(user_choice) < 1: 
                print('Please choose between 1 - 6')
            elif not user_choice.isnumeric():
                print('Please choose number between 1 - 6')
            else: 
                break
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
        elif user_choice == "6":
            # exit the program 
            print('Log out successful.\n')
            exit()
                    
    
    # individual check in function
    def checkIn(self, groupCheckLocation = None):
        # If no group check in, the location will be randomly generated 
        # If group check in is called, the location for check in will follow groupCheckIn location 
        
        if groupCheckLocation is None:
            user_location = random.choice(self.temp)
            self.temp.remove(user_location)
        else:
            user_location = groupCheckLocation
        # Get current time 
        current_time = self.getCurrentTime()
        # Check if the file exists 
        file_exists_client = os.path.isfile(f'client_file/{self.user_id}_{self.user_name}.csv')
        # store the client check in and check out details in the individual csv file 
        with open(f'client_file/{self.user_id}_{self.user_name}.csv', mode='a', newline='') as csv_file:
            if not file_exists_client: 
                writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
                writer.writeheader()
            writer_object = DictWriter(csv_file, fieldnames=self.fieldnames) 
            writer_object.writerow({'Client_id': f'{self.user_id}', 'Location': f'{user_location}','Client_name': f'{self.user_name}','Client_phone': f'{self.user_phone}' ,'Check In Time': f'{current_time}', 'Current Check In status': 0})
        # get response from server 
        sleep(1)
        response = self.stub.checkIn(SafeEntry_pb2.CheckInRequest(name=self.user_name, id=self.user_id, location=user_location, check_in_time=current_time, phone_number = self.user_phone))
        print(f"\n{self.user_name} Response Received: ")
        print(str(response.res))
        
    # individual check out function 
    def checkOut(self):
        # Get current time 
        current_time = self.getCurrentTime()
        # inititate current check in location array 
        current_check_in_location = []
        # check the client file and append the location with check in status = 0 into the array 
        df = pd.read_csv(f'client_file/{self.user_id}_{self.user_name}.csv')
        for index, row in df.loc[df['Current Check In status'] == 0].iterrows():
            current_check_in_location.append(row['Location'])
        # user choose the location that they wish to check out 
        if len(current_check_in_location) != 0: 
            print(f'\n{self.user_name} Type the location that you wish to check out: ')
            # print out the location name in the current_check_in_location list
            for i in current_check_in_location: 
                print (i)
            # user input location they wish to check out
            while True:
                check_out_location = str(input(''))
                if len(check_out_location) == 0:
                    print('Please enter location')
                else:
                    break
            # add check out time and change the current check in status to 1
            for index, row in df.loc[df['Current Check In status'] == 0].iterrows():
                if row['Location'] == check_out_location:
                    df.loc[index, 'Check Out Time'] = current_time
                    df.loc[index, 'Current Check In status'] = 1
            # drop dataframe Unname column 
            df.drop(df.filter(regex="Unname"),axis=1, inplace=True)
            df.to_csv(f'client_file/{self.user_id}_{self.user_name}.csv')
        
            # get response from server 
            sleep(1)
            response = self.stub.checkOut(SafeEntry_pb2.CheckOutRequest(name=self.user_name, id=self.user_id, location=check_out_location, check_out_time=current_time))
            print(f"\n{self.user_name} Response Received: ")
            print(str(response.res))
        else:
            print('You have no location to check out.')
        
    # group check out function 
    def groupCheckIn(self):
        # get response from server 
        response = self.stub.groupCheckIn(self.get_input_from_user_checkin())
        print(f"\n{self.user_name} Response Received: ")
        print(str(response.res))
    
    # group check out function 
    def groupCheckOut(self):
        # get response from server
        response = self.stub.groupCheckOut(self.get_input_from_user_checkout())
        print(f"\n{self.user_name} Response Received: ")
        print(str(response.res))
        
    # function to return all the location that visited by the client 
    def getAllLocation(self):
        # send get lcoation request to server 
        location_request = SafeEntry_pb2.LocationRequest(user_name=self.user_name, user_id=self.user_id)
        response = self.stub.getLocation(location_request)
        # print out the response from server 
        for reply in response:
            print(reply) 
        
    # get current time function
    def getCurrentTime(self):
        now = datetime.now()
        # get current time  
        current_time = now.strftime("%d/%m/%Y %H:%M:%S")
        return current_time
    
    # get user input for groupCheckIn function
    def get_input_from_user_checkin(self):
        # user check in location (use random location to simulate)
        user_location = random.choice(self.temp)
        self.temp.remove(user_location)
        # get current time 
        current_time = self.getCurrentTime()
        name = ''
        # self check in
        self.checkIn(groupCheckLocation=user_location)
        # loop to get the name, id and phone number for each group memeber
        while name != "q":
            name, id, phone = input(f'{self.user_name} Enter your family member name (enter _ if space), id and phone that you wish to check in or type \'q 1 1\' if finished inputting: \n').split()
            if name != 'q' and id != '1' and phone != '1':
                file_exists = os.path.isfile(f'client_file/{id}_{name}.csv')
                with open(f'client_file/{id}_{name}.csv', mode='a+', newline='') as csv_file:
                    if not file_exists: 
                        writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
                        writer.writeheader()
                    writer_object = DictWriter(csv_file, fieldnames=self.fieldnames)
                    # append the check in info to the client file 
                    writer_object.writerow({'Client_id': f'{id}', 'Location': f'{user_location}','Client_name': f'{name}', 'Client_phone': f'{phone}' ,'Check In Time': f'{current_time}', 'Current Check In status': 0})
                groupCheckInRequest = SafeEntry_pb2.GroupCheckInRequest(name=name, id=id, location=user_location, check_in_time=current_time, phone_number=phone)
                yield groupCheckInRequest
                time.sleep(1)
    
    # get user input for groupCheckOut function    
    def get_input_from_user_checkout(self):
        # get current time 
        current_time = self.getCurrentTime()
        name = ''
        # user input the user name and user id that they help to check out
        while name != "q":
            current_check_in_location = []
            name, id = input(f'{self.user_name} Enter your family member name (enter _ if space) and id that you wish to check out or type \'q 1\' if finished inputting: \n').split()
            if name != 'q' and id != '1':
                df = pd.read_csv(f'client_file/{id}_{name}.csv')
                for index, row in df.loc[df['Current Check In status'] == 0].iterrows():
                    current_check_in_location.append(row['Location'])
                # user select the location that they want to check out 
                print('Please type the location that you want to check out: ')
                for i in current_check_in_location:
                    print(i)
                check_out_location = input("")
                df = pd.read_csv(f'client_file/{id}_{name}.csv')
                for index, row in df.loc[df['Current Check In status'] == 0].iterrows():
                    if row['Location'] == check_out_location:
                        df.loc[index, 'Check Out Time'] = current_time
                        df.loc[index, 'Current Check In status'] = 1
                # drop dataframe Unname column 
                df.drop(df.filter(regex="Unname"),axis=1, inplace=True)
                df.to_csv(f'client_file/{id}_{name}.csv')
                groupCheckOutRequest = SafeEntry_pb2.GroupCheckOutRequest(name=name, id=id, location=check_out_location, check_out_time=current_time)
                yield groupCheckOutRequest
                time.sleep(1)

            
# function to generate client object
def run_client(user_name, user_id, user_phone):
    client = SafeEntryClient(user_name, user_id, user_phone)
    # main loop
    user_decision=''
    while user_decision != "e" and user_decision != "E": 
        client.run()
        user_decision = str(input(f"\nHello {user_name} Press E to exit the program or other button to continue.\n"))
    print('Log out successful.\n')

# function to test concurrency     
def test_concurrency():
    client1 = SafeEntryClient("test1", '12345', '6592786512')
    client2 = SafeEntryClient("test2", '23456', '6592786513')
    user_choice = input('\nEnter 1 to test concurrency for checkin or other ket for checkout: ')
    if user_choice == "1":
        t1 = threading.Thread(target=client1.checkIn)
        t2 = threading.Thread(target=client2.checkIn)
        t1.start()
        t2.start()
    elif user_choice == "2":
        t1 = threading.Thread(target=client1.checkOut)
        t2 = threading.Thread(target=client2.checkOut)
        t1.start()
        t2.start()
    
if __name__ == "__main__":
    logging.basicConfig()
    # user input the number of concurrent user to use the system
    user_name_list = []
    user_id_list = []
    user_phone_list = []
    user_choice = input('Enter 1 to test concurrency or other key to run the program normally: ')
    if user_choice == "1":
        test_concurrency()
    else:
        user_num = int(input('Enter the number of user: '))
        for i in range(user_num):
            print(f'User No.{i+1}: ')
            while True: 
                # user input name, id and phone number 
                user_name = str(input('Enter the name: '))
                user_id = str(input('Enter the id: '))
                user_phone = str(input('Enter the phone number(add 65 at the front eg. 6592375431): '))
                # validation check for user name and user phone 
                if not user_name.isalpha():
                    print("Name must contains alphabets only. Please try again\n")
                elif not user_phone.isnumeric():
                    print("Phone must contains numbers only. Please try again\n")
                else:
                    break
            user_name_list.append(user_name)
            user_id_list.append(user_id)
            user_phone_list.append(user_phone)
            # initiate user client object
        for i in range(len(user_name_list)):
            t = threading.Thread(target=run_client, args=(user_name_list[i], user_id_list[i], user_phone_list[i]))
            print(f'\n{user_name_list[i]} Thread started: ')
            t.start()
            t.join()
        print('All user has signed out.\n')

    
        
                
        

   

  
        
    