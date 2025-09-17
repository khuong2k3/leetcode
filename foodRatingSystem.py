from collections import defaultdict
from dataclasses import dataclass
import heapq


@dataclass
class Food:
    cuisine: str
    rating: int


class FoodRatings:
    foods: dict[str, Food]
    cuisines: dict[str, list[tuple[int, str]]]

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.foods = {}
        self.cuisines = defaultdict(lambda: [])

        for cuisine, food, rating in zip(cuisines, foods, ratings):
            self.foods[food] = Food(cuisine, rating)
            heapq.heappush(self.cuisines[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        currentFood = self.foods[food]
        currentFood.rating = newRating
        heapq.heappush(self.cuisines[currentFood.cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        foods = self.cuisines[cuisine]
        if len(foods) == 0:
            return ""

        while True:
            food = foods[0]
            if -food[0] != self.foods[food[1]].rating:
                _ = heapq.heappop(foods)
            else:
                return food[1]

