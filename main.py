#!/usr/bin/env python3
from commands import *
from printer import *


# Main class for handling all commands
class CommandExecutor:
    def __init__(self):
        s = SearchCmd()
        q = QuitCmd()
        self._sub_commands = {
            "search": s,
            "list": ListCmd(s.searcher),
            "play": PlayCmd(s.searcher),
            "q": q,
            "quit": q,
            "skip": SkipCmd()
        }

    def handle_string(self, line: str) -> None:
        args = line.split(' ')
        if len(args) >= 1:
            if args[0] in self._sub_commands:
                self._sub_commands[args[0]].execute_command(args[1:] if len(args) > 1 else None)
            else:
                Printer.print(f"{Fore.RED}[main] Command not found")
        else:
            Printer.print(f"{Fore.RED}[main] No input")


c = CommandExecutor() 
while True:
    c.handle_string(Input.read(f"{Fore.YELLOW}{Color.BOLD}{Color.BLINK}> {Color.NO_BLINK}"))

