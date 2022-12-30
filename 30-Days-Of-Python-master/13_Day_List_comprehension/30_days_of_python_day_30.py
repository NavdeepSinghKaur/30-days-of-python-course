numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

print([number for number in numbers if number <= 0])


list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

print([number for list in list_of_lists for lists in list for number in lists])


print([(i, 1, i*1, i*i, i*i*i, i*i*i*i, i*i*i*i*i,) for i in range(11)])


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

print([[element[0].upper(), element[0][0:3].upper(), element[1].upper()] for list in countries for element in list])


print([ "{country: %s, city: %s}" %(element[0].upper(), element[1].upper()) for list in countries for element in list])


names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]


print([f'{name[0]} {name[1]} ' for list in names for name in list])


slope = lambda x1, x2, y1, y2: (y2-y1 / x2-x1)

print(slope(3, 3, 2, 2))


