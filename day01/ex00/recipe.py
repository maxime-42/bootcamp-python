import sys

class Recipe():
    def __init__(self, name=None, cook_lvl=None, cook_time=None, ingredients=None, description=None, recipe_type=None):
        if None in locals().values():
            print("Null argument not expected", file=sys.stdout)
            exit()
        try:
            self.name = str(name)
            self.cooking_lvl = int(cook_lvl)
            self.cooking_time = int(cook_time)
            self.ingredients = list(ingredients)
            self.description = str(description)
            self.recipe_type = str(recipe_type)

            if len(name) == 0:
                raise Exception("Recipe is name empty")
            if cook_lvl > 5 or cook_lvl < 1:
                raise Exception("Cooking level is not between 1 and 5")
            if cook_time < 0:
                raise Exception("Moron ! Time is not negative...")
            if len(ingredients) == 0:
                raise Exception("No ingredients required?")
            if recipe_type not in ['lunch', 'starter', 'dessert']:
                raise Exception("Recipe type not correct, choose 'starter' or 'lunch' or 'dessert'")
        except Exception as e:
            print("Recipy exception raised:", repr(e), file=sys.stdout)
            exit()
        
    def __str__(self):
        txt = f"{self.name},{ self.cooking_lvl}, {self.cooking_time}, {self.ingredients}, {self.ingredients}, {self.description}, {self.recipe_type}"
        return (txt)
