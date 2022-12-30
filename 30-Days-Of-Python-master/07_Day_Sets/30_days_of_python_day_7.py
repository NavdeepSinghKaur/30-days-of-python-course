

x = (1 << 53) +1

print(x + 1.0)

it_companies = {'Meta', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add('Twitter')

it_companies.update(['OpenAi', 'AMD', 'Nvidia', 'Intel'])

it_companies.pop()

#The only difference between discard() and remove() methods, is that if you give an item that is not found in the set the methos willi rise an error, and the discard() methos it won't rise any error.

A.update(B)


A.intersection(B)


A.issubset(B)


A.isdisjoint(B)


B.intersection(A)


A.symmetric_difference(B)


del A, B


ages = set()


# Sting: is mutable tuple: is immutable set: is mutable, any element can be repeated 2 or more times


text = "I am a teacher and I love to inspire and teach people."

text2 = text.split()

text3 = set(text2)

print(text3)

print("XD")
