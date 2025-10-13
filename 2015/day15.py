import readfile
import os

high_score = 0
ready = 0

def day15(p):
    data = readfile.read_lines(15)

    ingredients = parse_data(data)

    global high_score

    if p == 1:
        create_cookie([], ingredients, 0, p)
        print("Day 15, Part 1 solution: " + str(high_score))
    
    if p == 2:
        create_cookie([], ingredients, 0, p)
        print("Day 15, Part 2 solution: " + str(high_score))

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

def create_cookie(recipe, ingredients, ingredient_number, p):
    amount = 0
    for part in recipe:
        amount += part[1]
    
    if amount == 100:
        ## recipe full, calculating score
        score = count_score(recipe, ingredients, p)

        global high_score

        if high_score < score and score != 0:
            high_score = score
        
        return
    
    if amount < 100:
        if ingredient_number == len(ingredients) - 1:
            ## last ingredient
            new_recipe = add_to_recipe(recipe, [ingredients[ingredient_number].name, 100-amount])
            create_cookie(new_recipe, ingredients, ingredient_number, p)
        else:
            ## ingredients left
            for amo in range(0, 101 - amount):
                ## loop to fill in this ingredient and moving to next
                new_recipe = add_to_recipe(recipe, [ingredients[ingredient_number].name, amo])
                create_cookie(new_recipe, ingredients, ingredient_number+1, p)

        return

def count_score(recipe, ingredients, p):
    part_capa = 0
    part_dura = 0
    part_flav = 0
    part_text = 0
    part_calo = 0

    for ing in recipe:
        for info in ingredients:
            if ing[0] == info.name:
                ## adding points of current ingredient
                part_capa += ing[1] * int(info.capacity)
                part_dura += ing[1] * int(info.durability)
                part_flav += ing[1] * int(info.flavor)
                part_text += ing[1] * int(info.texture)
                part_calo += ing[1] * int(info.calories)

    if part_capa <= 0 or part_dura <= 0 or part_flav <= 0 or part_text <= 0:
        return 0
    else:
        if p == 1:
            return part_capa * part_dura * part_flav * part_text
        if p == 2:
            if part_calo != 500:
                return 0
            else:
                return part_capa * part_dura * part_flav * part_text

def add_to_recipe(recipe, new_part):
    new_recipe = []
    part_found = False
    for part in recipe:
        if part[0] == new_part[0]:
            new_recipe.append([part[0], part[1] + new_part[1]])
            part_found = True
        else:
            new_recipe.append(part)
    
    if not part_found:
        new_recipe.append(new_part)
    
    return new_recipe

class ingredient:
    name = ""
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0