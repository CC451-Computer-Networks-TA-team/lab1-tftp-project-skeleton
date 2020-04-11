# Don't forget to change this file's name before submission.
import sys
import os
import enum


class PacketType(enum.Enum):
    """
    Represents a TFTP packet type

    Fill in the remaining type numbers
    as the RFC.
    """
    BAD_NUMBER = -1  # Placeholder, don't use this.
    RRQ = 1
    DATA = 3
    # Put other packet types here.
    # TODO: implement this enum.
    ACK = 4


class Packet(object):
    """
    Represents a TFTP packet.

    Leave as is.
    To know how to use this class, check make_ack function.
    """

    def __init__(self, packet_type: PacketType):
        self.packet_type = packet_type


def make_ack(blk) -> Packet:
    """
    Makes an ACK packet.

    This function is complete.
    """
    # Example of making ACK packet.
    p = Packet(PacketType.ACK)
    # Note that this field is added but
    # it's not defined in the constructor.
    # use the same way to make other packets.
    p.blk = blk
    return p

############################################
############ D E C O D E R S ###############
############################################
# The following methods convert byte arrays
# received from sockets to packet objects.
############################################


def decode_ack(packet_bytes) -> Packet:
    # TODO: implement this function
    p = Packet(PacketType.BAD_NUMBER)
    # Fill packet values.
    return p


def decode_data(packet_bytes) -> Packet:
    # TODO: implement this function
    p = Packet(PacketType.BAD_NUMBER)
    # Fill packet values.
    return p

############################################
############ E N C O D E R S ###############
############################################
# The following methods convert Packet
# objects to bytes to make them ready to be
# sent using sockets.
############################################


def encode_ack(packet: Packet) -> bytes:
    # TODO: implement this function
    return b''


def encode_data(packet: Packet) -> bytes:
    # TODO: implement this function
    return b''


def encode_rrq(packet: Packet) -> bytes:
    # TODO: implement this function
    return b''


def encode_wrq(packet: Packet) -> bytes:
    # TODO: implement this function
    return b''


############################################


def setup_sockets(address):
    """
    Feel free to delete this function.
    """
    pass


def pull_operation(file_name, ip_address):
    # TODO: implement this function
    # Do the logic for download
    pass


def push_operation(file_name, ip_address):
    # TODO: implement this function
    # Do the logic for upload
    pass

# TODO: Feel free to add functions here, don't repeat code please.
# def transfer_data(server_socket):
#     pass

############################################
################ L E A V E #################
################ A L O N E #################


def check_file_name():
    """
    Do NOT use this function.

    Leave as is.
    """
    script_name = os.path.basename(__file__)
    import re
    regexp_str = r"(\d{4,})(_\d{4,})?_(client|server)_lab1\.py"
    matches = re.findall(regexp_str, script_name)
    if not matches:
        print(f"[WARN] File name is invalid [{script_name}]")
    else:
        print("[LOG] Valid filename.")


def get_arg(param_index, default=None):
    """
    Gets a command-line argument by index
    falling back to a default value on error.

    Leave as is.
    """
    try:
        return sys.argv[param_index]
    except IndexError as e:
        if default:
            return default
        else:
            print(e)
            print(
                f"[FATAL] The comamnd-line argument #[{param_index}] is missing")
            exit(-1)    # Program execution failed.


def main():
    """
    Leave as is.
    """
    print("*" * 50)
    print("[LOG] Printing command line arguments\n", ",".join(sys.argv))
    check_file_name()
    print("*" * 50)

    operation = get_arg(1, "pull")
    file_name = get_arg(2, "test.txt")
    server_ip_address = get_arg(3, "127.0.0.1")    # IP address of the server
    server_port = get_arg(4, 69)    # Port number of the server

    # Modify this as needed.
    if operation == "push":
        print(f"Attempting to upload [{file_name}]...")
        push_operation(file_name, server_ip_address)
    elif operation == "pull":
        print(f"Attempting to download [{file_name}]...")
        pull_operation(file_name, server_ip_address)


if __name__ == "__main__":
    main()
