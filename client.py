import socket
import common_utils as cutils
from collections import namedtuple

def client_send(sock, buff ):
    sock.send( buff )

def client_recv( sock, bufflen):
    return cutils.receive_n_bytes( bufflen , sock)


def execute_client_step( sock, stepnum, st ):
    client_send( sock, st.client.buff)
    recvd = client_recv( sock, st.server.bufflen)
    print(f"Step: {stepnum} success sent:{st.client.bufflen} recvd:{recvd}\n")
    assert( recvd == st.server.bufflen )

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    #client_socket.connect((host, port))  # connect to the server
    client_socket.connect((cutils.HOST, cutils.PORT))  # connect to the server

    steps = cutils.test_pair()
    for stepnum, step in enumerate(steps):
        execute_client_step( client_socket, stepnum, step)

    print(" All client steps are complete")
    tmp = input()
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()

