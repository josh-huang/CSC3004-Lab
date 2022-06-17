from concurrent import futures

import logging

import grpc

import SafeEntry_pb2

import SafeEntry_pb2_grpc

from location_scrap import random_location

# client_info dictionary: key: client id value : array[name, location, checkin time]
client_info = {}

# location_info dictionary: key: Location name value: array[id]
location_info={}

# covid location array to store covid locations
covid_location = []

class SafeEntry(SafeEntry_pb2_grpc.SafeEntryServicer):
    
    #To be deleted 
    def Sub(self, request, context):
        return SafeEntry_pb2.Reply(res=request.x - request.y)
    
    # individual check in function 
    def checkIn(self, request, context):
        if request.name not in client_info:
            client_info[request.name]=[request.id, request.location, request.check_in_time]
        
        reply_message = 'Check In ' + request.location + ' successful' +
            
        return SafeEntry_pb2.CheckInReply(res=reply_message)
    
    # individual check out function 
    def checkOut(self, request, context):
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

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    #add SafeEntry Servicier to the server
    SafeEntry_pb2_grpc.add_SafeEntryServicer_to_server(SafeEntry(), server)            
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
