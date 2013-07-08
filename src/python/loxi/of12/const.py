# Copyright (c) 2008 The Board of Trustees of The Leland Stanford Junior University
# Copyright (c) 2011, 2012 Open Networking Foundation
# Copyright (c) 2012, 2013 Big Switch Networks, Inc.
# See the file LICENSE.pyloxi which should have been included in the source distribution

# Automatically generated by LOXI from template const.py
# Do not modify

OFP_VERSION = 3

# Identifiers from group macro_definitions
OFP_MAX_TABLE_NAME_LEN = 32
OFP_MAX_PORT_NAME_LEN = 16
OFP_TCP_PORT = 6633
OFP_SSL_PORT = 6633
OFP_ETH_ALEN = 6
OFP_DEFAULT_MISS_SEND_LEN = 128
OFP_VLAN_NONE = 0
OFP_FLOW_PERMANENT = 0
OFP_DEFAULT_PRIORITY = 32768
OFP_NO_BUFFER = 4294967295
DESC_STR_LEN = 256
SERIAL_NUM_LEN = 32
OFPQ_ALL = 4294967295
OFPQ_MIN_RATE_UNCFG = 65535
OFPQ_MAX_RATE_UNCFG = 65535

# Identifiers from group ofp_action_type
OFPAT_OUTPUT = 0
OFPAT_COPY_TTL_OUT = 11
OFPAT_COPY_TTL_IN = 12
OFPAT_SET_MPLS_TTL = 15
OFPAT_DEC_MPLS_TTL = 16
OFPAT_PUSH_VLAN = 17
OFPAT_POP_VLAN = 18
OFPAT_PUSH_MPLS = 19
OFPAT_POP_MPLS = 20
OFPAT_SET_QUEUE = 21
OFPAT_GROUP = 22
OFPAT_SET_NW_TTL = 23
OFPAT_DEC_NW_TTL = 24
OFPAT_SET_FIELD = 25
OFPAT_EXPERIMENTER = 65535

ofp_action_type_map = {
    0: 'OFPAT_OUTPUT',
    11: 'OFPAT_COPY_TTL_OUT',
    12: 'OFPAT_COPY_TTL_IN',
    15: 'OFPAT_SET_MPLS_TTL',
    16: 'OFPAT_DEC_MPLS_TTL',
    17: 'OFPAT_PUSH_VLAN',
    18: 'OFPAT_POP_VLAN',
    19: 'OFPAT_PUSH_MPLS',
    20: 'OFPAT_POP_MPLS',
    21: 'OFPAT_SET_QUEUE',
    22: 'OFPAT_GROUP',
    23: 'OFPAT_SET_NW_TTL',
    24: 'OFPAT_DEC_NW_TTL',
    25: 'OFPAT_SET_FIELD',
    65535: 'OFPAT_EXPERIMENTER',
}

# Identifiers from group ofp_bad_action_code
OFPBAC_BAD_TYPE = 0
OFPBAC_BAD_LEN = 1
OFPBAC_BAD_EXPERIMENTER = 2
OFPBAC_BAD_EXP_TYPE = 3
OFPBAC_BAD_OUT_PORT = 4
OFPBAC_BAD_ARGUMENT = 5
OFPBAC_EPERM = 6
OFPBAC_TOO_MANY = 7
OFPBAC_BAD_QUEUE = 8
OFPBAC_BAD_OUT_GROUP = 9
OFPBAC_MATCH_INCONSISTENT = 10
OFPBAC_UNSUPPORTED_ORDER = 11
OFPBAC_BAD_TAG = 12
OFPBAC_BAD_SET_TYPE = 13
OFPBAC_BAD_SET_LEN = 14
OFPBAC_BAD_SET_ARGUMENT = 15

