# This file is part of Scapy
# See http://www.secdev.org/projects/scapy for more information
# Copyright (C) Nils Weiss <nils@we155.de>
# This program is published under a GPLv2 license

# scapy.contrib.description = XCP over CAN(CAN-XCP)
# scapy.contrib.status = loads

import scapy.modules.six as six
from scapy.config import LINUX
from scapy.layers.can import CAN
from scapy.packet import Packet, bind_layers, bind_bottom_up
from scapy.fields import ByteEnumField, ShortField, ByteField,\
    FlagsField, XBitField, ThreeBytesField, StrFixedLenField


class CAN_XCP(Packet):
    name = "Universal calibration and measurement protocol"
    fields_desc = [
        FlagsField('flags', 0, 3, ['error',
                                   'remote_transmission_request',
                                   'extended']),
        XBitField('identifier', 0, 29),
        ByteField('length', 8),
        ThreeBytesField('reserved', 0),
    ]

    def extract_padding(self, p):
        return p, None


class CRO(Packet):
    commands = {
        0x01: "CONNECT",
        0x1B: "GET_CCP_VERSION",
        0x17: "EXCHANGE_ID",
        0x12: "GET_SEED",
        0x13: "UNLOCK",
        0x02: "SET_MTA",
        0x03: "DNLOAD",
        0x23: "DNLOAD_6",
        0x04: "UPLOAD",
        0x0F: "SHORT_UP",
        0x11: "SELECT_CAL_PAGE",
        0x14: "GET_DAQ_SIZE",
        0x15: "SET_DAQ_PTR",
        0x16: "WRITE_DAQ",
        0x06: "START_STOP",
        0x07: "DISCONNECT",
        0x0C: "SET_S_STATUS",
        0x0D: "GET_S_STATUS",
        0x0E: "BUILD_CHKSUM",
        0x10: "CLEAR_MEMORY",
        0x18: "PROGRAM",
        0x22: "PROGRAM_6",
        0x19: "MOVE",
        0x05: "TEST",
        0x09: "GET_ACTIVE_CAL_PAGE",
        0x08: "START_STOP_ALL",
        0x20: "DIAG_SERVICE",
        0x21: "ACTION_SERVICE"
    }
    name = 'Command Receive Object'



class CTO(Packet):
    commands = {
        0xFF: "CONNECT",
        0xFE: "DISCONNECT",
        0xFD: "GET_STATUS",
        0xF0: "DOWNLOAD",
        0xEF: "DDOWNLOAD_NEXT",
        0xEE: "DOWNLOAD_MAX",
        0xED: "DSHORT_DOWNLOAD",
        0xEC: "DMODIFY_BITS",
        0xEB: "DSET_CAL_PAGE",
        0xEA: "DGET_CAL_PAGE",
        0xE9: "DGET_PAG_PROCESSOR_INFO",
        0xE8: "DGET_SEGMENT_INFO",
        0xE7: "DGET_PAGE_INFO",
        0xE6: "DSET_SEGMENT_MODE",
        0xE5: "DGET_SEGMENT_MODE",
        0xE4: "DCOPY_CAL_PAGE",
        0xE2: "DSET_DAQ_PTR",
        0xE1: "DWRITE_DAQ",
        0xE0: "DSET_DAQ_LIST_MODE",
        0xDE: "DSTART_STOP_DAQ_LIST",
        0xDD: "DSTART_STOP_SYNCH",
        0xC7: "DWRITE_DAQ_MULTIPLE",
        0xDB: "DREAD_DAQ",
        0xDC: "DGET_DAQ_CLOCK",
        0xDA: "DGET_DAQ_PROCESSOR_INFO",
        0xD9: "DGET_DAQ_RESOLUTION_INFO",
        0xD8: "DGET_DAQ_LIST_INFO",
        0xD7: "DGET_DAQ_EVENT_INFO",
        0xE3: "DCLEAR_DAQ_LIST",
        0xD8: "DGET_DAQ_LIST_INFO",
        0xD6: "DFREE_DAQ",
        0xD5: "DALLOC_DAQ",
        0xD4: "DALLOC_ODT",
        0xD3: "DALLOC_ODT_ENTRY",
        0xD2: "PROGRAM_START",
        0xD1: "PROGRAM_CLEAR",
        0xD0: "PROGRAM",
        0xCF: "PROGRAM_RESET",
        0xCE: "GET_PGM_PROCESSOR_INFO",
        0xCD: "GET_SECTOR_INFO",
        0xCC: "PROGRAM_PREPARE",
        0xCB: "PROGRAM_FORMAT",
        0xCA: "PROGRAM_NEXT",
        0xC9: "PROGRAM_MAX",
        0xC8: "PROGRAM_VERIFY",

    }
    name = 'Command Transfer Object'

    fields_desc = [
        ByteEnumField('cmd', 0x01, commands),
    ]



