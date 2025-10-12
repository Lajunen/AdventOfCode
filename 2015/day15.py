import readfile
import os

high_score = 0
ready = 0

def day15(p):
    data = readfile.read_lines(15)

    ## ingredients = parse_data(data)
    ingredients = []
    new_ing = ingredient()
    new_ing.name = "Butterschotch"
    new_ing.capacity = -1
    new_ing.durability = -2
    new_ing.flavor = 6
    new_ing.texture = 3
    ingredients.append(new_ing)
    second = ingredient()
    second.name = "Cinnamon"
    second.capacity = 2
    second.durability = 3
    second.flavor = -2
    second.texture = -1
    ingredients.append(second)

    global high_score

    if p == 1:
        create_cookie([], ingredients)
        print("Day 15, Part 1 solution: " + str(high_score))

def parse_data(data):
    ingredients = []

    for line in data:
        line = line.replace(":", "")
        line = line.replace(",", "")
        info = line.split(" ")

        new_ing = ingredient()
        new_ing.name = info[0]
        new_ing.capacity = int(info[2])
        new_ing.durability = int(info[4])
        new_ing.flavor = int(info[6])
        new_ing.texture = int(info[8])
        new_ing.calories = int(info[10])

        ingredients.append(new_ing)
    
    return ingredients

def create_cookie(recipe, ingredients):
    amount = 0
    for part in recipe:
        amount += part[1]
    
    ## print(str(recipe))
    
    if amount == 0:
        new_recipe = []
        ## first time entering, adding 1 of each ingredient to start with
        for ing in ingredients:
            teaspoon = [ing.name, 1]
            new_recipe.append(teaspoon)

        create_cookie(new_recipe, ingredients)
        return
    
    if amount == 10:
        print(recipe)
        ## recipe full, calculating score
        score = 0

        for ing in recipe:
            for info in ingredients:
                if ing[0] == info.name:
                    ## adding points from capacity
                    part_score = ing[1] * info.capacity
                    if part_score < 0:
                        part_score = 0
                    score += part_score

                    ## adding points from durability
                    part_score = ing[1] * info.durability
                    if part_score < 0:
                        part_score = 0
                    score += part_score

                    ## adding points from flavor
                    part_score = ing[1] * info.flavor
                    if part_score < 0:
                        part_score = 0
                    score += part_score

                    ## adding points from texture
                    part_score = ing[1] * info.texture
                    if part_score < 0:
                        part_score = 0
                    score += part_score

        global high_score

        if high_score < score:
            high_score = score
        
        return
    
    if amount > 0 and amount < 10:
        for ing in ingredients:
            new_recipe = []
            for part in recipe:
                if part[0] == ing.name:
                    new_amount = part[1] + 1
                    new_teaspoon = [part[0], new_amount]
                    new_recipe.append(new_teaspoon)
                else:
                    new_teaspoon = [part[0], part[1]]
                    new_recipe.append(new_teaspoon)
            create_cookie(new_recipe, ingredients)
        return
                                

class ingredient:
    name = ""
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0

day15(1)