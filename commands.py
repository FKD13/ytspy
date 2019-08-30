#!/usr/bin/env python3
from searcher import *
from command_sender import *
from printer import *
from colorama import *
from re import match


class Command:
    def execute_command(self, args: List[str]) -> None:
        pass


class SearchCmd(Command):
    def __init__(self):
        self.searcher = Searcher()

    def execute_command(self, args: List[str]) -> None:
        if args is not None:
            self.searcher.search(args)
        else:
            Printer.print(f"{Fore.RED}[search] You have to pass arguments")


class ListCmd(Command):
    def __init__(self, searcher: Searcher):
        self.searcher = searcher

    def execute_command(self, args: List[str]) -> None:
        self.searcher.print_results()


class PlayCmd(Command):
    def __init__(self, searcher: Searcher):
        self.searcher = searcher

    def parse_to_range(self, interval: str) -> List[int]:
        if match('[0-9]+-[0-9]', interval):
            interval = interval.split('-')
            num1 = interval[0]
            num2 = interval[1]
            if not num1.isnumeric() or not num2.isnumeric():
                Printer.print(f"{Fore.RED}[Play] Usage: play [interval: 0-12]... [separate numbers]...")
                return []
            return [i for i in range(int(num1), int(num2) + 1)]
        elif interval.isnumeric():
            return [int(interval)]
        return []

    def execute_command(self, args: List[str]) -> None:
        search_results = self.searcher.get_results()
        numbers = []
        for arg in args:
            numbers += self.parse_to_range(arg)
        for number in numbers:
            if 0 <= number <= len(search_results):
                CommandSender.send(f"loadfile {search_results[number]} append-play")
            else:
                Printer.print(f"{Fore.RED}[Play] could not find song {number}")


class SkipCmd(Command):
    def execute_command(self, args: List[str]) -> None:
        CommandSender.send("playlist-next")


class ClearCmd(Command):
    def execute_command(self, args: List[str]) -> None:
        CommandSender.send("playlist-clear")


class QuitCmd(Command):
    def execute_command(self, args: List[str]) -> None:
        quit(0)
