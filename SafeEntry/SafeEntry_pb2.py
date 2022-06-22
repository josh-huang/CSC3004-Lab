# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SafeEntry.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fSafeEntry.proto\x12\tSafeEntry\"i\n\x0e\x43heckInRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x15\n\rcheck_in_time\x18\x04 \x01(\t\x12\x14\n\x0cphone_number\x18\x05 \x01(\t\"\x1b\n\x0c\x43heckInReply\x12\x0b\n\x03res\x18\x01 \x01(\t\"U\n\x0f\x43heckOutRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x16\n\x0e\x63heck_out_time\x18\x04 \x01(\t\"\x1c\n\rCheckOutReply\x12\x0b\n\x03res\x18\x01 \x01(\t\"n\n\x13GroupCheckInRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x15\n\rcheck_in_time\x18\x04 \x01(\t\x12\x14\n\x0cphone_number\x18\x05 \x01(\t\"Q\n\x11GroupCheckInReply\x12\x0b\n\x03res\x18\x01 \x01(\t\x12/\n\x07request\x18\x02 \x03(\x0b\x32\x1e.SafeEntry.GroupCheckInRequest\"Z\n\x14GroupCheckOutRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x16\n\x0e\x63heck_out_time\x18\x04 \x01(\t\"S\n\x12GroupCheckOutReply\x12\x0b\n\x03res\x18\x01 \x01(\t\x12\x30\n\x07request\x18\x02 \x03(\x0b\x32\x1f.SafeEntry.GroupCheckOutRequest\"N\n\nMOHRequest\x12\x15\n\rlocation_name\x18\x01 \x01(\t\x12\x12\n\nvisit_date\x18\x02 \x01(\t\x12\x15\n\rcheckOut_date\x18\x03 \x01(\t\"\x17\n\x08MOHReply\x12\x0b\n\x03res\x18\x01 \x01(\t\"5\n\x0fLocationRequest\x12\x11\n\tuser_name\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\" \n\rLocationReply\x12\x0f\n\x07res_msg\x18\x01 \x01(\t2\xc0\x03\n\tSafeEntry\x12?\n\x07\x63heckIn\x12\x19.SafeEntry.CheckInRequest\x1a\x17.SafeEntry.CheckInReply\"\x00\x12\x42\n\x08\x63heckOut\x12\x1a.SafeEntry.CheckOutRequest\x1a\x18.SafeEntry.CheckOutReply\"\x00\x12P\n\x0cgroupCheckIn\x12\x1e.SafeEntry.GroupCheckInRequest\x1a\x1c.SafeEntry.GroupCheckInReply\"\x00(\x01\x12S\n\rgroupCheckOut\x12\x1f.SafeEntry.GroupCheckOutRequest\x1a\x1d.SafeEntry.GroupCheckOutReply\"\x00(\x01\x12G\n\x0bgetLocation\x12\x1a.SafeEntry.LocationRequest\x1a\x18.SafeEntry.LocationReply\"\x00\x30\x01\x12>\n\x0eupdateLocation\x12\x15.SafeEntry.MOHRequest\x1a\x13.SafeEntry.MOHReply\"\x00\x62\x06proto3')



_CHECKINREQUEST = DESCRIPTOR.message_types_by_name['CheckInRequest']
_CHECKINREPLY = DESCRIPTOR.message_types_by_name['CheckInReply']
_CHECKOUTREQUEST = DESCRIPTOR.message_types_by_name['CheckOutRequest']
_CHECKOUTREPLY = DESCRIPTOR.message_types_by_name['CheckOutReply']
_GROUPCHECKINREQUEST = DESCRIPTOR.message_types_by_name['GroupCheckInRequest']
_GROUPCHECKINREPLY = DESCRIPTOR.message_types_by_name['GroupCheckInReply']
_GROUPCHECKOUTREQUEST = DESCRIPTOR.message_types_by_name['GroupCheckOutRequest']
_GROUPCHECKOUTREPLY = DESCRIPTOR.message_types_by_name['GroupCheckOutReply']
_MOHREQUEST = DESCRIPTOR.message_types_by_name['MOHRequest']
_MOHREPLY = DESCRIPTOR.message_types_by_name['MOHReply']
_LOCATIONREQUEST = DESCRIPTOR.message_types_by_name['LocationRequest']
_LOCATIONREPLY = DESCRIPTOR.message_types_by_name['LocationReply']
CheckInRequest = _reflection.GeneratedProtocolMessageType('CheckInRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHECKINREQUEST,
  '__module__' : 'SafeEntry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.CheckInRequest)
  })
_sym_db.RegisterMessage(CheckInRequest)

CheckInReply = _reflection.GeneratedProtocolMessageType('CheckInReply', (_message.Message,), {
  'DESCRIPTOR' : _CHECKINREPLY,
  '__module__' : 'SafeEntry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.CheckInReply)
  })
