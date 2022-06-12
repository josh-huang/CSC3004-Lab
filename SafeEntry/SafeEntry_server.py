from concurrent import futures

import logging

import grpc

import SafeEntry_pb2

import SafeEntry_pb2_grpc


class SafeEntry(SafeEntry_pb2_grpc.SafeEntryServicer):
    def Add(self, request, context):
        return SafeEntry_pb2.Reply(res=request.x + request.y)

    def Sub(self, request, context):
        return SafeEntry_pb2.Reply(res=request.x - request.y)

    def Multiply(self, request, context):
        return SafeEntry_pb2.Reply(res=request.x * request.y)

    def Divide(self, request, context):
        return SafeEntry_pb2.Reply(res=request.x / request.y)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    #add Calculator Servicier to the server
    SafeEntry_pb2_grpc.add_SafeEntryServicer_to_server(SafeEntry(), server)            
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
