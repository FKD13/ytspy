from urllib import request
from os import *


FIFO = 'music.fifo'


class Searcher:
    def __init__(self):
        self._results = []
    
    def search(self, search_term: list):
        content = request.urlopen(f"https://www.youtube.com/results?search_query={'+'.join(search_term)}")
        content = content.read().decode()
        content = content.replace('\n','').replace('<', '\n<').split('\n')
        self._results.clear()
        for line in content:
            if line.startswith('<a href="/watch') and len(line.split('"')[1]) == 20:
                link = line.split('"')
                self._results.append({
                    "url": 'https://www.youtube.com' + link[1],
                    "title": link[7]
                })
        self.print_results()

    def print_results(self):
        for i, vid in enumerate(self._results):
            print(f'[{i}] {vid["title"]}')


class Command:
    def execute_command(self, args: list):
        pass


class SearchCmd(Command):
    def __init__(self):
        self.searcher = Searcher()

    def execute_command(self, args: list):
        if args is not None:
            self.searcher.search(args)
        else:
            print("[search] You have to pass arguments")


class ListCmd(Command):
    def __init__(self, searcher: Searcher):
        self.searcher = searcher

    def execute_command(self, args: list):
        self.searcher.print_results()


class PlayCmd(Command):
    def __init__(self, searcher: Searcher):
        self.searcher = searcher

    def execute_command(self, args: list):
        if len(args) == 1 and args[0].isnumeric() and int(args[0]) >= 0 and int(args[0]) < len(self.searcher._results):
            system(f'echo "loadfile {self.searcher._results[int(args[0])]["url"]} append-play" >> {FIFO}')
        else:
            print(f'[play] Usage: play [0 <= number <= {len(self.searcher._results)}]')


class CommandExecutor:
    def __init__(self):
        s = SearchCmd()
        self._sub_commands = {
            "search" : s,
            "list" : ListCmd(s.searcher),
            "play" : PlayCmd(s.searcher)
        }

    def handle_string(self, line: str):
        args = line.split(' ')
        if len(args) >= 1:
            if args[0] in self._sub_commands:
                self._sub_commands[args[0]].execute_command(args[1:] if len(args) > 1 else None)
            else:
                print("Command not found")
        else:
            print("No input")


c = CommandExecutor() 
while True:
    c.handle_string(input("> "))