ofp_bad_action_code_map = {
    0: 'OFPBAC_BAD_TYPE',
    1: 'OFPBAC_BAD_LEN',
    2: 'OFPBAC_BAD_EXPERIMENTER',
    3: 'OFPBAC_BAD_EXP_TYPE',
    4: 'OFPBAC_BAD_OUT_PORT',
    5: 'OFPBAC_BAD_ARGUMENT',
    6: 'OFPBAC_EPERM',
    7: 'OFPBAC_TOO_MANY',
    8: 'OFPBAC_BAD_QUEUE',
    9: 'OFPBAC_BAD_OUT_GROUP',
    10: 'OFPBAC_MATCH_INCONSISTENT',
    11: 'OFPBAC_UNSUPPORTED_ORDER',
    12: 'OFPBAC_BAD_TAG',
    13: 'OFPBAC_BAD_SET_TYPE',
    14: 'OFPBAC_BAD_SET_LEN',
    15: 'OFPBAC_BAD_SET_ARGUMENT',
}

# Identifiers from group ofp_bad_instruction_code
OFPBIC_UNKNOWN_INST = 0
OFPBIC_UNSUP_INST = 1
OFPBIC_BAD_TABLE_ID = 2
OFPBIC_UNSUP_METADATA = 3
OFPBIC_UNSUP_METADATA_MASK = 4
OFPBIC_BAD_EXPERIMENTER = 5
OFPBIC_BAD_EXP_TYPE = 6
OFPBIC_BAD_LEN = 7
OFPBIC_EPERM = 8

ofp_bad_instruction_code_map = {
    0: 'OFPBIC_UNKNOWN_INST',
    1: 'OFPBIC_UNSUP_INST',
    2: 'OFPBIC_BAD_TABLE_ID',
    3: 'OFPBIC_UNSUP_METADATA',
    4: 'OFPBIC_UNSUP_METADATA_MASK',
    5: 'OFPBIC_BAD_EXPERIMENTER',
    6: 'OFPBIC_BAD_EXP_TYPE',
    7: 'OFPBIC_BAD_LEN',
    8: 'OFPBIC_EPERM',
}

# Identifiers from group ofp_bad_match_code
OFPBMC_BAD_TYPE = 0
OFPBMC_BAD_LEN = 1
OFPBMC_BAD_TAG = 2
OFPBMC_BAD_DL_ADDR_MASK = 3
OFPBMC_BAD_NW_ADDR_MASK = 4
OFPBMC_BAD_WILDCARDS = 5
OFPBMC_BAD_FIELD = 6
OFPBMC_BAD_VALUE = 7
OFPBMC_BAD_MASK = 8
OFPBMC_BAD_PREREQ = 9
OFPBMC_DUP_FIELD = 10
OFPBMC_EPERM = 11

ofp_bad_match_code_map = {
    0: 'OFPBMC_BAD_TYPE',
    1: 'OFPBMC_BAD_LEN',
    2: 'OFPBMC_BAD_TAG',
    3: 'OFPBMC_BAD_DL_ADDR_MASK',
    4: 'OFPBMC_BAD_NW_ADDR_MASK',
    5: 'OFPBMC_BAD_WILDCARDS',
    6: 'OFPBMC_BAD_FIELD',
    7: 'OFPBMC_BAD_VALUE',
    8: 'OFPBMC_BAD_MASK',
    9: 'OFPBMC_BAD_PREREQ',
    10: 'OFPBMC_DUP_FIELD',
    11: 'OFPBMC_EPERM',
}

# Identifiers from group ofp_bad_request_code
OFPBRC_BAD_VERSION = 0
OFPBRC_BAD_TYPE = 1
OFPBRC_BAD_STAT = 2
OFPBRC_BAD_EXPERIMENTER = 3
OFPBRC_BAD_EXP_TYPE = 4
OFPBRC_EPERM = 5
OFPBRC_BAD_LEN = 6
OFPBRC_BUFFER_EMPTY = 7
OFPBRC_BUFFER_UNKNOWN = 8
OFPBRC_BAD_TABLE_ID = 9
OFPBRC_IS_SLAVE = 10
OFPBRC_BAD_PORT = 11
OFPBRC_BAD_PACKET = 12

