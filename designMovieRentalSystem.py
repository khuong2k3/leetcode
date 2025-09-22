from collections import defaultdict
from dataclasses import dataclass
import heapq


@dataclass
class Movie:
    shop: int
    movie: int
    price: int

    def toList(self):
        return [self.shop, self.movie, self.price]

    def toTuple(self):
        return (self.shop, self.movie, self.price)


class MovieRentingSystem:
    def __init__(self, n: int, entries: list[list[int]]):
        self.n: int = n
        self.moviesDict: defaultdict[int, list[tuple[int, Movie]]] = defaultdict(list)
        self.rented: set[tuple[int, int, int]] = set()
        for entry in entries:
            movieValue = Movie(entry[0], entry[1], entry[2])
            heapq.heappush(self.moviesDict[entry[0]], (entry[2], movieValue))
            # self.rented[(movieValue.shop, movieValue.movie)] = movieValue.price

    def search(self, movie: int) -> list[int]:
        movieList = self.moviesDict.get(movie)
        if movieList is None:
            return []
        for _, m in movieList:
            if m.toTuple() in self.rented:
                continue

            return m.toList()
        return []

    def rent(self, shop: int, movie: int) -> None:
        self.moviesDict[movie][0]
        # self.rented[(shop, movie)]

        return None

    def drop(self, shop: int, movie: int) -> None:
        return None

    def report(self) -> list[list[int]]:
        return []


