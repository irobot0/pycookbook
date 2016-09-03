#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to implement a network service involving sockets where servers and
clients authenticate themselves and encrypt the transmitted data using SSL.
"""


"""
SOLUTION
"""

from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
from socket import SOL_SOCKET
from socket import SO_REUSEADDR
import ssl

KEYFILE = 'server_key.pem'      # Private key of the server
CERTFILE = 'server_cert.pem'    # Server certivficate (given to client)


def echo_client(conn):
    while True:
        data = conn.recv(8192)
        if data == b'':
            break
        else:
            conn.send(data)
    conn.close()
    print('Connection closed.')


def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(address)
    s.listen(1)

    # Wrap with an SSL layer requiring client certs.
    s_ssl = ssl.wrap_socket(s,
                            keyfile=KEYFILE,
                            certfile=CERTFILE,
                            server_side=True
                            )

    # Wait for connections.
    while True:
        try:
            conn, addr = s_ssl.accept()
            print('Got connection: ', conn, addr)
            echo_client(conn)
        except Exception as e:
            print('{}: {}'.format(e.__class__.__name__, e))


echo_server(('', 20000))