ofp_bad_request_code_map = {
    0: 'OFPBRC_BAD_VERSION',
    1: 'OFPBRC_BAD_TYPE',
    2: 'OFPBRC_BAD_STAT',
    3: 'OFPBRC_BAD_EXPERIMENTER',
    4: 'OFPBRC_BAD_EXP_TYPE',
    5: 'OFPBRC_EPERM',
    6: 'OFPBRC_BAD_LEN',
    7: 'OFPBRC_BUFFER_EMPTY',
    8: 'OFPBRC_BUFFER_UNKNOWN',
    9: 'OFPBRC_BAD_TABLE_ID',
    10: 'OFPBRC_IS_SLAVE',
    11: 'OFPBRC_BAD_PORT',
    12: 'OFPBRC_BAD_PACKET',
}

# Identifiers from group ofp_bsn_vport_q_in_q_untagged
OF_BSN_VPORT_Q_IN_Q_UNTAGGED = 65535

ofp_bsn_vport_q_in_q_untagged_map = {
    65535: 'OF_BSN_VPORT_Q_IN_Q_UNTAGGED',
}

# Identifiers from group ofp_capabilities
OFPC_FLOW_STATS = 1
OFPC_TABLE_STATS = 2
OFPC_PORT_STATS = 4
OFPC_GROUP_STATS = 8
OFPC_IP_REASM = 32
OFPC_QUEUE_STATS = 64
OFPC_PORT_BLOCKED = 256

ofp_capabilities_map = {
    1: 'OFPC_FLOW_STATS',
    2: 'OFPC_TABLE_STATS',
    4: 'OFPC_PORT_STATS',
    8: 'OFPC_GROUP_STATS',
    32: 'OFPC_IP_REASM',
    64: 'OFPC_QUEUE_STATS',
    256: 'OFPC_PORT_BLOCKED',
}

# Identifiers from group ofp_config_flags
OFPC_FRAG_NORMAL = 0
OFPC_FRAG_DROP = 1
OFPC_FRAG_REASM = 2
OFPC_FRAG_MASK = 3
OFPC_INVALID_TTL_TO_CONTROLLER = 4

ofp_config_flags_map = {
    0: 'OFPC_FRAG_NORMAL',
    1: 'OFPC_FRAG_DROP',
    2: 'OFPC_FRAG_REASM',
    3: 'OFPC_FRAG_MASK',
    4: 'OFPC_INVALID_TTL_TO_CONTROLLER',
}

# Identifiers from group ofp_controller_max_len
OFPCML_MAX = 65509
OFPCML_NO_BUFFER = 65535

ofp_controller_max_len_map = {
    65509: 'OFPCML_MAX',
    65535: 'OFPCML_NO_BUFFER',
}

# Identifiers from group ofp_controller_role
OFPCR_ROLE_NOCHANGE = 0
OFPCR_ROLE_EQUAL = 1
OFPCR_ROLE_MASTER = 2
OFPCR_ROLE_SLAVE = 3

ofp_controller_role_map = {
    0: 'OFPCR_ROLE_NOCHANGE',
    1: 'OFPCR_ROLE_EQUAL',
    2: 'OFPCR_ROLE_MASTER',
    3: 'OFPCR_ROLE_SLAVE',
}

# Identifiers from group ofp_error_type
OFPET_HELLO_FAILED = 0
OFPET_BAD_REQUEST = 1
OFPET_BAD_ACTION = 2
OFPET_BAD_INSTRUCTION = 3
OFPET_BAD_MATCH = 4
OFPET_FLOW_MOD_FAILED = 5
OFPET_GROUP_MOD_FAILED = 6
OFPET_PORT_MOD_FAILED = 7
OFPET_TABLE_MOD_FAILED = 8
OFPET_QUEUE_OP_FAILED = 9
OFPET_SWITCH_CONFIG_FAILED = 10
OFPET_ROLE_REQUEST_FAILED = 11
OFPET_EXPERIMENTER = 65535

