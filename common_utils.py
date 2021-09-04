import socket 
from collections import namedtuple
import binary_utils as butils
import smb_parser as smb

#HOST = '172.19.154.198'
HOST = '127.0.0.1'
PORT =  445

step = namedtuple( 'step', ['buff', 'bufflen'])
step_pair = namedtuple('step_pair', ['client', 'server'])

def test_pair_1():
    c1 = 'Hi who are you?'.encode()
    s1 = 'I am ananda'.encode()


    c2 = 'How are you doing?'.encode()
    s2 = 'Im doing really great'.encode()
    print(f"clsend1:{len(c1)} srsend1:{len(s1)} clsend2:{len(c2)} srsend2:{len(s2)}")

    st1 = step_pair( step(c1, len(c1)), step(s1, len(s1)))
    st2  = step_pair( step(c2, len(c2)), step(s2, len(s2)))
    return [st1, st2]

def test_pair():
    SMB_READ_REQ_FILE  = 'readRequest.payload'
    SMB_READ_RESP_FILE  = 'readResponse.payload'

    c1 = butils.file_to_bytes(  SMB_READ_REQ_FILE )
    s1 = butils.file_to_bytes(  SMB_READ_RESP_FILE )

    print(f"clsend1:{len(c1)} srsend1:{len(s1)} ")

    req = smb.modify_read_req_filelen(c1, 600 * 1024)
    resp = smb.modify_read_resp_filelen(s1, 600 * 1024)
    butils.bytes_to_file( req,  'request_600k')
    butils.bytes_to_file( resp,  'response_600k')
    st1 = step_pair( step(req, len(req)), step(resp, len( resp)))
    return [st1]

def receive_n_bytes( recvlen , conn):
    recvd = 0
    remaining = recvlen

    while remaining > 0:
        data = conn.recv(1024)
        if not data:
            print("Breaking from here....\n")
            break

        rsz = len(data)
        if (rsz > remaining):
            print("Sync between client and server lost")
            x = 1/0
        recvd += rsz
        remaining -= rsz
        print(f"Received: {rsz} total:{recvd} remain:{remaining}")

    print(f"Step:Received {recvd} bytes")
    return recvd
