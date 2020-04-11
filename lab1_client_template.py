# Don't forget to change this file's name before submission.
import sys
import os
import enum

############################################
############# O B J E C T S ################
############################################
# Logical objects to be used in your code.
############################################


class PacketType(enum.Enum):
    """
    Represents a TFTP packet type

    Fill in the remaining type numbers
    as the RFC.
    """
    RRQ = 1
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
    # Example of making ACK packet.
    p = Packet(PacketType.ACK)
    # Note that this field is added but
    # it's not defined in the constructor.
    # use the same way to make other packets.
    p.blk = blk
    return p


def make_rrq(file_name) -> Packet:
    # TODO: implement this function
    pass


def make_wrq(file_name) -> Packet:
    # TODO: implement this function
    pass


def make_data(blk, data) -> Packet:
    # TODO: implement this function
    pass


############################################
############ D E C O D E R S ###############
############################################
# The following methods convert byte arrays
# received from sockets to packet objects.
############################################
def decode_ack(packet_bytes) -> Packet:
    # TODO: implement this function
    pass


def decode_rrq(packet_bytes) -> Packet:
    # TODO: implement this function
    pass


def decode_wrq(packet_bytes) -> Packet:
    # TODO: implement this function
    pass


def decode_data(packet_bytes) -> Packet:
    # TODO: implement this function
    pass


def decode_packet_bytes(packet_bytes) -> Packet:
    """
    Accepts packet bytes received 
    from socket. the first 2 bytes have
    the packet type according to the RFC.

    Extract the packet type then call the
    appropriate function from decode_***
    accordingly.
    """
    # TODO: implement this function
    # Learn about Array slicing in Python.
    packet_type_bytes = packet_bytes[:2]
    pass

############################################
############ E N C O D E R S ###############
############################################
# The following methods convert Packet
# objects to bytes to make them ready to be
# sent using sockets.
############################################


def encode_ack(packet: Packet) -> bytes:
    # TODO: implement this function
    pass


def encode_rrq(packet: Packet) -> bytes:
    # TODO: implement this function
    pass


def encode_wrq(packet: Packet) -> bytes:
    # TODO: implement this function
    pass


def encode_data(packet: Packet) -> bytes:
    # TODO: implement this function
    pass


def encode_packet_bytes(packet: Packet) -> bytes:
    """
    Convert the packet object to an array
    of bytes to be sent to the socket.

    Convert the object according to the
    order of fields and their sizes in the
    RFC.
    """
    if packet.packet_type == PacketType.ACK:
        return encode_ack(packet)

    # .. etc
    # TODO: implement this function
    pass
############################################


def setup_sockets(address):
    """
    Socket logic MUST NOT be written in the TftpProcessor
    class. It knows nothing about the sockets.

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
    matches = re.findall(r"(\d{4}_)+lab1\.(py|rar|zip)", script_name)
    if not matches:
        print(f"[WARN] File name is invalid [{script_name}]")
    pass


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

    ip_address = get_arg(1, "127.0.0.1")    # IP address of the server
    operation = get_arg(2, "pull")
    file_name = get_arg(3, "test.txt")

    # Modify this as needed.
    if operation == "push":
        print(f"Attempting to upload [{file_name}]...")
        push_operation(file_name, ip_address)
    elif operation == "pull":
        print(f"Attempting to download [{file_name}]...")
        pull_operation(file_name, ip_address)


if __name__ == "__main__":
    main()