ofp_error_type_map = {
    0: 'OFPET_HELLO_FAILED',
    1: 'OFPET_BAD_REQUEST',
    2: 'OFPET_BAD_ACTION',
    3: 'OFPET_BAD_INSTRUCTION',
    4: 'OFPET_BAD_MATCH',
    5: 'OFPET_FLOW_MOD_FAILED',
    6: 'OFPET_GROUP_MOD_FAILED',
    7: 'OFPET_PORT_MOD_FAILED',
    8: 'OFPET_TABLE_MOD_FAILED',
    9: 'OFPET_QUEUE_OP_FAILED',
    10: 'OFPET_SWITCH_CONFIG_FAILED',
    11: 'OFPET_ROLE_REQUEST_FAILED',
    65535: 'OFPET_EXPERIMENTER',
}

# Identifiers from group ofp_flow_mod_command
OFPFC_ADD = 0
OFPFC_MODIFY = 1
OFPFC_MODIFY_STRICT = 2
OFPFC_DELETE = 3
OFPFC_DELETE_STRICT = 4

ofp_flow_mod_command_map = {
    0: 'OFPFC_ADD',
    1: 'OFPFC_MODIFY',
    2: 'OFPFC_MODIFY_STRICT',
    3: 'OFPFC_DELETE',
    4: 'OFPFC_DELETE_STRICT',
}

# Identifiers from group ofp_flow_mod_failed_code
OFPFMFC_UNKNOWN = 0
OFPFMFC_TABLE_FULL = 1
OFPFMFC_BAD_TABLE_ID = 2
OFPFMFC_OVERLAP = 3
OFPFMFC_EPERM = 4
OFPFMFC_BAD_TIMEOUT = 5
OFPFMFC_BAD_COMMAND = 6
OFPFMFC_BAD_FLAGS = 7

ofp_flow_mod_failed_code_map = {
    0: 'OFPFMFC_UNKNOWN',
    1: 'OFPFMFC_TABLE_FULL',
    2: 'OFPFMFC_BAD_TABLE_ID',
    3: 'OFPFMFC_OVERLAP',
    4: 'OFPFMFC_EPERM',
    5: 'OFPFMFC_BAD_TIMEOUT',
    6: 'OFPFMFC_BAD_COMMAND',
    7: 'OFPFMFC_BAD_FLAGS',
}

# Identifiers from group ofp_flow_mod_flags
OFPFF_SEND_FLOW_REM = 1
OFPFF_CHECK_OVERLAP = 2
OFPFF_RESET_COUNTS = 4

ofp_flow_mod_flags_map = {
    1: 'OFPFF_SEND_FLOW_REM',
    2: 'OFPFF_CHECK_OVERLAP',
    4: 'OFPFF_RESET_COUNTS',
}

# Identifiers from group ofp_flow_removed_reason
OFPRR_IDLE_TIMEOUT = 0
OFPRR_HARD_TIMEOUT = 1
OFPRR_DELETE = 2
OFPRR_GROUP_DELETE = 3

ofp_flow_removed_reason_map = {
    0: 'OFPRR_IDLE_TIMEOUT',
    1: 'OFPRR_HARD_TIMEOUT',
    2: 'OFPRR_DELETE',
    3: 'OFPRR_GROUP_DELETE',
}

# Identifiers from group ofp_group
OFPG_MAX = 4294967040
OFPG_ALL = 4294967292
OFPG_ANY = 4294967295

ofp_group_map = {
    4294967040: 'OFPG_MAX',
    4294967292: 'OFPG_ALL',
    4294967295: 'OFPG_ANY',
}

# Identifiers from group ofp_group_capabilities
OFPGFC_SELECT_WEIGHT = 1
OFPGFC_SELECT_LIVENESS = 2
OFPGFC_CHAINING = 4
OFPGFC_CHAINING_CHECKS = 8

ofp_group_capabilities_map = {
    1: 'OFPGFC_SELECT_WEIGHT',
    2: 'OFPGFC_SELECT_LIVENESS',
    4: 'OFPGFC_CHAINING',
    8: 'OFPGFC_CHAINING_CHECKS',
}

