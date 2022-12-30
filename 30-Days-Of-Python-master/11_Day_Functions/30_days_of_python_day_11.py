from statistics import mode


def add_two_numbers(parameter1 = 0, parameter2 = 0):
    return parameter1 + parameter2

print(add_two_numbers(parameter2 = 34, parameter1 = 32441))


def area_of_the_circle(r = 0):
    return 3.141519 * r * r

print(area_of_the_circle(3235))


def add_all_nums(*args):
    total = 0
    for number in args:
        total = total + number        
    print(total)

add_all_nums(1, 3)


def celsius_to_farenheit(argument):
    return (argument*9/5) + 32

print(celsius_to_farenheit(100))


def check_season(month):
    if month == 1:
        print("winter")
    if month == 2:
        print("winter")
    if month == 3:
        print("spring")
    if month == 4:
        print("spring")  
    if month == 5:
        print("spring") 
    if month == 6:
        print("spring")  
    if month == 7:
        print("summer")
    if month == 8:
        print("summer")
    if month == 9:
        print("summer") 
    if month == 10:
        print("Autumn")
    if month == 11:
        print("Autumn")
    if month == 12:
        print("winter")

check_season(5)


def print_list(list):
    for element in list:
        print(element)

list_y = ["google", "apple", "amazon", "microsoft", "tesla", "toyota", "twitter"]

print_list(list_y)


def reversed_list(list):
    reverse_list = []
    i = (len(list) -1)
    
    while i >= 0:
            reverse_list.append(list[i])
            i -= 1
    print(reverse_list)



print(reversed_list(list_y))


def capitalize_list_items(list):
    i = len(list) -1
    while i >= 0:
        print(list[i].capitalize())
        i-=1

capitalize_list_items(list_y)


def add_item(list, item):
    list.append(item)
    print(list)

add_item(list_y, "qualcomm")


def remove_item(list, item):
    list.remove(item)
    print(list)

remove_item(list_y, "toyota")


def sum_of_numbers(number):
    number +=1
    total = 0
    for count in range(number):
        total = total + count
    print(total)
sum_of_numbers(5)


def sum_of_odds(number):
    total = 0
    number +=1
    range(number)
    
    for index in range(number):
        if index % 2 != 0:
            total = total + index
    print(total)

sum_of_odds(10)


def sum_of_evens(number):
    number +=1
    total = 0
    for i in range(number):
        if i % 2 == 0:
            total = total + i
    print(total)

sum_of_evens(10)


def evnen_and_odds(number):
    number +=1
    odds = 0
    evens = 0
    for index in range(number):
        if index % 2 == 0:
            evens+=1
        if index % 2 != 0:
            odds+=1
        
    print("The sum of odds are %s \nThe sum of evens are %d " %(odds, evens))

evnen_and_odds(100)


def factorial(number):
    number +=1
    total = 1
    for index in range(number):
        if index == 0:
            continue
        total = total * index
    print(total)

factorial(5)


def is_empty(parameter = False):
    if parameter: print("is not empty")
    else: print ("is empty")

is_empty()


list_of_numbers = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]

def mean(list):
    total = 0
    for number in list:
        total = total + number
    print(f'The mean is {total/2}')

mean(list_of_numbers)


def calculate_median(list):
    count = len(list) -1
    if count % 2 != 0.0:
        print(f'This list has 2 median items, the first one is: {list[int(count/2)]}, and the second one is {list[int((count/2) + 1)]}')
    else:
        print(f'The median item is: {list[int(count/2)]}')

calculate_median(list_of_numbers)


def calculate_mode(list):
    print(mode(list))

calculate_mode(list_of_numbers)


def calculate_mode_explicit(list):
    count = 0
    num = list[0]

    for element in list:
        freq = list.count(element)
        if (freq > num):
            count = freq
            num = element
    print(num)

calculate_mode_explicit(list_of_numbers)


def calcluate_range(list):
    highest_val = max(list)
    lowest_val = min(list)
    print(highest_val - lowest_val)

calcluate_range(list_of_numbers)


def is_prime(number):
    if number % 2 != 0:
        print(f'{number} is prime')
    else:
        print(f'{number} is not prime')

is_prime(4)



def item_repetition(list):
    tupule_of_repeated_items = []

    for element in list:
        if list.count(element) >= 2:
            tupule_of_repeated_items.append(element)
        else:
            print(f'This item is not repeated {element}')

    tuple(tupule_of_repeated_items)

    for repeated_element in tupule_of_repeated_items:
        print(f'This element was repeaetd {repeated_element}')


item_repetition(list_of_numbers)

def check_data_type(list):
    data_types = []
    for item in list:
        data_types.append(type(item))

    length = data_types[0]

    for element in data_types:
        if element != length:
            print(f'This ')
        else:
            print(f'This eleemnt is the same data type {element}')

check_data_type(list_of_numbers)


def valid_variable(variable):
    elements_of_variable = []
    for element in variable:
        elements_of_variable.append(element)

    if elements_of_variable.__contains__("-"):
        print("This is not a valid variable")
    else:
        print("This is a valid variable")

valid_variable("variable")

def most_spoken_languages(list):
    return 0

