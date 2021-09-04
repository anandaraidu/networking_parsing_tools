import socket 
import common_utils as cutils
from collections import namedtuple
import time


def server_send(sock, buff ):
    print(f"Sending of Len: {len(buff)}")
    sock.send( buff )

def server_recv( sock, bufflen):
    return cutils.receive_n_bytes( bufflen , sock )


def execute_server_step( sock, stepnum, st ):
    recvd = server_recv( sock, st.client.bufflen)
    print(f"Server: Step: {stepnum} success sent:{st.client.bufflen} recvd:{recvd}\n")
    assert( recvd == st.client.bufflen )
    server_send( sock, st.server.buff)

def server_program( ):
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    #server_socket.bind((host, port))  # bind host address and port together
    server_socket.bind((cutils.HOST, cutils.PORT))  # bind host address and port together

    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))

    steps = cutils.test_pair()
    for stepnum, step in enumerate(steps):
        execute_server_step( conn, stepnum, step)

    print(" All server steps are complete")
    tmp = input()
    conn.close()  # close the connection

if __name__ == '__main__':
    server_program()