# Identifiers from group ofp_group_mod_command
OFPGC_ADD = 0
OFPGC_MODIFY = 1
OFPGC_DELETE = 2

ofp_group_mod_command_map = {
    0: 'OFPGC_ADD',
    1: 'OFPGC_MODIFY',
    2: 'OFPGC_DELETE',
}

# Identifiers from group ofp_group_mod_failed_code
OFPGMFC_GROUP_EXISTS = 0
OFPGMFC_INVALID_GROUP = 1
OFPGMFC_WEIGHT_UNSUPPORTED = 2
OFPGMFC_OUT_OF_GROUPS = 3
OFPGMFC_OUT_OF_BUCKETS = 4
OFPGMFC_CHAINING_UNSUPPORTED = 5
OFPGMFC_WATCH_UNSUPPORTED = 6
OFPGMFC_LOOP = 7
OFPGMFC_UNKNOWN_GROUP = 8
OFPGMFC_CHAINED_GROUP = 9
OFPGMFC_BAD_TYPE = 10
OFPGMFC_BAD_COMMAND = 11
OFPGMFC_BAD_BUCKET = 12
OFPGMFC_BAD_WATCH = 13
OFPGMFC_EPERM = 14

ofp_group_mod_failed_code_map = {
    0: 'OFPGMFC_GROUP_EXISTS',
    1: 'OFPGMFC_INVALID_GROUP',
    2: 'OFPGMFC_WEIGHT_UNSUPPORTED',
    3: 'OFPGMFC_OUT_OF_GROUPS',
    4: 'OFPGMFC_OUT_OF_BUCKETS',
    5: 'OFPGMFC_CHAINING_UNSUPPORTED',
    6: 'OFPGMFC_WATCH_UNSUPPORTED',
    7: 'OFPGMFC_LOOP',
    8: 'OFPGMFC_UNKNOWN_GROUP',
    9: 'OFPGMFC_CHAINED_GROUP',
    10: 'OFPGMFC_BAD_TYPE',
    11: 'OFPGMFC_BAD_COMMAND',
    12: 'OFPGMFC_BAD_BUCKET',
    13: 'OFPGMFC_BAD_WATCH',
    14: 'OFPGMFC_EPERM',
}

# Identifiers from group ofp_group_type
OFPGT_ALL = 0
OFPGT_SELECT = 1
OFPGT_INDIRECT = 2
OFPGT_FF = 3

ofp_group_type_map = {
    0: 'OFPGT_ALL',
    1: 'OFPGT_SELECT',
    2: 'OFPGT_INDIRECT',
    3: 'OFPGT_FF',
}

# Identifiers from group ofp_hello_failed_code
OFPHFC_INCOMPATIBLE = 0
OFPHFC_EPERM = 1

ofp_hello_failed_code_map = {
    0: 'OFPHFC_INCOMPATIBLE',
    1: 'OFPHFC_EPERM',
}

# Identifiers from group ofp_instruction_type
OFPIT_GOTO_TABLE = 1
OFPIT_WRITE_METADATA = 2
OFPIT_WRITE_ACTIONS = 3
OFPIT_APPLY_ACTIONS = 4
OFPIT_CLEAR_ACTIONS = 5
OFPIT_EXPERIMENTER = 65535

ofp_instruction_type_map = {
    1: 'OFPIT_GOTO_TABLE',
    2: 'OFPIT_WRITE_METADATA',
    3: 'OFPIT_WRITE_ACTIONS',
    4: 'OFPIT_APPLY_ACTIONS',
    5: 'OFPIT_CLEAR_ACTIONS',
    65535: 'OFPIT_EXPERIMENTER',
}

# Identifiers from group ofp_match_type
OFPMT_STANDARD = 0
OFPMT_OXM = 1

ofp_match_type_map = {
    0: 'OFPMT_STANDARD',
    1: 'OFPMT_OXM',
}