# ##### CTO COMMANDS ######

# STANDARD COMMANDS


class CONNECT(Packet):
    commands = {0x00: 'NORMAL', 0x01: 'USER_DEFINED'}
    fields_desc = [
        ByteEnumField('connection_mode', 0x1, commands),
    ]


bind_layers(CTO, CONNECT, cmd=0xFF)


class DISCONNECT(Packet):
    # DISCONNECT has not data
    pass


bind_layers(CTO, DISCONNECT, cmd=0xFE)


class GET_STATUS(Packet):
    # GET_STATU has not data
    pass


bind_layers(CTO, GET_STATUS, cmd=0xFD)


class SYNCH(Packet):
    pass
    # TODO implement SYNCH


bind_layers(CTO, SYNCH, cmd=0xFC)


class GET_COMM_MODE_INFO(Packet):
    # GET_COMM_MODE_INFO has no data
    pass


bind_layers(CTO, GET_COMM_MODE_INFO, cmd=0xFB)


class GET_ID(Packet):
    # TODO Implement GET ID from ASAM Standard
    pass


bind_layers(CTO, GET_ID, cmd=0xFA)


class SET_REQUEST(Packet):
    # TODO Implement SET_REQUEST from ASAM Standard
    pass


bind_layers(CTO, SET_REQUEST, cmd=0xF9)


class GET_SEED(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, GET_SEED, cmd=0xF8)


class UNLOCK(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, UNLOCK, cmd=0xF7)


class SET_MTA(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, SET_MTA, cmd=0xF6)


class UPLOAD(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, UPLOAD, cmd=0xF5)


class SHORT_UPLOAD(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, SHORT_UPLOAD, cmd=0xF4)


class BUILD_CHECKSUM(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, BUILD_CHECKSUM, cmd=0xF3)


class TRANSPORT_LAYER_CMD(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, TRANSPORT_LAYER_CMD, cmd=0xF2)


class USER_CMD(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, USER_CMD, cmd=0xF1)


# Calibration Commands

class DOWNLOAD(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, DOWNLOAD, cmd=0xF0)


class DOWNLOAD_NEXT(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, DOWNLOAD_NEXT, cmd=0xEF)


class DOWNLOAD_MAX(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, DOWNLOAD_MAX, cmd=0xEE)


class SHORT_DOWNLOAD(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, SHORT_DOWNLOAD, cmd=0xED)


class MODIFY_BITS(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, MODIFY_BITS, cmd=0xEC)


# Page Switchting commands


class SET_CAL_PAGE(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, SET_CAL_PAGE, cmd=0xEB)


class GET_CAL_PAGE(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, GET_CAL_PAGE, cmd=0xEA)


class GET_PAG_PROCESSOR_INFO(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, GET_PAG_PROCESSOR_INFO, cmd=0xE9)


class GET_SEGMENT_INFO(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, GET_SEGMENT_INFO, cmd=0xE8)


class GET_PAGE_INFO(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, GET_PAGE_INFO, cmd=0xE7)


class SET_SEGMENT_MODE(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, SET_SEGMENT_MODE, cmd=0xE6)


class GET_SEGMENT_MODE(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, GET_SEGMENT_MODE, cmd=0xE5)


class COPY_CAL_PAGE(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, COPY_CAL_PAGE, cmd=0xE4)


# Cyclic Data exchange Basic commands


class SET_DAQ_PTR(Packet):
    # TOOD implement from ASAM Standard
    pass


bind_layers(CTO, SET_DAQ_PTR, cmd=0xE2)


class WRITE_DAQ(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, WRITE_DAQ, cmd=0xE1)


class SET_DAQ_LIST_MODE(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, SET_DAQ_LIST_MODE, cmd=0xE0)


class START_STOP_DAQ_LIST(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, START_STOP_DAQ_LIST, cmd=0xDE)


