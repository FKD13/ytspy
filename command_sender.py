#!/bin/python3
# the fifo used to send commands to mpv
from os import *

FIFO = 'music.fifo'


class CommandSender:

    @staticmethod
    def send(message: str) -> None:
        system(f'echo "{message}" >> {FIFO}')
