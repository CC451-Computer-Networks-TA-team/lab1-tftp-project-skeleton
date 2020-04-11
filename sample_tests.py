import sys
import binascii
import traceback

# Try to import client or server
try:
    from template_client_lab1 import *
    MODE = "CLIENT"
except:
    try:
        from template_server_lab1 import *
        MODE = "SERVER"
    except Exception as e:
        print(e)
        msg = "No modules found. If you renamed the template, please import"\
            " the correct file name here."
        print(msg)
        exit(-1)


####################################################
####################################################
############# H A C K Y   C O D E S ################
####################################################
####################################################
# https://stackoverflow.com/questions/5762491/how-to-print-color-in-console-using-system-out-println
# https://www.linuxjournal.com/article/8603
# those guys don't work on poor windows (mostly)
ANSI_RESET = "\u001B[0m"
ANSI_RED = "\u001B[31m"
ANSI_GREEN = "\u001B[32m"


def print_red(text):
    print(f"{ANSI_RED}{text}{ANSI_RESET}")


def print_green(text):
    print(f"{ANSI_GREEN}{text}{ANSI_RESET}")


def caller_info():
    caller_stackframe = sys._getframe().f_back.f_back
    function_name = caller_stackframe.f_code.co_name
    line_num = caller_stackframe.f_lineno

    return function_name, line_num


def do_assert(correct, actual, case=""):
    fn_name, fn_lineno = caller_info()
    if correct != actual:
        msg_hd = f"Line {fn_lineno} [failed] {fn_name}: {case}"
        msg_tl = f" \nExpected ( %s ) got ( %s )\n" % (
            correct, actual)
        print_red(msg_hd+msg_tl)
    else:
        print_green(f"[success] {fn_name}: {case}")


def run_test(function):
    try:
        function()
    except Exception as e:
        exc_traceback = sys.exc_info()[2]
        # Caller's traceback.
        exc_traceback = exc_traceback.tb_next
        print_red(f"Line {exc_traceback.tb_lineno} threw an exception: {e}")

####################################################
####################################################


def test_decode_ack_packet():
    # this is NOT a string. It's a byte literal (byte array).
    # treat this as an array in your code and it'll work.
    raw = b'\x00\x04\x00\x01'
    ack_packet = decode_ack(raw)

    actual_value = ack_packet.packet_type
    correct_value = PacketType.ACK
    case = "Decode ACK packet. [Packet Type]"
    do_assert(correct_value, actual_value, case)

    actual_value = ack_packet.blk
    correct_value = 1
    case = "Decode ACK packet. [Block Number]"
    do_assert(correct_value, actual_value, case)


def test_encode_ack_packet():
    p = Packet(PacketType.ACK)
    p.blk = 1

    actual_value = encode_ack(p)
    correct_value = b'\x00\x04\x00\x01'
    case = "Encode ACK packet."
    do_assert(correct_value, actual_value, case)


def test_decode_data_packet():
    raw = b'\x00\x03\x00\x01'
    data_packet = decode_data(raw)

    actual_value = data_packet.packet_type
    correct_value = PacketType.DATA
    case = "Decode DATA packet [Packet Type]."
    do_assert(correct_value, actual_value, case)

    actual_value = data_packet.data
    correct_value = b'\x00\x01'
    case = "Decode DATA packet [Data]."
    do_assert(correct_value, actual_value, case)


def test_encode_data_packet():
    p = Packet(PacketType.DATA)
    p.data = b'\x00\x01'

    actual_value = encode_data(p)
    correct_value = b'\x00\x03\x00\x01'
    case = "Encode DATA packet."
    do_assert(correct_value, actual_value, case)


def test_decode_rrq():
    raw = b"\x00\x01\x74\x65\x73\x74\x2e\x74\x78\x74\x00\x6f\x63\x74\x65\x74\x00"
    rrq = decode_rrq(raw)

    actual_value = rrq.packet_type
    correct_value = PacketType.RRQ
    case = "Decode RRQ packet [Packet Type]."
    do_assert(correct_value, actual_value, case)

    actual_value = rrq.file_name
    # Note that there's no NULL(\0) at the end of the string
    correct_value = "test.txt"
    case = "Decode RRQ packet [File name]."
    do_assert(correct_value, actual_value, case)

    actual_value = rrq.mode
    # Note that there's no NULL(\0) at the end of the string
    correct_value = "octet"
    case = "Decode RRQ packet [Mode]."
    do_assert(correct_value, actual_value, case)


def test_encode_rrq():
    p = Packet(PacketType.RRQ)
    p.mode = "octet"
    p.file_name = "test.txt"

    actual_value = encode_rrq(p)
    correct_value = b"\x00\x01\x74\x65\x73\x74\x2e\x74\x78\x74\x00\x6f\x63\x74\x65\x74\x00"
    case = "Encode RRQ packet."
    do_assert(correct_value, actual_value, case)


def test_rrq():
    if MODE == "CLIENT":
        run_test(test_encode_rrq)
    elif MODE == "SERVER":
        run_test(test_decode_rrq)


def main():
    """
    Leave as is. There're no syntax errors here.
    """
    run_test(test_encode_ack_packet)
    run_test(test_decode_ack_packet)
    run_test(test_encode_data_packet)
    run_test(test_decode_data_packet)
    run_test(test_rrq)


if __name__ == "__main__":
    main()
