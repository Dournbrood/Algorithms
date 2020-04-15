#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # We simply iterate through the dict and floor divide all the elements.
    num_batches = None
    if len(ingredients.items()) < len(recipe.items()):
        return 0

    for ingredient, amount in ingredients.items():
        if amount // recipe[ingredient] < 1:
            return 0
        else:
            if num_batches == None:
                num_batches = amount // recipe[ingredient]
            if amount // recipe[ingredient] < num_batches:
                num_batches = amount // recipe[ingredient]
    return num_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
