import random
import string


def random_user_id():
    print(f'{random.choice(string.ascii_letters)} {random.randint(0, 9)} {random.randint(0, 9)} {random.choice(string.ascii_lowercase)}')

random_user_id()


def user_id_gen_by_user(one, two = 0):
    one = one -1
    count = 0
    first_choice_list = []
    second_choice_list = []
    while count <= one:
        (first_choice_list.append(random.choice(string.hexdigits)))
        count+=1

    
    print(first_choice_list)

user_id_gen_by_user(5)

def user_id_gen(one, two):
    two_counter = 0
    one_counter = 0
    elements_list = []
    one_list = []
    copy_list = []
    while two_counter < two:
        while one_counter < one:
            one_list.append(random.choice(string.hexdigits))
            one_counter +=1
        copy_list = one_list.copy()
        print(copy_list)
        one_list.clear()
        copy_list.clear()
        one_counter = 0
        two_counter +=1
    print(elements_list)

user_id_gen(20, 3)


def random_rgb_spectrum():
    print(f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0,255)})')

random_rgb_spectrum()

def random_hexa_colors():
    e = 0
    i = 0
    list_of_hexdigits = []
    while e <= 2:
        i = 0
        if e != 0: list_of_hexdigits.append(",")
        while i <= 5:
            list_of_hexdigits.append(random.choice(string.hexdigits))
            i += 1
        e+=1

    print(*list_of_hexdigits)

random_hexa_colors()

def rgb_array():
    rgb_spectrum = 0
    array_of_rgb_spectrum = []

    while rgb_spectrum <= 255:
        array_of_rgb_spectrum.append(rgb_spectrum)
        rgb_spectrum += 1
        
    print(array_of_rgb_spectrum)

rgb_array()


def hex_array():
    hex_digits_array = []

    for element in string.hexdigits:
        hex_digits_array.append(element)

    print(hex_digits_array)

hex_array()


def hexa_or_rgb(number):
    choice = input('type 1 for HEX, or 2 for RGB: ')
    i = 1
    e = 0
    every_element = []

    if choice == str(1):

        while i <= number:
            while e <= 5:
                every_element.append(random.choice(string.hexdigits))
                e += 1
            i += 1
            e = 0

    if choice == str(2):

        while i <= number:
            while e <= 2:
                every_element.append(random.randint(0, 255))
                e += 1
            i += 1
            e = 0

    print(*every_element)

hexa_or_rgb(1)


def unique_numbers_0_9():
    counter = 0
    array_of_numbers = []
    iterator = 0

    while counter <= 7:
        array_of_numbers.append(random.randint(0,9))
        counter += 1
        
    length = len(array_of_numbers) -1
    
    while iterator <= length:

        element = array_of_numbers[iterator]
        variable = array_of_numbers.count(element)

        if variable >= 2:
            unique_numbers_0_9() 
            return 0

        iterator += 1
        
    print(array_of_numbers)

unique_numbers_0_9()