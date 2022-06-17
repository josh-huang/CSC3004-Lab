from concurrent import futures

import logging

import grpc

import SafeEntry_pb2

import SafeEntry_pb2_grpc

from location_scrap import random_location

from datetime import datetime

# client_info dictionary: key: client id value : array[name, location, checkin time]
client_info = {}

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
        
        if (request.id, request.name) not in client_info:
            client_info[request.id, request.name]= [[request.location , request.check_in_time]]
        else:
            client_info[request.id, request.name].append([request.location, request.check_in_time])
        
        reply_message = 'Check In ' + request.location + ' successful' 
        
        print(client_info)
            
        return SafeEntry_pb2.CheckInReply(res=reply_message)
    
    # individual check out function 
    def checkOut(self, request, context):
        # print out the request message
        print("Check out request received: ")
        print(request)
        
        if request.name not in client_info:
            client_info.append([request.name, request.id, request.location])
            
        return SafeEntry_pb2.CheckOutReply(res='Check Out ' + request.location + ' successful')
    
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
        pass
    
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