# Identifiers from group ofp_oxm_class
OFPXMC_NXM_0 = 0
OFPXMC_NXM_1 = 1
OFPXMC_OPENFLOW_BASIC = 32768
OFPXMC_EXPERIMENTER = 65535

ofp_oxm_class_map = {
    0: 'OFPXMC_NXM_0',
    1: 'OFPXMC_NXM_1',
    32768: 'OFPXMC_OPENFLOW_BASIC',
    65535: 'OFPXMC_EXPERIMENTER',
}

# Identifiers from group ofp_packet_in_reason
OFPR_NO_MATCH = 0
OFPR_ACTION = 1
OFPR_INVALID_TTL = 2

ofp_packet_in_reason_map = {
    0: 'OFPR_NO_MATCH',
    1: 'OFPR_ACTION',
    2: 'OFPR_INVALID_TTL',
}

# Identifiers from group ofp_port
OFPP_MAX = 4294967040
OFPP_IN_PORT = 4294967288
OFPP_TABLE = 4294967289
OFPP_NORMAL = 4294967290
OFPP_FLOOD = 4294967291
OFPP_ALL = 4294967292
OFPP_CONTROLLER = 4294967293
OFPP_LOCAL = 4294967294

ofp_port_map = {
    4294967040: 'OFPP_MAX',
    4294967288: 'OFPP_IN_PORT',
    4294967289: 'OFPP_TABLE',
    4294967290: 'OFPP_NORMAL',
    4294967291: 'OFPP_FLOOD',
    4294967292: 'OFPP_ALL',
    4294967293: 'OFPP_CONTROLLER',
    4294967294: 'OFPP_LOCAL',
}

# Identifiers from group ofp_port_config
OFPPC_PORT_DOWN = 1
OFPPC_NO_RECV = 4
OFPPC_NO_FWD = 32
OFPPC_NO_PACKET_IN = 64

ofp_port_config_map = {
    1: 'OFPPC_PORT_DOWN',
    4: 'OFPPC_NO_RECV',
    32: 'OFPPC_NO_FWD',
    64: 'OFPPC_NO_PACKET_IN',
}

# Identifiers from group ofp_port_features
OFPPF_10MB_HD = 1
OFPPF_10MB_FD = 2
OFPPF_100MB_HD = 4
OFPPF_100MB_FD = 8
OFPPF_1GB_HD = 16
OFPPF_1GB_FD = 32
OFPPF_10GB_FD = 64
OFPPF_40GB_FD = 128
OFPPF_100GB_FD = 256
OFPPF_1TB_FD = 512
OFPPF_OTHER = 1024
OFPPF_COPPER = 2048
OFPPF_FIBER = 4096
OFPPF_AUTONEG = 8192
OFPPF_PAUSE = 16384
OFPPF_PAUSE_ASYM = 32768

ofp_port_features_map = {
    1: 'OFPPF_10MB_HD',
    2: 'OFPPF_10MB_FD',
    4: 'OFPPF_100MB_HD',
    8: 'OFPPF_100MB_FD',
    16: 'OFPPF_1GB_HD',
    32: 'OFPPF_1GB_FD',
    64: 'OFPPF_10GB_FD',
    128: 'OFPPF_40GB_FD',
    256: 'OFPPF_100GB_FD',
    512: 'OFPPF_1TB_FD',
    1024: 'OFPPF_OTHER',
    2048: 'OFPPF_COPPER',
    4096: 'OFPPF_FIBER',
    8192: 'OFPPF_AUTONEG',
    16384: 'OFPPF_PAUSE',
    32768: 'OFPPF_PAUSE_ASYM',
}

# Identifiers from group ofp_port_mod_failed_code
OFPPMFC_BAD_PORT = 0
OFPPMFC_BAD_HW_ADDR = 1
OFPPMFC_BAD_CONFIG = 2
OFPPMFC_BAD_ADVERTISE = 3
OFPPMFC_EPERM = 4

