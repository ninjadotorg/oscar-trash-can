# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow_serving/apis/regression.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apis import input_pb2 as tensorflow__serving_dot_apis_dot_input__pb2
from apis import model_pb2 as tensorflow__serving_dot_apis_dot_model__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow_serving/apis/regression.proto',
  package='tensorflow.serving',
  syntax='proto3',
  serialized_pb=_b('\n(tensorflow_serving/apis/regression.proto\x12\x12tensorflow.serving\x1a#tensorflow_serving/apis/input.proto\x1a#tensorflow_serving/apis/model.proto\"\x1b\n\nRegression\x12\r\n\x05value\x18\x01 \x01(\x02\"G\n\x10RegressionResult\x12\x33\n\x0bregressions\x18\x01 \x03(\x0b\x32\x1e.tensorflow.serving.Regression\"p\n\x11RegressionRequest\x12\x31\n\nmodel_spec\x18\x01 \x01(\x0b\x32\x1d.tensorflow.serving.ModelSpec\x12(\n\x05input\x18\x02 \x01(\x0b\x32\x19.tensorflow.serving.Input\"J\n\x12RegressionResponse\x12\x34\n\x06result\x18\x01 \x01(\x0b\x32$.tensorflow.serving.RegressionResultB\x03\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[tensorflow__serving_dot_apis_dot_input__pb2.DESCRIPTOR,tensorflow__serving_dot_apis_dot_model__pb2.DESCRIPTOR,])




_REGRESSION = _descriptor.Descriptor(
  name='Regression',
  full_name='tensorflow.serving.Regression',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.serving.Regression.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=165,
)


_REGRESSIONRESULT = _descriptor.Descriptor(
  name='RegressionResult',
  full_name='tensorflow.serving.RegressionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='regressions', full_name='tensorflow.serving.RegressionResult.regressions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=167,
  serialized_end=238,
)


_REGRESSIONREQUEST = _descriptor.Descriptor(
  name='RegressionRequest',
  full_name='tensorflow.serving.RegressionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='model_spec', full_name='tensorflow.serving.RegressionRequest.model_spec', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input', full_name='tensorflow.serving.RegressionRequest.input', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=240,
  serialized_end=352,
)


_REGRESSIONRESPONSE = _descriptor.Descriptor(
  name='RegressionResponse',
  full_name='tensorflow.serving.RegressionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='tensorflow.serving.RegressionResponse.result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=354,
  serialized_end=428,
)

_REGRESSIONRESULT.fields_by_name['regressions'].message_type = _REGRESSION
_REGRESSIONREQUEST.fields_by_name['model_spec'].message_type = tensorflow__serving_dot_apis_dot_model__pb2._MODELSPEC
_REGRESSIONREQUEST.fields_by_name['input'].message_type = tensorflow__serving_dot_apis_dot_input__pb2._INPUT
_REGRESSIONRESPONSE.fields_by_name['result'].message_type = _REGRESSIONRESULT
DESCRIPTOR.message_types_by_name['Regression'] = _REGRESSION
DESCRIPTOR.message_types_by_name['RegressionResult'] = _REGRESSIONRESULT
DESCRIPTOR.message_types_by_name['RegressionRequest'] = _REGRESSIONREQUEST
DESCRIPTOR.message_types_by_name['RegressionResponse'] = _REGRESSIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Regression = _reflection.GeneratedProtocolMessageType('Regression', (_message.Message,), dict(
  DESCRIPTOR = _REGRESSION,
  __module__ = 'tensorflow_serving.apis.regression_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.Regression)
  ))
_sym_db.RegisterMessage(Regression)

RegressionResult = _reflection.GeneratedProtocolMessageType('RegressionResult', (_message.Message,), dict(
  DESCRIPTOR = _REGRESSIONRESULT,
  __module__ = 'tensorflow_serving.apis.regression_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.RegressionResult)
  ))
_sym_db.RegisterMessage(RegressionResult)

RegressionRequest = _reflection.GeneratedProtocolMessageType('RegressionRequest', (_message.Message,), dict(
  DESCRIPTOR = _REGRESSIONREQUEST,
  __module__ = 'tensorflow_serving.apis.regression_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.RegressionRequest)
  ))
_sym_db.RegisterMessage(RegressionRequest)

RegressionResponse = _reflection.GeneratedProtocolMessageType('RegressionResponse', (_message.Message,), dict(
  DESCRIPTOR = _REGRESSIONRESPONSE,
  __module__ = 'tensorflow_serving.apis.regression_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.RegressionResponse)
  ))
_sym_db.RegisterMessage(RegressionResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\370\001\001'))
# @@protoc_insertion_point(module_scope)
