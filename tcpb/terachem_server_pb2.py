# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: terachem_server.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='terachem_server.proto',
  package='terachem_server',
  syntax='proto3',
  serialized_pb=_b('\n\x15terachem_server.proto\x12\x0fterachem_server\"\x9d\x01\n\x06Status\x12\x0c\n\x04\x62usy\x18\x01 \x01(\x08\x12\x12\n\x08\x61\x63\x63\x65pted\x18\x02 \x01(\x08H\x00\x12\x11\n\x07working\x18\x03 \x01(\x08H\x00\x12\x13\n\tcompleted\x18\x04 \x01(\x08H\x00\x12\x0f\n\x07job_dir\x18\x05 \x01(\t\x12\x13\n\x0bjob_scr_dir\x18\x06 \x01(\t\x12\x15\n\rserver_job_id\x18\x07 \x01(\x05\x42\x0c\n\njob_status\"\xbd\x01\n\x03Mol\x12\r\n\x05\x61toms\x18\x01 \x03(\t\x12\x0b\n\x03xyz\x18\x02 \x03(\x01\x12,\n\x05units\x18\x03 \x01(\x0e\x32\x1d.terachem_server.Mol.UnitType\x12\x0e\n\x06\x63harge\x18\x04 \x01(\x05\x12\x14\n\x0cmultiplicity\x18\x05 \x01(\x05\x12\x0e\n\x06\x63losed\x18\x06 \x01(\x08\x12\x12\n\nrestricted\x18\x07 \x01(\x08\"\"\n\x08UnitType\x12\x0c\n\x08\x41NGSTROM\x10\x00\x12\x08\n\x04\x42OHR\x10\x01\"\xe7\x04\n\x08JobInput\x12!\n\x03mol\x18\x01 \x01(\x0b\x32\x14.terachem_server.Mol\x12.\n\x03run\x18\x02 \x01(\x0e\x32!.terachem_server.JobInput.RunType\x12\x34\n\x06method\x18\x03 \x01(\x0e\x32$.terachem_server.JobInput.MethodType\x12\r\n\x05\x62\x61sis\x18\x04 \x01(\t\x12\x11\n\torb1afile\x18\x08 \x01(\t\x12\x11\n\torb1bfile\x18\t \x01(\t\x12\x14\n\x0cuser_options\x18\x07 \x03(\t\x12\x0c\n\x04xyz2\x18\x11 \x03(\x01\x12\x19\n\x11return_bond_order\x18\x10 \x01(\x08\"E\n\x07RunType\x12\n\n\x06\x45NERGY\x10\x00\x12\x0c\n\x08GRADIENT\x10\x01\x12\x0c\n\x08\x43OUPLING\x10\x0e\x12\x12\n\x0e\x43I_VEC_OVERLAP\x10\x13\"\x96\x02\n\nMethodType\x12\x06\n\x02HF\x10\x00\x12\x08\n\x04\x43\x41SE\x10\x02\x12\t\n\x05SVWN1\x10\x03\x12\t\n\x05SVWN3\x10\x04\x12\t\n\x05SVWN5\x10\x05\x12\x08\n\x04SVWN\x10\x05\x12\n\n\x06\x42\x33LYP1\x10\x06\x12\t\n\x05\x42\x33LYP\x10\x06\x12\n\n\x06\x42\x33LYP3\x10\x07\x12\n\n\x06\x42\x33LYP5\x10\x08\x12\x08\n\x04\x42LYP\x10\t\x12\r\n\tBHANDHLYP\x10\n\x12\x07\n\x03PBE\x10\x0b\x12\n\n\x06REVPBE\x10\x0c\x12\x08\n\x04PBE0\x10\r\x12\x0b\n\x07REVPBE0\x10\x0e\x12\x08\n\x04WPBE\x10\x0f\x12\t\n\x05WPBEH\x10\x10\x12\x07\n\x03\x42OP\x10\x11\x12\t\n\x05MUBOP\x10\x12\x12\x0c\n\x08\x43\x41MB3LYP\x10\x13\x12\x07\n\x03\x42\x39\x37\x10\x14\x12\x08\n\x04WB97\x10\x15\x12\t\n\x05WB97X\x10\x16\x1a\x02\x10\x01\"\xed\x04\n\tJobOutput\x12!\n\x03mol\x18\x01 \x01(\x0b\x32\x14.terachem_server.Mol\x12\x0e\n\x06\x65nergy\x18\x02 \x03(\x01\x12\x10\n\x08gradient\x18\x03 \x03(\x01\x12\x0f\n\x07\x63harges\x18\x04 \x03(\x01\x12\r\n\x05spins\x18\x05 \x03(\x01\x12\x0f\n\x07\x64ipoles\x18\x06 \x03(\x01\x12\x11\n\torb1afile\x18\x0c \x01(\t\x12\x11\n\torb1bfile\x18\r \x01(\t\x12\x10\n\x08orb_size\x18\x0e \x01(\x05\x12\x15\n\rorba_energies\x18\x19 \x03(\x01\x12\x15\n\rorbb_energies\x18\x1a \x03(\x01\x12\x18\n\x10orba_occupations\x18\x1b \x03(\x01\x12\x18\n\x10orbb_occupations\x18\x1c \x03(\x01\x12\x0f\n\x07job_dir\x18\t \x01(\t\x12\x13\n\x0bjob_scr_dir\x18\n \x01(\t\x12\x15\n\rserver_job_id\x18\x0b \x01(\x05\x12\r\n\x05nacme\x18\x15 \x03(\x01\x12\x13\n\x0b\x63i_overlaps\x18\x11 \x03(\x01\x12\x17\n\x0f\x63i_overlap_size\x18\x12 \x01(\x05\x12\x19\n\x11\x63\x61s_energy_states\x18\x13 \x03(\x05\x12\x18\n\x10\x63\x61s_energy_mults\x18\x14 \x03(\x05\x12\x1d\n\x15\x63\x61s_transition_dipole\x18\x16 \x03(\x01\x12\x12\n\ncis_states\x18\x1d \x01(\x05\x12\x1d\n\x15\x63is_unrelaxed_dipoles\x18\x1e \x03(\x01\x12\x1b\n\x13\x63is_relaxed_dipoles\x18\x1f \x03(\x01\x12\x1e\n\x16\x63is_transition_dipoles\x18  \x03(\x01\x12\x12\n\nbond_order\x18\x10 \x03(\x01*?\n\x0bMessageType\x12\n\n\x06STATUS\x10\x00\x12\x07\n\x03MOL\x10\x01\x12\x0c\n\x08JOBINPUT\x10\x02\x12\r\n\tJOBOUTPUT\x10\x03\x42\x1b\xaa\x02\x18Google.Protobuf.TeraChemb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_MESSAGETYPE = _descriptor.EnumDescriptor(
  name='MessageType',
  full_name='terachem_server.MessageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOBINPUT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOBOUTPUT', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1636,
  serialized_end=1699,
)
_sym_db.RegisterEnumDescriptor(_MESSAGETYPE)

