import webbrowser
import requests
import statistics
import numpy
import re
import bs4

# elements = requests.get('http://www.gutenberg.org/files/1112/1112.txt').text

# splitted_elements = elements.split()

# elements_set = set()
# elements_list = []
# for element in splitted_elements:
#     elements_set.add(element)
#     elements_list.append(element)

# words = []
# for word in elements_set:
#     words.append([elements_list.count(word), word])

# words.sort(reverse=True)

# print(words[:10])


# api = requests.get('https://api.thecatapi.com/v1/breeds')

# api = api.json()

# imperial_weights = []

# [imperial_weights.append(words['weight']['metric']) for words in api]

# weights_imperial = []
# for elements in imperial_weights:
#     for element in elements:
#         print(element)
#         try:
#             int(element)
#             weights_imperial.append(int(element))
#         except:
#             print(f'this: {element}, wasn\'t a number')   

# print(statistics.median(weights_imperial), min(weights_imperial), max(weights_imperial), numpy.std(weights_imperial), statistics.median(weights_imperial), print(statistics.mean(weights_imperial)))


# api = requests.get('https://api.thecatapi.com/v1/breeds')

# api = api.json()

# lifespan = []
# for items in api:
#     print(items)
#     lifespan.append(items['life_span'])

# re_pattern = r'\D'
# counter = 0
# lifespan_cleared = []
# for items in lifespan:
#     item = re.split(re_pattern, items)
#     lifespan_cleared.append(item)

# print(lifespan_cleared)


# final_lifespan = []

# for element in lifespan_cleared:
#     for items in element:
#         try:
#             final_lifespan.append(int(items))
#         except:
#             print()

# print(min(final_lifespan))

# print(max(final_lifespan))

# print(statistics.mean(final_lifespan))

# print(numpy.std(final_lifespan))


# api = requests.get('https://api.thecatapi.com/v1/breeds')

# api = api.json()

# origin_list = []
# origin_set = set()
# name_list = []

# for elements in api:
#     origin_list.append(elements['origin'])
#     origin_set.add(elements['origin'])
#     name_list.append([elements['origin'], elements['name']])

# final_list = []
# [final_list.append([origin_list.count(country), country]) for country in origin_set]


# real_final_list = []
# for element in final_list:
#     counter = 0
#     while counter != (len(name_list) -1):

#         if element[1] == name_list[counter][0]:
#             real_final_list.append([element[0], name_list[counter]])
#             print([element[0], name_list[counter]])
#         counter += 1

# print(real_final_list)


