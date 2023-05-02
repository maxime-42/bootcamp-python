from typing import Type
from datetime import datetime
import sys
from recipe import Recipe

    
class Book():
    def __init__(self, name="CookBook"):
        self.name = name
        self.creation_date = self.get_time()
        self.last_update = self.creation_date

        self.cookbook: dict[str, list] = {"starter" : [], "lunch" : [], "dessert" : []}

    def add_recipe(self, recipe:Recipe):
        """Add a recipe to the cook book and update last_update"""
        try:
            if not isinstance(recipe, Recipe):
                raise TypeError("Unexpected type")
        except TypeError as error_msg:
            print(error_msg)
        else:
            self.cookbook[recipe.recipe_type].append(recipe)
            self.last_update = self.get_time()
            
    def get_time(self):
            return datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f")

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for recipe_list in self.cookbook.values():
            for recipe in recipe_list:
                if recipe.name == name:
                    return recipe
        print("{name} Doesn't exist in the cookbook")

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        try :
            return   [ recipe.name for recipe in self.cookbook[recipe_type]]
        except KeyError as error_msg:
            print("{error_msg}")
