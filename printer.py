#!/usr/bin/env python3
from colorama import *


class Color:
    BOLD = '\033[01m'
    BLINK = '\033[05m'
    NO_BLINK = '\033[25m'


class Printer:
    @staticmethod
    def print(message: str) -> None:
        print(f"{Style.RESET_ALL}{message}")


class Input:
    @staticmethod
    def read(message: str) -> str:
        return input(f"{Style.RESET_ALL}{message}")
