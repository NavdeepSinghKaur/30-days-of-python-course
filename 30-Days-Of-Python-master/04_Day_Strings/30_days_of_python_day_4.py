
from http.client import UNSUPPORTED_MEDIA_TYPE


sub_string1 = "Thirty";

sub_string2 = "Days";

sub_string3 = "Of";

sub_string4 = "Python";

string1 = f'{sub_string1} {sub_string2} {sub_string3} {sub_string4}'

print(string1)


sub_string1 = "Coding"

sub_string2 = "For"

sub_string3 = "All"

string2 = "{} {} {}".format(sub_string1, sub_string2, sub_string3)

print(string2)

company = string2

print(company)


print(len(company))


print(company.upper())


print(company.lower())


print(string2.capitalize())


print(string2.title())


print(string2.swapcase())


print("coding for all".capitalize())


print("coing for all".title())


print("coding for all".swapcase())


print("Coding For All".replace("Coding ", ""))


print("Coding For All".__contains__("Coding"))


print("Coding For All".replace("Coding", "python"))


print("Python For Everyone".replace("Everyone", "All"))


print("Coding For All".split())


print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", "))


print("Coding For All"[0])


print("Coding For All".rindex("l"))


print("Coding For All"[10])


PFE = "Python For Everyone"

print(PFE)


CFA = "Coding For All"

print(CFA)


print("Coding For All".index("C"))


print("Coding For All".index("F"))


print("Coding For All People".rindex("l"))


print("You cannot end a sentence with because because because is a conjunction".find("because"))


print("You cannot end a sentence with because because because is a conjunction".rindex("because"))


var1 = 'You cannot end a sentence with because because because is a conjunction'

sliced_because = var1[30:54]

print(sliced_because)


print("Coding For All".startswith("Coding"))


print("Coding For All".endswith("coding"))


print('   Coding For All      '.strip(" "))


print("30DaysOfPython".isidentifier())

print("thirty_days_of_python".isidentifier())


libraries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]

joined_libraries = ", ".join(libraries)

print(joined_libraries)


print("I am enjoying this challenge. \n I just wonder what is next.")


print("Name \t\t Age \t Country \t City\nAsabench\t 250\t Finland\t Helsinki")


radius = 10

area = 3.14*radius**2

print("The area of a circle with radius {} is {} meters square.".format(radius, area))

eight = 8

six = 6

print(f'{eight} + {six} = {eight + six}')

print(f'{eight} - {six} = {eight - six}')

print(f'{eight} * {six} = {eight*six}')

print(f'{eight} / {six} = {eight/six}')

print(f'{eight} % {six} = {eight}')

print(f'{eight} // {six} = {eight // six}')

print(f'{eight} ** {six} = {eight ** six}')