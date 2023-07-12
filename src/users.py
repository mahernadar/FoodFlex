from typing import List


class User(object):
    def __init__(
        self, age: int, weight: float, height: float, diet: str
    ) -> None:
        self.id = NotImplemented
        self.age = age
        self.weight = weight
        self.height = height
        self.liked_recipes = None
        self.restricted_ingredients = None

    def submit_restricted_ingredients(self, ingredients: List(str)):
        NotImplemented

    def submit_liked_recipes(self, ingredients: List(str)):
        NotImplemented

    def recommend_meals(self, number_of_days: int, meals_per_day: int):
        NotImplemented

    def recommend_based_on_available_ingredients(
        self, number_of_days: int, meals_per_day: int
    ):
        NotImplemented

    def calculate_ingredients_quantities(self):
        NotImplemented

    def get_shopping_list(self):
        NotImplemented

    def adjust_recipes_quantities_based_on_calories(self):
        NotImplemented
