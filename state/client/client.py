import socket
from connection import *
from connect import *
import time
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

conn = Connection(sock, Connect())
conn.run()
