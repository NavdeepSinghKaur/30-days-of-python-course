import json
import csv

speech = open('data/donald_speech.txt')

lines = speech.readlines()

counter = 0
for line in lines:
    counter += 1
print(counter)


obama_speech = open('data/obama_speech.txt')

lines = obama_speech.readlines()

counter = 0
for line in lines:
    counter += 1
print(counter)


michelle_speech = open('data/michelle_obama_speech.txt')

lines = michelle_speech.readlines()

counter = 0
for line in lines:
    counter += 1
print(counter)


melina_speech = open('data/melina_trump_speech.txt')

lines = melina_speech.readlines()

counter = 0

for line in lines:
    counter += 1
print(counter)


def most_spoken_language(filename, number):

    file = open(filename, encoding='utf8')

    countries_data = json.load(file)

    language_set = set()
    languages = list()
    for elements in countries_data:
        for element in elements['languages']:
            language_set.add(element)
            languages.append(element)

    def take_first(element): return element[0]
    top_ten_languages = []
    for element in language_set:
        counted_element = languages.count(element)
        top_ten_languages.append((counted_element, element))
    top_ten_languages.sort(key=take_first, reverse=True)
    
    print(top_ten_languages[:number])

most_spoken_language('data/countries_data.json', 10)


def most_populated_countries(filename, number):

    file = open(filename, encoding='utf8')

    countries_data = json.load(file)

    def value(key):
        return key[1]

    population_list = list()
    for elements in countries_data:
        population_list.append([elements['name'], elements['population']])
    population_list.sort(key=value, reverse=True)
    
    for element in population_list[:number]:
        print(f'country: {element[0]}, population: {element[1]}')

most_populated_countries('data/countries_data.json', 3)


with open('data/email_exchanges_big.txt') as email_adresses:
    email = email_adresses.read().split()

    adresses = []
    for line in email:
        if "@" in line:
            line.split()
            adresses.append(line)
        
    # print(adresses)

def find_most_common_words(file, number):

    words_list = []
    words_set = set()
    with open(file) as f:
        for word in f.read().split():
            words_list.append(word)
            words_set.add(word)
    
    counted_words = []
    for words in words_set:
        count = words_list.count(words)
        counted_words.append([count, words])
    counted_words.sort(reverse=True)
    print(counted_words[: number])

find_most_common_words('data/donald_speech.txt', 10)

find_most_common_words('data/obama_speech.txt', 10)

find_most_common_words('data/melina_trump_speech.txt', 10)

find_most_common_words('data/michelle_obama_speech.txt', 10)

find_most_common_words('data/romeo_and_juliet.txt', 10)


with open('data/hacker_news.csv') as f:
    reader = csv.reader(f, delimiter=',')

    python_line = 0
    javascript_line = 0
    java_line = 0

    for row in reader:
        for shit in row:
            if ('python' or 'Python') in shit:
                python_line += 1
            if ('JavaScript'or 'javascript') in shit:
                javascript_line += 1
            if ('java' or 'Java') in shit:
                java_line += 1
    print(python_line, javascript_line, java_line)