#!/bin/python3
from urllib import request
from typing import List, Dict


class Searcher:
    def __init__(self):
        self._results: List[Dict[str, str]] = []

    def search(self, search_term: List[str]) -> None:
        content = request.urlopen(f"https://www.youtube.com/results?search_query={'+'.join(search_term)}")
        content = content.read().decode()
        content = content.replace('\n', '').replace('<', '\n<').split('\n')
        self._results.clear()
        for line in content:
            if line.startswith('<a href="/watch') and len(line.split('"')[1]) == 20:
                link = line.split('"')
                self._results.append({
                    "url": 'https://www.youtube.com' + link[1],
                    "title": link[7]
                })
        self.print_results()

    def get_results(self) -> List[str]:
        return [i['url'] for i in self._results]

    def print_results(self) -> None:
        for i, vid in enumerate(self._results):
            print(f'[{i}] {vid["title"]}')
