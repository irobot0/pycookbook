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

# An example of a client that connects to an SSL server
# and verifies its certificate

from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
import ssl

s = socket(AF_INET, SOCK_STREAM)

# Wrap with an SSL layer and require the server to present its certificate
ssl_s = ssl.wrap_socket(s,
                        cert_reqs=ssl.CERT_REQUIRED,
                        ca_certs='server_cert.pem'
                        )

ssl_s.connect(('localhost', 20000))

# Communicate with the server
ssl_s.send(b'Hello World!')
resp = ssl_s.recv(8192)
print('Got: ', resp)

# Done
ssl_s.close()
