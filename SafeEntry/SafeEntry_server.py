from concurrent import futures

import logging

import grpc

import SafeEntry_pb2

import SafeEntry_pb2_grpc

from location_scrap import random_location

from datetime import datetime

# location_info dictionary: key: Location name value: array[id]
location_info= {}

# covid location array to store covid locations
covid_location = []

class SafeEntry(SafeEntry_pb2_grpc.SafeEntryServicer):
    
    # individual check in function 
    def checkIn(self, request, context):
        # print out the request message
        print("Check in request received: ")
        print(request)
        # store the client check in details in the {request.id}_{request.name}_info text file 
        with open(f"server_file/{request.id}_{request.name}_info.txt", "a+") as file_object:
            # Move read cursor to the start of file.
            file_object.seek(0)
            # If file is not empty then append '\n'
            data = file_object.read(100)
            if len(data) > 0 :
                file_object.write("\n")
            # Append text at the end of file
            file_object.write(f"{request.location}  {request.check_in_time} ")
        
        reply_message = 'Check In ' + request.location + ' successful' 
            
        return SafeEntry_pb2.CheckInReply(res=reply_message)
    
    # individual check out function 
    def checkOut(self, request, context):
        # print out the request message
        print("Check out request received: ")
        print(request)
        # add the check out details in client_info.txt
        with open(f"server_file/{request.id}_{request.name}_info.txt", "a+") as file_object:
            lines = file_object.readlines()
            file_object.seek(0)
            file_object.write("\n")
            file_object.write(f"{request.location}  {request.check_out_time}  Check Out")
                    
        reply_message = 'Check out ' + request.location + ' successful'  
           
        return SafeEntry_pb2.CheckOutReply(res=reply_message)
            
    
    # group check in function 
    def groupCheckIn(self, request, context):
        if request.name not in client_info:
            client_info.append([request.name, request.id, request.location])
            
        return SafeEntry_pb2.Reply(res='Group Check In ' + request.location + ' successful')
    
    # group check out function 
    def groupCheckOut(self, request, context):
        if request.name not in client_info:
            client_info.append([request.name, request.id, request.location])
            
        return SafeEntry_pb2.Reply(res='Group Check Out ' + request.location + ' successful')
    
    # MOH update location 
    def updateLocation(self, request, context):
        
        return SafeEntry_pb2.MOHReply(res='Updates have been received.')
    
    # send sms notification to the clients who has visited covid places
    def getNotification(self, request, context):
        pass
    
    # get all the location that visited by the client
    def getLocation(self, request, context):
        # print out the get location request message
        print("Get location request received: ")
        print(request)
    
    # get current time function
    def getCurrentTime(self):
        now = datetime.now()
            # get current time  
        current_time = now.strftime("%H:%M:%S")
        return current_time

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5), maximum_concurrent_rpcs=10)
    #add SafeEntry Servicier to the server
    SafeEntry_pb2_grpc.add_SafeEntryServicer_to_server(SafeEntry(), server)            
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