MessageType = enum_type_wrapper.EnumTypeWrapper(_MESSAGETYPE)
STATUS = 0
MOL = 1
JOBINPUT = 2
JOBOUTPUT = 3


_MOL_UNITTYPE = _descriptor.EnumDescriptor(
  name='UnitType',
  full_name='terachem_server.Mol.UnitType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ANGSTROM', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOHR', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=358,
  serialized_end=392,
)
_sym_db.RegisterEnumDescriptor(_MOL_UNITTYPE)

_JOBINPUT_RUNTYPE = _descriptor.EnumDescriptor(
  name='RunType',
  full_name='terachem_server.JobInput.RunType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENERGY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRADIENT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COUPLING', index=2, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CI_VEC_OVERLAP', index=3, number=19,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=660,
  serialized_end=729,
)
_sym_db.RegisterEnumDescriptor(_JOBINPUT_RUNTYPE)

_JOBINPUT_METHODTYPE = _descriptor.EnumDescriptor(
  name='MethodType',
  full_name='terachem_server.JobInput.MethodType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HF', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CASE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SVWN1', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SVWN3', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SVWN5', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SVWN', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='B3LYP1', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='B3LYP', index=7, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='B3LYP3', index=8, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='B3LYP5', index=9, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLYP', index=10, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BHANDHLYP', index=11, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PBE', index=12, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REVPBE', index=13, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PBE0', index=14, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REVPBE0', index=15, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WPBE', index=16, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WPBEH', index=17, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOP', index=18, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MUBOP', index=19, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMB3LYP', index=20, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='B97', index=21, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WB97', index=22, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WB97X', index=23, number=22,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=_descriptor._ParseOptions(descriptor_pb2.EnumOptions(), _b('\020\001')),
  serialized_start=732,
  serialized_end=1010,
)
_sym_db.RegisterEnumDescriptor(_JOBINPUT_METHODTYPE)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='terachem_server.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='busy', full_name='terachem_server.Status.busy', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accepted', full_name='terachem_server.Status.accepted', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='working', full_name='terachem_server.Status.working', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='completed', full_name='terachem_server.Status.completed', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='job_dir', full_name='terachem_server.Status.job_dir', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='job_scr_dir', full_name='terachem_server.Status.job_scr_dir', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_job_id', full_name='terachem_server.Status.server_job_id', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
    _descriptor.OneofDescriptor(
      name='job_status', full_name='terachem_server.Status.job_status',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=43,
  serialized_end=200,
)


