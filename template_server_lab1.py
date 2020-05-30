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
    return p


def decode_data(packet_bytes) -> Packet:
    # TODO: implement this function
    p = Packet(PacketType.BAD_NUMBER)
    return p


def decode_rrq(packet_bytes) -> Packet:
    # TODO: implement this function
    p = Packet(PacketType.BAD_NUMBER)
    return p


def decode_wrq(packet_bytes) -> Packet:
    # TODO: implement this function
    p = Packet(PacketType.BAD_NUMBER)
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


############################################


def setup_sockets(server_ip_address, server_port_number):
    """
    Feel free to delete this function.
    """
    pass


def server_logic(server_ip_address, server_port_number):
    setup_sockets(server_ip_address, server_port_number)

    # TODO: put the rest of the server logic
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

    # NEVER remove the command line arguments or ignore them.
    # ALWAYS use them in your code, as the grader will pass them
    # to your code the same way.
    ip_address = get_arg(1, "127.0.0.1")    # IP address of the server
    port_number = int(get_arg(2, "69")) # Change the default value for development if you want.
    server_logic(ip_address, port_number)


if __name__ == "__main__":
    main()
