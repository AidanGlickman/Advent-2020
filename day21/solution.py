def readFoods(inpath="input.txt"):
    with open(inpath, "r") as infile:
        foodStrs = infile.read().splitlines()
        foods = []
        for line in foodStrs:
            tokens = line.split(" (contains ")
            ingredients = set(tokens[0].split())
            allergens = set(tokens[1][:-1].split(", "))
            foods.append((ingredients, allergens))
        return foods


def part1(foods):
    foodCount = {}
    possible = {}
    for ingredients, allergens in foods:
        for ingredient in ingredients:
            if ingredient not in foodCount.keys():
                foodCount[ingredient] = 1
            else:
                foodCount[ingredient] += 1

        for allergen in allergens:
            if allergen not in possible:
                possible[allergen] = ingredients.copy()
            else:
                possible[allergen] &= ingredients

    allergic = set()
    for ingAllergens in possible.values():
        allergic.update(ingAllergens)

    return sum(foodCount[ing] for ing in (foodCount.keys() - allergic))


def part2(foods):
    possible = {}
    for ingredients, allergens in foods:
        for allergen in allergens:
            if allergen not in possible:
                possible[allergen] = ingredients.copy()
            else:
                possible[allergen] &= ingredients

    found = set()
    allergenMap = []
    while len(allergenMap) < len(possible.keys()):
        for allergen, ingredients in possible.items():
            if len(ingredients - found) == 1:
                ing = min(ingredients - found)
                allergenMap.append((allergen, ing))
                found.add(ing)
                break

    return ",".join(x[1] for x in sorted(allergenMap))


def main():
    foods = readFoods()
    print(f"Part 1: {part1(foods)}\nPart 2: {part2(foods)}")


main()
