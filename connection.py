import socket
import json
import config as c_
import requests
import reddit_api_fondler as r_a_f

class Connection:
    def __init__(self):
        self.socket = None
        self.buffer = None

    def connect(self, host, port):
    #   makes socket
        self.socket = socket.socket()
        self.socket.connect((host, port))
    
    def send(self, *data):
    #   packages data for encoding and sends
        data = ' '.join(data) + '\r\n'
        self.socket.send(bytes((data), 'utf-8'))

    def recv(self):
    #   grabs lines, stores to buffer and reads
        data = self.socket.recv(4096)
        if self.buffer is not None:
            data = self.buffer + data
            self.buffer = None
        lines = data.split(b'\r\n')
        for line in range(len(lines) -1):
            line = str(lines[line], 'utf-8', 'replace')
            yield line
        last_line = lines[-1]
        if last_line:
            self.buffer = last_line

    def discoball(self):
    #   disconnect
        self.socket.close()
        self.socket = None

    def establish_connection(self):
    #   start connection
        self.connect(c_.bot_config.host, c_.bot_config.port)
        self.send('USER ' + (c_.bot_config.user + ' ')*3 + 'python bot')
        self.send('NICK ' + c_.bot_config.nick)
        self.send('JOIN ' + c_.bot_config.channel)
    




connection = Connection()
connection.establish_connection()