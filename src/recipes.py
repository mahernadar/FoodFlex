class Recipe(object):
    def __init__(
        self,
        ingredients,
        name,
        nutrition_facts,
        accepted_diets,
        embedding,
        link,
    ):
        self.ingredients = ingredients
        self.name = name
        self.nutrition_facts = nutrition_facts
        self.accepted_diets = accepted_diets
        self.embedding = embedding
        self.link = link
        self.config = {}

    def get_ingredients_quantities_metric_units(self):
        NotImplemented

    def adjust_ingredients_quantities_based_on_goal(self, goal):
        NotImplemented
        # update the recipe's config dict...
