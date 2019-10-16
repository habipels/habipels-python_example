#!/usr/bin/python
import socket

sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM )
host_adresi = "192.168.43.1"
port_degeri = 53

def port_tarama(port):
    if sock.connect_ex((host_adresi,port)):
        print("{} bu port kapalıdır".format(port))
    else : 
        print("{} bu port açıktır".format(port))

port_tarama(port_degeri)