# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: p_greet.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rp_greet.proto\x12\x07p_greet\".\n\x0cGreetRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08greeting\x18\x02 \x01(\t\" \n\rGreetResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2C\n\tP_GREETER\x12\x36\n\x05Greet\x12\x15.p_greet.GreetRequest\x1a\x16.p_greet.GreetResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'p_greet_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_GREETREQUEST']._serialized_start=26
  _globals['_GREETREQUEST']._serialized_end=72
  _globals['_GREETRESPONSE']._serialized_start=74
  _globals['_GREETRESPONSE']._serialized_end=106
  _globals['_P_GREETER']._serialized_start=108
  _globals['_P_GREETER']._serialized_end=175
# @@protoc_insertion_point(module_scope)