class START_STOP_SYNCH(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, START_STOP_SYNCH, cmd=0xDD)


class WRITE_DAQ_MULTIPLE(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, WRITE_DAQ_MULTIPLE, cmd=0xC7)


class READ_DAQ(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, READ_DAQ, cmd=0xDB)


class GET_DAQ_CLOCK(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, GET_DAQ_CLOCK, cmd=0xDC)


class GET_DAQ_PROCESSOR_INFO(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, GET_DAQ_PROCESSOR_INFO, cmd=0xDA)


class GET_DAQ_RESOLUTION_INFO(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, GET_DAQ_RESOLUTION_INFO, cmd=0xD9)


class GET_DAQ_LIST_INFO(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, GET_DAQ_LIST_INFO, cmd=0xD8)


class GET_DAQ_EVENT_INFO(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, GET_DAQ_EVENT_INFO, cmd=0xD7)


# Cyclic data transfer - static configuration commands


class CLEAR_DAQ_LIST(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, CLEAR_DAQ_LIST, cmd=0xE3)


class GET_DAQ_LIST_INFO(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, GET_DAQ_LIST_INFO, cmd=0xD8)


# Cyclic Data transfer - dynamic configuration commands


class FREE_DAQ(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, FREE_DAQ, cmd=0xD6)


class ALLOC_DAQ(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, ALLOC_DAQ, cmd=0xD5)


class ALLOC_ODT(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, ALLOC_ODT, cmd=0xD4)


class ALLOC_ODT_ENTRY(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, ALLOC_ODT_ENTRY, cmd=0xD3)


# Flash Programming commands


class PROGRAM_START(Packet):
    # TDOD implement from ASAM Standard
    pass


bind_layers(CTO, PROGRAM_START, cmd=0xD2)


class PROGRAM_CLEAR(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, PROGRAM_CLEAR, cmd=0xD1)


class PROGRAM(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, PROGRAM, cmd=0xD0)


class PROGRAM_RESET(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, PROGRAM_RESET, cmd=0xCF)


class GET_PGM_PROCESSOR_INFO(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, GET_PGM_PROCESSOR_INFO, cmd=0xCE)


class GET_SECTOR_INFO(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, GET_SECTOR_INFO, cmd=0xCD)


class PROGRAM_PREPARE(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, PROGRAM_PREPARE, cmd=0xCC)


class PROGRAM_FORMAT(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, PROGRAM_FORMAT, cmd=0xCB)


class PROGRAM_NEXT(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, PROGRAM_NEXT, cmd=0xCA)


class PROGRAM_MAX(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, PROGRAM_MAX, cmd=0xC9)


class PROGRAM_VERIFY(Packet):
    # TODO implement from ASAM Standard
    pass


bind_layers(CTO, PROGRAM_VERIFY, cmd=0xC8)


# ##### DTOs #####
class DEFAULT_DTO(Packet):
    fields_desc = [
        StrFixedLenField('load', b'\xff' * 5, length=5)
    ]


class CONNECT_DTO(Packet):
    resource = {}
    comm_mode_basic = {}
    fields_desc = [
        ByteEnumField('resource', 1, resource),
        ByteEnumField('comm_mode_basic',
                      2, comm_mode_basic),
        ByteField('max_cto', 3),
        ShortField('max_dto', 5),
        ByteField('xcp_protocol_layer_version_number_msb', 6),
        ByteField('xcp_transport_layer_version_number_msb', 7)
    ]


class GET_STATUS_DTO(Packet):
    pass


class DTO(Packet):
    __slots__ = Packet.__slots__ + ["payload_cls"]

    packet_ids = {0xFF: 'POSITIVE', 0xFE: 'NEGATIVE'}

    fields_desc = [
        ByteEnumField("packet_id", "POSITIVE", packet_ids)
    ]

    def __init__(self, *args, **kwargs):
        self.payload_cls = DEFAULT_DTO
        if "payload_cls" in kwargs:
            self.payload_cls = kwargs["payload_cls"]
            del kwargs["payload_cls"]
        Packet.__init__(self, *args, **kwargs)

    @staticmethod
    def get_dto_cls(sent_cmd):
        try:
            return {
                0xFF: CONNECT_DTO,
                0xFD: GET_STATUS_DTO
            }[sent_cmd]
        except KeyError:
            return DEFAULT_DTO

    def answers(self, other):
        if not hasattr(other, "cmd"):
            return 0

        payload_cls = self.get_dto_cls(other.cmd)
        if self.payload_cls != payload_cls:
            data = bytes(self.load)
            self.remove_payload()
            self.add_payload(payload_cls(data))
            self.payload_cls = payload_cls
            self.payload_cls = payload_cls
        return 1


