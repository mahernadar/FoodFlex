import sys

sys.path.insert(0, "../")  # needed for using the utils file in the notebook.

from utils import (
    RECIPE_TITLE_EMBEDDINGS,
    RECIPES_METADATA,
    INGREDIENTS_INDICES,
    RECOMMENDABLE_TITLE_EMBEDDINGS,
)
from sentence_transformers import util
import torch
from typing import Union, List
from pprint import pprint

ALL_INGREDIENTS_INDICES = INGREDIENTS_INDICES.ingredient_index.astype(
    str
).tolist()

device = "mps" if torch.backends.mps.is_available() else "cpu"


class RecipeRecommender(object):
    def __init__(
        self,
        input_recipes_indices: List[str],
    ) -> None:
        self.input_recipes_indices = input_recipes_indices
        self.get_corpus_embeddings()
        self.get_query_combined_embedding()

    def recommend(self, k: int):
        self.recommended_recipes = util.semantic_search(
            self.query_combined_embedding,
            self.corpus_embeddings,
            score_function=util.dot_score,
            top_k=k,
        )

    def get_corpus_embeddings(self):
        """
        getting the embeddings of all non-singular-ingredient recipes,
        normalizing and turning into matrix:
        """

        #TODO: remove the indices that were selected in the query:
        corpus_embeddings = torch.stack(
            list(RECOMMENDABLE_TITLE_EMBEDDINGS.values())
        )
        corpus_embeddings_normalized = util.normalize_embeddings(
            corpus_embeddings
        )
        
        corpus_embeddings_normalized = torch.squeeze(
            corpus_embeddings_normalized, dim=1
        )

        self.corpus_embeddings = corpus_embeddings_normalized

    def get_query_combined_embedding(self):
        """
        Retrieve the indices of the ingredients or recipes that were input and take the mean of their
        embedding values:
        """
        query_embeddings = [
            RECIPE_TITLE_EMBEDDINGS[index].to(device)
            for index in self.input_recipes_indices
        ]
        query_embeddings = torch.stack(query_embeddings)
        query_embeddings_normalized = util.normalize_embeddings(
            query_embeddings
        )
        query_combined_embedding = torch.mean(
            query_embeddings_normalized, dim=0
        )

        self.query_combined_embedding = query_combined_embedding


if __name__ == "__main__":

    print("starting hummus recommendations... \n")
    # get recommended recipes based on one of the hummus recipes:
    hummus_index = [300, 21051]

    cols = ['title', 'sorted_NER']

    print("recipe title: ", RECIPES_METADATA.iloc[hummus_index]['title'])

    print("ingredients: ", RECIPES_METADATA.iloc[hummus_index]['sorted_NER'])


    input_indices = [str(i) for i in hummus_index]

    print("searching for similar recipes ...")

    recipe_recommender = RecipeRecommender(input_recipes_indices=input_indices)
    recipe_recommender.recommend(k=5)
    print(recipe_recommender.recommended_recipes)

