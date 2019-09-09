#!/bin/python3
import json
from typing import Dict, List
from printer import Printer
from colorama import Fore


class PlaylistManager:
    def __init__(self, file: str = None):
        self._file = file if file is not None else "playlists.json"
        self._playlists: Dict[List[List[str]]] = self._load()

    def _load(self) -> Dict[List[List]]:
        try:
            with open(self._file, 'r') as f:
                return json.loads(f.read())
        except FileNotFoundError:
            Printer.print(f"{Fore.RED}Error: Could not load file: {self._file}")
            Printer.print(f"{Fore.RED}Creating file: {self._file}")
            with open(self._file, 'w') as f:
                f.write(json.dumps({}))
            return {}

    def save(self) -> None:
        with open(self._file) as f:
            f.write(json.dumps(self._playlists))

    def get_playlist(self, name: str) -> List[List[str]]:
        return self._playlists[name] if name in self._playlists else {}




