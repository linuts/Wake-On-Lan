'''
                    Copyright (C) 2013 Alexander B. Libby

    Wake On Lan is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation version 3.

    Wake On Lan is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Wake On Lan. If not, see <http://www.gnu.org/licenses/gpl.txt>.

    See project home page at: <https://github.com/linuts/Wake-On-Lan>
'''

import socket
from tkinter import *
from re import match
import pickle

class WakeOnLan():
    """"""

    def __init__(self, mac):
        """"""
        self.__mac = mac.replace(':', '').upper()
        if not self.__is_mac:
            raise ValueError("Invalid MAC '{0}'".format(mac))

    def __str__(self):
        """"""
        output = ""
        for index in range(len(self.__mac)):
            letter = self.__mac[index]
            if index % 2:
                output += "{0}:".format(letter)
            else:
                output += letter
        return output[:-1]

    @property
    def __is_mac(self):
        """"""
        if not match("[0-9A-Fa-f]", self.__mac) == None \
          and len(self.__mac) == 12:
            return True
        else:
            return False

    def send_packet(self):
        """"""
        data = b'\xff' * 6 + bytes().fromhex(self.__mac) * 16
        print(data)
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as stream:
            stream.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            stream.sendto(data, ("<broadcast>", 9))

class GUISettup(Tk):
    pass

class GUIWakeup(Tk):
    pass
