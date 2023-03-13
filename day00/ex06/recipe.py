"""toto"""
from typing import Type
from pydantic import BaseModel

WARNING = '\033[93m'

###############BaseModel#############
class Recipe(BaseModel):
    """the value of dictionary"""
    ingredients:list[str]
    mealType:str
    prepTime:int

sandwich_ingredient = ["ham", "bread", "cheese", "tomatoes"]
cake_ingredient = ["flour", "sugar", "eggs."]
salad_ingredient = ["avocado", "arugula", "tomatoes", "spinach"]

###############CookBook#############

cookbook: dict[str, Recipe] = {
    "sanwdiw" : Recipe(ingredients = sandwich_ingredient, mealType="lunch", prepTime=10),
    "cake" : Recipe(ingredients = cake_ingredient, mealType="dessert", prepTime=60),
    "salad" : Recipe(ingredients = salad_ingredient, mealType="spinach.", prepTime=15)
}

# ###############useful functions to handle cookbook:s#############

def  print_all_recipe_names():
    """A function that print all recipe names."""
    for key in cookbook:
        print(f"name : {key}")


def recipe_details(name:str):
    """display details of a recipe"""
    recipe:Recipe | None = cookbook.get(name)
    if recipe is not None:
        print(f"Ingredients list: {recipe.ingredients}")
        print(f"To be eaten for {recipe.mealType}.")
        print(f"Takes {recipe.prepTime} minutes of cooking.")


def delete_recipe(name:str):
    """take name recipe then delete it from the cookbook"""
    if name in cookbook:
        cookbook.pop(name)

def get_input(msg_prompt: str, condition, cast: Type = None, error_msg=None):
    """		get input content	
            check he cast 	
            check the condion 
    """
    while True:
        try:
            reponse = cast(input(msg_prompt))
            assert condition(reponse), error_msg
        except ValueError as msg:
            print(f"{WARNING}{msg}")
        except AssertionError as msg:
            print(f"{WARNING}{msg}")

        else:
            return reponse

def add_recipient():
    """list of ingredient to add"""
    warning_msg = "only be alphabet"
    name = get_input("Enter meal name:\t", lambda x: x.isalpha(), str, warning_msg)
    ingredient:list = []
    input_value:str = " "
    while len(input_value) > 0:
        input_value = get_input("Enter ingredients:\t", lambda x: x , str, warning_msg)
        ingredient.append(input_value)
    type_meal:str = get_input("Type meal:\t", lambda x: x.isalpha() > 0, str, warning_msg)
    prep_time:int  = get_input("Prep time:v\t", lambda x: x > 0, int, "only positive value")

    new_recipe = Recipe(ingredients = ingredient, mealType=type_meal, prepTime=prep_time)
    cookbook[name] =  new_recipe

def menu():
    """menu option"""
    while True:
        list_menu = "1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n>>>"
        choice  = get_input(list_menu, lambda x: x > 0 and x in (1, 2, 3, 5), int, "No valide choice")

menu()
# add_recipient()
# print_all_recipe_names()
