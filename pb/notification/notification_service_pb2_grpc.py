# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from notification import notification_service_pb2 as notification_dot_notification__service__pb2


class NotificationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateNotification = channel.unary_unary(
                '/notification.NotificationService/CreateNotification',
                request_serializer=notification_dot_notification__service__pb2.CreateNotificationRequest.SerializeToString,
                response_deserializer=notification_dot_notification__service__pb2.CreateNotificationResponse.FromString,
                )


class NotificationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateNotification(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NotificationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateNotification': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateNotification,
                    request_deserializer=notification_dot_notification__service__pb2.CreateNotificationRequest.FromString,
                    response_serializer=notification_dot_notification__service__pb2.CreateNotificationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'notification.NotificationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NotificationService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateNotification(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/notification.NotificationService/CreateNotification',
            notification_dot_notification__service__pb2.CreateNotificationRequest.SerializeToString,
            notification_dot_notification__service__pb2.CreateNotificationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