bind_layers(CAN_XCP, DTO)
# ##### DTOs ######


class XCP_Port():
    """ Reresentation of a XCP Port,
        Holds all infomration of a found port.
    """
    def __init__(self, request_id, response_id, cto_connet_answer):
        self.__answer_msg = cto_connet_answer
        self.__request_id = request_id
        self.__response_id = response_id

    def get_request_id(self):
        return self.__request_id

    def get_response_id(self):
        return self.__response_id

    def __str__(self):
        return """  Found XCP Port
                    Request ID: 0x%x
                    Response ID: 0x%x
                    Comm_Mode: 0x%x, Resource: 0x%x,
                    max_cto: %d, max_dto: %d,
                    portocol_verison: %d, transport_version: %d
               """ % (self.__request_id, self.__response_id,
                      self.__answer_msg.comm_mode_basic,
                      self.__answer_msg.resource,
                      self.__answer_msg.max_cto, self.__answer_msg.max_dto,
                      self.__answer_msg.xcp_protocol_layer_version_number_msb,
                      self.__answer_msg.xcp_transport_layer_version_number_msb)


class XCP_SCANNER():
    """
    Main class for scanning
    """
    def __init__(self, can_socket, start, end, use_extended_can_id,
                 verbose, timeout=0.02):
        """
        Constructor
        :param can_socket: Socket where scan is happening
        :param start: Start ID for scanning
        :param end: Last ID for scanning
        :param use_extended_can_id: True if extended IDs are used
        :param verbose: Select verbosing
        :param timeout: Timeout for receiveing messiages
        """
        self.__socket = can_socket
        self.__start = start
        self.__end = end
        self.__use_extended_can_id = use_extended_can_id
        self.__receive_thread = None
        self.__send_thread = None
        self.__results = list()
        self.__verbose = verbose
        self.__known_ids = list()
        self.__flags = 0
        if use_extended_can_id:
            self.__flags = "extended"

        if six.PY2 or not LINUX:
            self.__socket.timeout = timeout
        else:
            self.__socket.ins.settimeout(timeout)  # Set RX-timeout of socket

    def get_known_ids(self):
        """
        Wakes up CAN and safes all ids on the bus
        """
        dummy_pkt = CAN(identifier=0x123,
                        data=b'\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA')
        known_ids = list()
        lsend = lambda: self.__socket.send(dummy_pkt)
        backrdn_pkts = self.__socket.sniff(timeout=5,
                                           started_callback=lsend)
        for p in backrdn_pkts:
            if p.identifier not in known_ids:
                known_ids.append(p)
        return known_ids

    def KNOWN_IDS(self):
        return self.__known_ids

    def __add_answers_to_list(self, sent, recv):
        """ Check if port has been found and add it to list """
        if recv.identifier in self.__known_ids:
            return
        if recv.length != 8:
            self.__known_ids.append(recv.identifier)
            return
        try:
            recv_cto = CONNECT_DTO(bytes(recv.payload))
        except IOError:
            self.__known_ids.append(recv.identifier)
            return
        if (recv.data[0] == 0xFF and recv.length == 8):
            self.__results.append(XCP_Port(sent.identifier,
                                           recv.identifier, recv_cto))

    def start_scan(self):
        """Starts the Scan"""
        self.__known_ids = self.get_known_ids()

        # Craft connect packet
        sent = CAN(identifier=self.__start, length=2, flags=self.__flags)
        sent = sent / CTO(cmd="CONNECT")
        sent = sent / CONNECT(connection_mode="NORMAL")

        recv_callback = lambda recv: self.__add_answers_to_list(sent, recv)
        lsend = lambda: self.__socket.send(sent)
        while sent.identifier <= self.__end:
            #  Sniff for responses after sending
            self.__socket.sniff(prn=recv_callback,
                                timeout=0.01, started_callback=lsend)
            sent.identifier += 1

    def get_results(self):
        """ Getter for results """
        return self.__results
