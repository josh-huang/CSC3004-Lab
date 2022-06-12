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
        self.Add = channel.unary_unary(
                '/SafeEntry.SafeEntry/Add',
                request_serializer=SafeEntry__pb2.Request.SerializeToString,
                response_deserializer=SafeEntry__pb2.Reply.FromString,
                )
        self.Sub = channel.unary_unary(
                '/SafeEntry.SafeEntry/Sub',
                request_serializer=SafeEntry__pb2.Request.SerializeToString,
                response_deserializer=SafeEntry__pb2.Reply.FromString,
                )
        self.Multiply = channel.unary_unary(
                '/SafeEntry.SafeEntry/Multiply',
                request_serializer=SafeEntry__pb2.Request.SerializeToString,
                response_deserializer=SafeEntry__pb2.Reply.FromString,
                )
        self.Divide = channel.unary_unary(
                '/SafeEntry.SafeEntry/Divide',
                request_serializer=SafeEntry__pb2.Request.SerializeToString,
                response_deserializer=SafeEntry__pb2.Reply.FromString,
                )


class SafeEntryServicer(object):
    """The greeting service definition.
    """

    def Add(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Sub(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Multiply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Divide(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SafeEntryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Add': grpc.unary_unary_rpc_method_handler(
                    servicer.Add,
                    request_deserializer=SafeEntry__pb2.Request.FromString,
                    response_serializer=SafeEntry__pb2.Reply.SerializeToString,
            ),
            'Sub': grpc.unary_unary_rpc_method_handler(
                    servicer.Sub,
                    request_deserializer=SafeEntry__pb2.Request.FromString,
                    response_serializer=SafeEntry__pb2.Reply.SerializeToString,
            ),
            'Multiply': grpc.unary_unary_rpc_method_handler(
                    servicer.Multiply,
                    request_deserializer=SafeEntry__pb2.Request.FromString,
                    response_serializer=SafeEntry__pb2.Reply.SerializeToString,
            ),
            'Divide': grpc.unary_unary_rpc_method_handler(
                    servicer.Divide,
                    request_deserializer=SafeEntry__pb2.Request.FromString,
                    response_serializer=SafeEntry__pb2.Reply.SerializeToString,
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
    def Add(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry.SafeEntry/Add',
            SafeEntry__pb2.Request.SerializeToString,
            SafeEntry__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Sub(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry.SafeEntry/Sub',
            SafeEntry__pb2.Request.SerializeToString,
            SafeEntry__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Multiply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry.SafeEntry/Multiply',
            SafeEntry__pb2.Request.SerializeToString,
            SafeEntry__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Divide(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry.SafeEntry/Divide',
            SafeEntry__pb2.Request.SerializeToString,
            SafeEntry__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
