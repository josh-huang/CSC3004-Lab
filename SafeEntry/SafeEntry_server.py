from concurrent import futures

import logging

import grpc

import SafeEntry_pb2

import SafeEntry_pb2_grpc

# client_info dictionary: key: client id value : array[name, location, checkin time]
client_info = {}

# location_info dictionary: key: Location name value: array[id]
location_info={}

class SafeEntry(SafeEntry_pb2_grpc.SafeEntryServicer):
    
    #To be deleted 
    def Sub(self, request, context):
        return SafeEntry_pb2.Reply(res=request.x - request.y)
    
    # individual check in function 
    def checkIn(self, request, context):
        if request.name not in client_info:
            client_info[request.name]=[request.id, request.location, request.check_in_time]
            
        return SafeEntry_pb2.CheckInReply(res='Check In ' + request.location + ' successful')
    
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
    
    # for MOH use 
    def updateLocation(self, request, context):
        #TO-DO Implement update location 
        pass
        # receive location name and iterate through location info and send notification to all the names in the array 



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
