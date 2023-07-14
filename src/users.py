from typing import List


class User(object):
    def __init__(
        self,
        age: int,
        weight: float,  # KG
        height: float,
        diet: str,
        restricted_ingredients: List[str] = [],
        daily_calories_goal: int = None,
    ) -> None:
        self.id = NotImplemented
        self.diet = diet
        self.age = age
        self.weight = weight
        self.height = height
        self.nutritional_goals = {}
        self.liked_recipes = []
        self.restricted_ingredients = restricted_ingredients
        self.daily_calories_goal = daily_calories_goal

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

    def build_user_nutritional_values(self):
        protein_calories = self.weight * 4
        carb_calories = self.daily_calories_goal / 2.0
        fat_calories = (
            self.daily_calories_goal - carb_calories - protein_calories
        )
        self.nutritional_goals = {
            "Protein Calories": protein_calories,
            "Carbohydrates Calories": carb_calories,
            "Fat Calories": fat_calories,
        }


# todo: word2vec: sort the ingredients of each recipe alphabetically!!