_sym_db.RegisterMessage(CheckInReply)

CheckOutRequest = _reflection.GeneratedProtocolMessageType('CheckOutRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHECKOUTREQUEST,
  '__module__' : 'SafeEntry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.CheckOutRequest)
  })
_sym_db.RegisterMessage(CheckOutRequest)

CheckOutReply = _reflection.GeneratedProtocolMessageType('CheckOutReply', (_message.Message,), {
  'DESCRIPTOR' : _CHECKOUTREPLY,
  '__module__' : 'SafeEntry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.CheckOutReply)
  })
_sym_db.RegisterMessage(CheckOutReply)

GroupCheckInRequest = _reflection.GeneratedProtocolMessageType('GroupCheckInRequest', (_message.Message,), {
  'DESCRIPTOR' : _GROUPCHECKINREQUEST,
  '__module__' : 'SafeEntry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.GroupCheckInRequest)
  })
_sym_db.RegisterMessage(GroupCheckInRequest)

GroupCheckInReply = _reflection.GeneratedProtocolMessageType('GroupCheckInReply', (_message.Message,), {
  'DESCRIPTOR' : _GROUPCHECKINREPLY,
  '__module__' : 'SafeEntry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.GroupCheckInReply)
  })
_sym_db.RegisterMessage(GroupCheckInReply)

GroupCheckOutRequest = _reflection.GeneratedProtocolMessageType('GroupCheckOutRequest', (_message.Message,), {
  'DESCRIPTOR' : _GROUPCHECKOUTREQUEST,
  '__module__' : 'SafeEntry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.GroupCheckOutRequest)
  })
_sym_db.RegisterMessage(GroupCheckOutRequest)

GroupCheckOutReply = _reflection.GeneratedProtocolMessageType('GroupCheckOutReply', (_message.Message,), {
  'DESCRIPTOR' : _GROUPCHECKOUTREPLY,
  '__module__' : 'SafeEntry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.GroupCheckOutReply)
  })
_sym_db.RegisterMessage(GroupCheckOutReply)

MOHRequest = _reflection.GeneratedProtocolMessageType('MOHRequest', (_message.Message,), {
  'DESCRIPTOR' : _MOHREQUEST,
  '__module__' : 'SafeEntry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.MOHRequest)
  })
_sym_db.RegisterMessage(MOHRequest)

MOHReply = _reflection.GeneratedProtocolMessageType('MOHReply', (_message.Message,), {
  'DESCRIPTOR' : _MOHREPLY,
  '__module__' : 'SafeEntry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.MOHReply)
  })
_sym_db.RegisterMessage(MOHReply)

LocationRequest = _reflection.GeneratedProtocolMessageType('LocationRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOCATIONREQUEST,
  '__module__' : 'SafeEntry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.LocationRequest)
  })
_sym_db.RegisterMessage(LocationRequest)

LocationReply = _reflection.GeneratedProtocolMessageType('LocationReply', (_message.Message,), {
  'DESCRIPTOR' : _LOCATIONREPLY,
  '__module__' : 'SafeEntry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.LocationReply)
  })
_sym_db.RegisterMessage(LocationReply)

_SAFEENTRY = DESCRIPTOR.services_by_name['SafeEntry']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CHECKINREQUEST._serialized_start=30
  _CHECKINREQUEST._serialized_end=135
  _CHECKINREPLY._serialized_start=137
  _CHECKINREPLY._serialized_end=164
  _CHECKOUTREQUEST._serialized_start=166
  _CHECKOUTREQUEST._serialized_end=251
  _CHECKOUTREPLY._serialized_start=253
  _CHECKOUTREPLY._serialized_end=281
  _GROUPCHECKINREQUEST._serialized_start=283
  _GROUPCHECKINREQUEST._serialized_end=393
  _GROUPCHECKINREPLY._serialized_start=395
  _GROUPCHECKINREPLY._serialized_end=476
  _GROUPCHECKOUTREQUEST._serialized_start=478
  _GROUPCHECKOUTREQUEST._serialized_end=568
  _GROUPCHECKOUTREPLY._serialized_start=570
  _GROUPCHECKOUTREPLY._serialized_end=653
  _MOHREQUEST._serialized_start=655
  _MOHREQUEST._serialized_end=733
  _MOHREPLY._serialized_start=735
  _MOHREPLY._serialized_end=758
  _LOCATIONREQUEST._serialized_start=760
  _LOCATIONREQUEST._serialized_end=813
  _LOCATIONREPLY._serialized_start=815
  _LOCATIONREPLY._serialized_end=847
  _SAFEENTRY._serialized_start=850
  _SAFEENTRY._serialized_end=1298
# @@protoc_insertion_point(module_scope)
