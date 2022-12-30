empty_tuple = ()

empty_tuple = tuple()


name_of_bros = ("name1", "name2", "name3")

name_of_bros2 = ("name4", "name5", "name6")


siblings = name_of_bros + name_of_bros2


print(len(siblings))


members = list(siblings)

members.append("patron1")
members.append("patron2")


print(tuple(members))


# LVL 2


list(members)

members.pop(0)
members.pop(0)
members.pop(0)
members.pop(0)
members.pop(0)
members.pop(0)

print(members)


fruits = ("banana", "manngo")

vegetables = ("carrot", "tomato")

animal_products = ("milk", "eggs")

food_stuff_lt = list(fruits) + list(vegetables) + list(animal_products)


print(food_stuff_lt)

food_stuff_lt.pop()
food_stuff_lt.pop()
food_stuff_lt.pop()
food_stuff_lt.pop(0)
food_stuff_lt.pop(0)
food_stuff_lt.pop(0)

tuple(food_stuff_lt)

del food_stuff_lt


nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("Estonia" in nordic_countries)

print("Iceland" in nordic_countries)

