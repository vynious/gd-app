# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: booking/booking_message.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x62ooking/booking_message.proto\x12\x07\x62ooking\x1a\x1fgoogle/protobuf/timestamp.proto\"h\n\x07\x42ooking\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x10\n\x08\x63lass_id\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"9\n\x14\x43reateBookingRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x10\n\x08\x63lass_id\x18\x02 \x01(\t\":\n\x15\x43reateBookingResponse\x12!\n\x07\x62ooking\x18\x01 \x01(\x0b\x32\x10.booking.Booking\"\"\n\x14\x43\x61ncelBookingRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x17\n\x15\x43\x61ncelBookingResponse\"&\n\x13ListBookingsRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\":\n\x14ListBookingsResponse\x12\"\n\x08\x62ookings\x18\x01 \x03(\x0b\x32\x10.booking.Booking\"\x1f\n\x11GetBookingRequest\x12\n\n\x02id\x18\x01 \x01(\t\"7\n\x12GetBookingResponse\x12!\n\x07\x62ooking\x18\x01 \x01(\x0b\x32\x10.booking.Booking\"*\n\x17GetBookingByUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\">\n\x18GetBookingByUserResponse\x12\"\n\x08\x62ookings\x18\x01 \x03(\x0b\x32\x10.booking.Booking\"E\n\x14UpdateBookingRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x63lass_id\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\":\n\x15UpdateBookingResponse\x12!\n\x07\x62ooking\x18\x01 \x01(\x0b\x32\x10.booking.Bookingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'booking.booking_message_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_BOOKING']._serialized_start=75
  _globals['_BOOKING']._serialized_end=179
  _globals['_CREATEBOOKINGREQUEST']._serialized_start=181
  _globals['_CREATEBOOKINGREQUEST']._serialized_end=238
  _globals['_CREATEBOOKINGRESPONSE']._serialized_start=240
  _globals['_CREATEBOOKINGRESPONSE']._serialized_end=298
  _globals['_CANCELBOOKINGREQUEST']._serialized_start=300
  _globals['_CANCELBOOKINGREQUEST']._serialized_end=334
  _globals['_CANCELBOOKINGRESPONSE']._serialized_start=336
  _globals['_CANCELBOOKINGRESPONSE']._serialized_end=359
  _globals['_LISTBOOKINGSREQUEST']._serialized_start=361
  _globals['_LISTBOOKINGSREQUEST']._serialized_end=399
  _globals['_LISTBOOKINGSRESPONSE']._serialized_start=401
  _globals['_LISTBOOKINGSRESPONSE']._serialized_end=459
  _globals['_GETBOOKINGREQUEST']._serialized_start=461
  _globals['_GETBOOKINGREQUEST']._serialized_end=492
  _globals['_GETBOOKINGRESPONSE']._serialized_start=494
  _globals['_GETBOOKINGRESPONSE']._serialized_end=549
  _globals['_GETBOOKINGBYUSERREQUEST']._serialized_start=551
  _globals['_GETBOOKINGBYUSERREQUEST']._serialized_end=593
  _globals['_GETBOOKINGBYUSERRESPONSE']._serialized_start=595
  _globals['_GETBOOKINGBYUSERRESPONSE']._serialized_end=657
  _globals['_UPDATEBOOKINGREQUEST']._serialized_start=659
  _globals['_UPDATEBOOKINGREQUEST']._serialized_end=728
  _globals['_UPDATEBOOKINGRESPONSE']._serialized_start=730
  _globals['_UPDATEBOOKINGRESPONSE']._serialized_end=788
# @@protoc_insertion_point(module_scope)
