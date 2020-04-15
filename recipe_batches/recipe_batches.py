#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # We simply iterate through the dict and floor divide all the elements.
    num_batches = None
    if len(ingredients.items()) < len(recipe.items()):
        return 0

    for ingredient, amount in ingredients.items():
        flooredAmount = amount // recipe[ingredient]
        if flooredAmount < 1:
            return 0
        elif num_batches == None or flooredAmount < num_batches:
            num_batches = flooredAmount

    return num_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
