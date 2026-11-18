pasta = ("Pasta Arrabiata", "Italian", 20, "Medium")
burrito = ("Veg Burrito", "Mexican", 45, "Hard")
all_recipes = (pasta,burrito)
print("Recipe 1:", pasta)

print("Name:", pasta[0], "| Level:", pasta[-1])
print("Burrito time:", all_recipes[1][2])
print("Cuisine and minutes:", pasta[1:3])


print("Pasta card:")
for detail in pasta:
    print(" -", detail)


pasta_list = ["Tomato", "Garlic", "Olive Oil", "Chilli", "Pasta", "Garlic"]
burrito_items = {"rice", "oregano", "garlic", "onion", "tomato", "spices"}
pasta_items = set(pasta_list)
print("Pasta items:", len(pasta_items), sorted(pasta_items))


extra = input("Add one ingrediant to the pasta: ")
pasta_items.add(extra)
pasta_items.discard("chilli")
pasta_items.discard("basil")
print("Updated pasta items:", sorted(pasta_items))


every_item = pasta_items.union(burrito_items)
shared = pasta_items.intersection(burrito_items)
only_pasta = pasta_items.difference(burrito_items)
not_shared = pasta_items.symmetric_difference(burrito_items)
print('Every item:', sorted(every_item))
print("Shared:", sorted(shared))
print("Only pasta:", sorted(only_pasta))
print("Not Shared:", sorted(not_shared))