ofp_port_mod_failed_code_map = {
    0: 'OFPPMFC_BAD_PORT',
    1: 'OFPPMFC_BAD_HW_ADDR',
    2: 'OFPPMFC_BAD_CONFIG',
    3: 'OFPPMFC_BAD_ADVERTISE',
    4: 'OFPPMFC_EPERM',
}

# Identifiers from group ofp_port_no
OFPP_ANY = 4294967295

ofp_port_no_map = {
    4294967295: 'OFPP_ANY',
}

# Identifiers from group ofp_port_reason
OFPPR_ADD = 0
OFPPR_DELETE = 1
OFPPR_MODIFY = 2

ofp_port_reason_map = {
    0: 'OFPPR_ADD',
    1: 'OFPPR_DELETE',
    2: 'OFPPR_MODIFY',
}

# Identifiers from group ofp_port_state
OFPPS_LINK_DOWN = 1
OFPPS_BLOCKED = 2
OFPPS_LIVE = 4

ofp_port_state_map = {
    1: 'OFPPS_LINK_DOWN',
    2: 'OFPPS_BLOCKED',
    4: 'OFPPS_LIVE',
}

# Identifiers from group ofp_queue_op_failed_code
OFPQOFC_BAD_PORT = 0
OFPQOFC_BAD_QUEUE = 1
OFPQOFC_EPERM = 2

ofp_queue_op_failed_code_map = {
    0: 'OFPQOFC_BAD_PORT',
    1: 'OFPQOFC_BAD_QUEUE',
    2: 'OFPQOFC_EPERM',
}

# Identifiers from group ofp_queue_properties
OFPQT_MIN_RATE = 1
OFPQT_MAX_RATE = 2
OFPQT_EXPERIMENTER = 65535

ofp_queue_properties_map = {
    1: 'OFPQT_MIN_RATE',
    2: 'OFPQT_MAX_RATE',
    65535: 'OFPQT_EXPERIMENTER',
}

# Identifiers from group ofp_role_request_failed_code
OFPRRFC_STALE = 0
OFPRRFC_UNSUP = 1
OFPRRFC_BAD_ROLE = 2

ofp_role_request_failed_code_map = {
    0: 'OFPRRFC_STALE',
    1: 'OFPRRFC_UNSUP',
    2: 'OFPRRFC_BAD_ROLE',
}

# Identifiers from group ofp_stats_reply_flags
OFPSF_REPLY_MORE = 1

ofp_stats_reply_flags_map = {
    1: 'OFPSF_REPLY_MORE',
}

# Identifiers from group ofp_stats_types
OFPST_DESC = 0
OFPST_FLOW = 1
OFPST_AGGREGATE = 2
OFPST_TABLE = 3
OFPST_PORT = 4
OFPST_QUEUE = 5
OFPST_GROUP = 6
OFPST_GROUP_DESC = 7
OFPST_GROUP_FEATURES = 8
OFPST_EXPERIMENTER = 65535

ofp_stats_types_map = {
    0: 'OFPST_DESC',
    1: 'OFPST_FLOW',
    2: 'OFPST_AGGREGATE',
    3: 'OFPST_TABLE',
    4: 'OFPST_PORT',
    5: 'OFPST_QUEUE',
    6: 'OFPST_GROUP',
    7: 'OFPST_GROUP_DESC',
    8: 'OFPST_GROUP_FEATURES',
    65535: 'OFPST_EXPERIMENTER',
}

# Identifiers from group ofp_switch_config_failed_code
OFPSCFC_BAD_FLAGS = 0
OFPSCFC_BAD_LEN = 1
OFPSCFC_EPERM = 2

ofp_switch_config_failed_code_map = {
    0: 'OFPSCFC_BAD_FLAGS',
    1: 'OFPSCFC_BAD_LEN',
    2: 'OFPSCFC_EPERM',
}

# Identifiers from group ofp_table
OFPTT_MAX = 254
OFPTT_ALL = 255

ofp_table_map = {
    254: 'OFPTT_MAX',
    255: 'OFPTT_ALL',
}