_MOL = _descriptor.Descriptor(
  name='Mol',
  full_name='terachem_server.Mol',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='atoms', full_name='terachem_server.Mol.atoms', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='xyz', full_name='terachem_server.Mol.xyz', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='units', full_name='terachem_server.Mol.units', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='charge', full_name='terachem_server.Mol.charge', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='multiplicity', full_name='terachem_server.Mol.multiplicity', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='closed', full_name='terachem_server.Mol.closed', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='restricted', full_name='terachem_server.Mol.restricted', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MOL_UNITTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=203,
  serialized_end=392,
)


_JOBINPUT = _descriptor.Descriptor(
  name='JobInput',
  full_name='terachem_server.JobInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mol', full_name='terachem_server.JobInput.mol', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='run', full_name='terachem_server.JobInput.run', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='method', full_name='terachem_server.JobInput.method', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='basis', full_name='terachem_server.JobInput.basis', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orb1afile', full_name='terachem_server.JobInput.orb1afile', index=4,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orb1bfile', full_name='terachem_server.JobInput.orb1bfile', index=5,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_options', full_name='terachem_server.JobInput.user_options', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='xyz2', full_name='terachem_server.JobInput.xyz2', index=7,
      number=17, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='return_bond_order', full_name='terachem_server.JobInput.return_bond_order', index=8,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _JOBINPUT_RUNTYPE,
    _JOBINPUT_METHODTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=395,
  serialized_end=1010,
)


_JOBOUTPUT = _descriptor.Descriptor(
  name='JobOutput',
  full_name='terachem_server.JobOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mol', full_name='terachem_server.JobOutput.mol', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='energy', full_name='terachem_server.JobOutput.energy', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gradient', full_name='terachem_server.JobOutput.gradient', index=2,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='charges', full_name='terachem_server.JobOutput.charges', index=3,
      number=4, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spins', full_name='terachem_server.JobOutput.spins', index=4,
      number=5, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dipoles', full_name='terachem_server.JobOutput.dipoles', index=5,
      number=6, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orb1afile', full_name='terachem_server.JobOutput.orb1afile', index=6,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orb1bfile', full_name='terachem_server.JobOutput.orb1bfile', index=7,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orb_size', full_name='terachem_server.JobOutput.orb_size', index=8,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orba_energies', full_name='terachem_server.JobOutput.orba_energies', index=9,
      number=25, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orbb_energies', full_name='terachem_server.JobOutput.orbb_energies', index=10,
      number=26, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orba_occupations', full_name='terachem_server.JobOutput.orba_occupations', index=11,
      number=27, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orbb_occupations', full_name='terachem_server.JobOutput.orbb_occupations', index=12,
      number=28, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='job_dir', full_name='terachem_server.JobOutput.job_dir', index=13,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='job_scr_dir', full_name='terachem_server.JobOutput.job_scr_dir', index=14,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_job_id', full_name='terachem_server.JobOutput.server_job_id', index=15,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nacme', full_name='terachem_server.JobOutput.nacme', index=16,
      number=21, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ci_overlaps', full_name='terachem_server.JobOutput.ci_overlaps', index=17,
      number=17, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ci_overlap_size', full_name='terachem_server.JobOutput.ci_overlap_size', index=18,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cas_energy_states', full_name='terachem_server.JobOutput.cas_energy_states', index=19,
      number=19, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cas_energy_mults', full_name='terachem_server.JobOutput.cas_energy_mults', index=20,
      number=20, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cas_transition_dipole', full_name='terachem_server.JobOutput.cas_transition_dipole', index=21,
      number=22, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cis_states', full_name='terachem_server.JobOutput.cis_states', index=22,
      number=29, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cis_unrelaxed_dipoles', full_name='terachem_server.JobOutput.cis_unrelaxed_dipoles', index=23,
      number=30, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cis_relaxed_dipoles', full_name='terachem_server.JobOutput.cis_relaxed_dipoles', index=24,
      number=31, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cis_transition_dipoles', full_name='terachem_server.JobOutput.cis_transition_dipoles', index=25,
      number=32, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bond_order', full_name='terachem_server.JobOutput.bond_order', index=26,
      number=16, type=1, cpp_type=5, label=3,
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
  serialized_start=1013,
  serialized_end=1634,
)

