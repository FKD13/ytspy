#!/bin/python3
from searcher import *
from command_sender import *


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
            print("[search] You have to pass arguments")


class ListCmd(Command):
    def __init__(self, searcher: Searcher):
        self.searcher = searcher

    def execute_command(self, args: List[str]) -> None:
        self.searcher.print_results()


class PlayCmd(Command):
    def __init__(self, searcher: Searcher):
        self.searcher = searcher

    def execute_command(self, args: List[str]) -> None:
        search_results = self.searcher.get_results()
        if len(args) == 1 and args[0].isnumeric() and 0 <= int(args[0]) < len(search_results):
            CommandSender.send(f"loadfile {search_results[int(args[0])]} append-play")
        else:
            print(f'[play] Usage: play [0 <= number <= {len(search_results)}]')


class SkipCmd(Command):
    def execute_command(self, args: List[str]) -> None:
        CommandSender.send("playlist-next")


class ClearCmd(Command):
    def execute_command(self, args: List[str]) -> None:
        CommandSender.send("playlist-clear")


class QuitCmd(Command):
    def execute_command(self, args: List[str]) -> None:
        quit(0)
