from pydantic import BaseModel
import pyinputplus as pyip

###############BaseModel#############
class Recipe(BaseModel):
    ingredients:list[str]
    mealType:str
    prepTime:int

SandwichIngredient = ["ham", "bread", "cheese" "tomatoes"]
cakeIngredient = ["flour", "sugar", "eggs."]
saladIngredient = ["avocado", "arugula", "tomatoes", "spinach"]

###############CookBook#############

cookbook: dict[str, Recipe] = {
    "sanwdiw" : Recipe(ingredients = SandwichIngredient, mealType="lunch", prepTime=10),
    "cake" : Recipe(ingredients = cakeIngredient, mealType="dessert", prepTime=60),
    "salad" : Recipe(ingredients = saladIngredient, mealType="spinach.", prepTime=15)
}

###############useful functions to handle cookbook:s#############

def reciptName():
	for key in cookbook.keys():
			print(f"name : {key}")

def recipeDetails(name:str):
	"""display details of a recipe"""
	recipe:Recipe | None = cookbook.get(name)
	if recipe != None:
		print(f"Ingredients list: {recipe.ingredients}")
		print(f"To be eaten for {recipe.mealType}.")
		print(f"Takes {recipe.prepTime} minutes of cooking.")




################ add recipe into the cookbook#####################


def deleteRecipe(name:str):
	"""take name recipe then delete it from the cookbook"""
	recipe:Recipe | None = cookbook.get(name)
	if recipe != None:
		cookbook.pop(name)

def ingredientToAdd():
	"""list of ingredient to add"""
	count = 0
	listIngredient = []
	ingredient:str =""
	while count < 3:
		ingredient = input("Enter ingredient :")
		if ingredient.isalpha():
			count += 1
			listIngredient.append(ingredient)
		else:
			print("only letter")
	return listIngredient


def inputStrToAdd():
	"""name of new recipe to add"""
	nameRecipe = ""
	while True:
		nameRecipe = input("Enter name :")
		if nameRecipe.isalpha():
			return nameRecipe
		else:
			print("only letter")


def timeOfNewRecipe():
	"""preparation time:"""
	time = pyip.inputNum('Enter a preparation time: ', min=1)
	return time


def addRecipe():
	mealName:str = inputStrToAdd()
	newIngredient:list[str] = ingredientToAdd()
	typeMeal:str = inputStrToAdd()
	prepTime:int = timeOfNewRecipe()

	newRecipe = Recipe(ingredients = newIngredient, mealType=typeMeal, prepTime=prepTime)
	cookbook[mealName] = newRecipe

	print("\n")

# timeOfNewRecipe()
# print(ingredientToAdd() )
# def addRecipe()
# timeOfNewRecipe()
# input_list = [ map(str,input().split()) for x in range(3)]
# input_list = [ int(input()) for x in range(3)]