_STATUS.oneofs_by_name['job_status'].fields.append(
  _STATUS.fields_by_name['accepted'])
_STATUS.fields_by_name['accepted'].containing_oneof = _STATUS.oneofs_by_name['job_status']
_STATUS.oneofs_by_name['job_status'].fields.append(
  _STATUS.fields_by_name['working'])
_STATUS.fields_by_name['working'].containing_oneof = _STATUS.oneofs_by_name['job_status']
_STATUS.oneofs_by_name['job_status'].fields.append(
  _STATUS.fields_by_name['completed'])
_STATUS.fields_by_name['completed'].containing_oneof = _STATUS.oneofs_by_name['job_status']
_MOL.fields_by_name['units'].enum_type = _MOL_UNITTYPE
_MOL_UNITTYPE.containing_type = _MOL
_JOBINPUT.fields_by_name['mol'].message_type = _MOL
_JOBINPUT.fields_by_name['run'].enum_type = _JOBINPUT_RUNTYPE
_JOBINPUT.fields_by_name['method'].enum_type = _JOBINPUT_METHODTYPE
_JOBINPUT_RUNTYPE.containing_type = _JOBINPUT
_JOBINPUT_METHODTYPE.containing_type = _JOBINPUT
_JOBOUTPUT.fields_by_name['mol'].message_type = _MOL
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['Mol'] = _MOL
DESCRIPTOR.message_types_by_name['JobInput'] = _JOBINPUT
DESCRIPTOR.message_types_by_name['JobOutput'] = _JOBOUTPUT
DESCRIPTOR.enum_types_by_name['MessageType'] = _MESSAGETYPE

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), dict(
  DESCRIPTOR = _STATUS,
  __module__ = 'terachem_server_pb2'
  # @@protoc_insertion_point(class_scope:terachem_server.Status)
  ))
_sym_db.RegisterMessage(Status)

Mol = _reflection.GeneratedProtocolMessageType('Mol', (_message.Message,), dict(
  DESCRIPTOR = _MOL,
  __module__ = 'terachem_server_pb2'
  # @@protoc_insertion_point(class_scope:terachem_server.Mol)
  ))
_sym_db.RegisterMessage(Mol)

JobInput = _reflection.GeneratedProtocolMessageType('JobInput', (_message.Message,), dict(
  DESCRIPTOR = _JOBINPUT,
  __module__ = 'terachem_server_pb2'
  # @@protoc_insertion_point(class_scope:terachem_server.JobInput)
  ))
_sym_db.RegisterMessage(JobInput)

JobOutput = _reflection.GeneratedProtocolMessageType('JobOutput', (_message.Message,), dict(
  DESCRIPTOR = _JOBOUTPUT,
  __module__ = 'terachem_server_pb2'
  # @@protoc_insertion_point(class_scope:terachem_server.JobOutput)
  ))
_sym_db.RegisterMessage(JobOutput)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\252\002\030Google.Protobuf.TeraChem'))
_JOBINPUT_METHODTYPE.has_options = True
_JOBINPUT_METHODTYPE._options = _descriptor._ParseOptions(descriptor_pb2.EnumOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