# Identifiers from group ofp_table_config
OFPTC_TABLE_MISS_CONTROLLER = 0
OFPTC_TABLE_MISS_CONTINUE = 1
OFPTC_TABLE_MISS_DROP = 2
OFPTC_TABLE_MISS_MASK = 3

ofp_table_config_map = {
    0: 'OFPTC_TABLE_MISS_CONTROLLER',
    1: 'OFPTC_TABLE_MISS_CONTINUE',
    2: 'OFPTC_TABLE_MISS_DROP',
    3: 'OFPTC_TABLE_MISS_MASK',
}

# Identifiers from group ofp_table_mod_failed_code
OFPTMFC_BAD_TABLE = 0
OFPTMFC_BAD_CONFIG = 1
OFPTMFC_EPERM = 2

ofp_table_mod_failed_code_map = {
    0: 'OFPTMFC_BAD_TABLE',
    1: 'OFPTMFC_BAD_CONFIG',
    2: 'OFPTMFC_EPERM',
}

# Identifiers from group ofp_type
OFPT_HELLO = 0
OFPT_ERROR = 1
OFPT_ECHO_REQUEST = 2
OFPT_ECHO_REPLY = 3
OFPT_EXPERIMENTER = 4
OFPT_FEATURES_REQUEST = 5
OFPT_FEATURES_REPLY = 6
OFPT_GET_CONFIG_REQUEST = 7
OFPT_GET_CONFIG_REPLY = 8
OFPT_SET_CONFIG = 9
OFPT_PACKET_IN = 10
OFPT_FLOW_REMOVED = 11
OFPT_PORT_STATUS = 12
OFPT_PACKET_OUT = 13
OFPT_FLOW_MOD = 14
OFPT_GROUP_MOD = 15
OFPT_PORT_MOD = 16
OFPT_TABLE_MOD = 17
OFPT_STATS_REQUEST = 18
OFPT_STATS_REPLY = 19
OFPT_BARRIER_REQUEST = 20
OFPT_BARRIER_REPLY = 21
OFPT_QUEUE_GET_CONFIG_REQUEST = 22
OFPT_QUEUE_GET_CONFIG_REPLY = 23
OFPT_ROLE_REQUEST = 24
OFPT_ROLE_REPLY = 25

ofp_type_map = {
    0: 'OFPT_HELLO',
    1: 'OFPT_ERROR',
    2: 'OFPT_ECHO_REQUEST',
    3: 'OFPT_ECHO_REPLY',
    4: 'OFPT_EXPERIMENTER',
    5: 'OFPT_FEATURES_REQUEST',
    6: 'OFPT_FEATURES_REPLY',
    7: 'OFPT_GET_CONFIG_REQUEST',
    8: 'OFPT_GET_CONFIG_REPLY',
    9: 'OFPT_SET_CONFIG',
    10: 'OFPT_PACKET_IN',
    11: 'OFPT_FLOW_REMOVED',
    12: 'OFPT_PORT_STATUS',
    13: 'OFPT_PACKET_OUT',
    14: 'OFPT_FLOW_MOD',
    15: 'OFPT_GROUP_MOD',
    16: 'OFPT_PORT_MOD',
    17: 'OFPT_TABLE_MOD',
    18: 'OFPT_STATS_REQUEST',
    19: 'OFPT_STATS_REPLY',
    20: 'OFPT_BARRIER_REQUEST',
    21: 'OFPT_BARRIER_REPLY',
    22: 'OFPT_QUEUE_GET_CONFIG_REQUEST',
    23: 'OFPT_QUEUE_GET_CONFIG_REPLY',
    24: 'OFPT_ROLE_REQUEST',
    25: 'OFPT_ROLE_REPLY',
}

# Identifiers from group ofp_vlan_id
OFPVID_NONE = 0
OFPVID_PRESENT = 4096

ofp_vlan_id_map = {
    0: 'OFPVID_NONE',
    4096: 'OFPVID_PRESENT',
}
