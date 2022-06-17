# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import SafeEntry_pb2 as SafeEntry__pb2


class SafeEntryStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.checkIn = channel.unary_unary(
                '/SafeEntry.SafeEntry/checkIn',
                request_serializer=SafeEntry__pb2.CheckInRequest.SerializeToString,
                response_deserializer=SafeEntry__pb2.CheckInReply.FromString,
                )
        self.checkOut = channel.unary_unary(
                '/SafeEntry.SafeEntry/checkOut',
                request_serializer=SafeEntry__pb2.CheckOutRequest.SerializeToString,
                response_deserializer=SafeEntry__pb2.CheckOutReply.FromString,
                )


class SafeEntryServicer(object):
    """The greeting service definition.
    """

    def checkIn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def checkOut(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SafeEntryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'checkIn': grpc.unary_unary_rpc_method_handler(
                    servicer.checkIn,
                    request_deserializer=SafeEntry__pb2.CheckInRequest.FromString,
                    response_serializer=SafeEntry__pb2.CheckInReply.SerializeToString,
            ),
            'checkOut': grpc.unary_unary_rpc_method_handler(
                    servicer.checkOut,
                    request_deserializer=SafeEntry__pb2.CheckOutRequest.FromString,
                    response_serializer=SafeEntry__pb2.CheckOutReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SafeEntry.SafeEntry', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SafeEntry(object):
    """The greeting service definition.
    """

    @staticmethod
    def checkIn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry.SafeEntry/checkIn',
            SafeEntry__pb2.CheckInRequest.SerializeToString,
            SafeEntry__pb2.CheckInReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def checkOut(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry.SafeEntry/checkOut',
            SafeEntry__pb2.CheckOutRequest.SerializeToString,
            SafeEntry__pb2.CheckOutReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
