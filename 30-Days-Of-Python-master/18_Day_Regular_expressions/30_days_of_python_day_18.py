import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

iterator = 0

splitted = paragraph.split(' ')
print(splitted)

for element in splitted:
    element = re.findall(splitted[iterator], paragraph)
    print(f'({len(element)}, {element})')
    iterator += 1


points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']

int_points = []
for element in points:
    inted = int(element)
    int_points.append(inted)

int_points.sort()

print((len(int_points) -1) - int_points[0])

pattern = r'\d'
pattern2 = "-"
is_valid_variable = input("enter a variable name")
match = re.match(pattern, is_valid_variable)
match2 = re.findall(pattern2, is_valid_variable)

if (match) or (match2):
    print("is not a valid variable")


sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(text):

    text = re.sub(r'\s', 'Resserved_space_for_whiteline', text)
    print(text)
    text = re.sub(r'[\W^\s]', '', text)

    print(text)

    # counter = 0
    # length = len(text) -1

    # for element in text:    
    #     if (counter <= length) and (element[counter] == ("%" or "$" or "&")):
    #         element = ''

    # print(text)

    # print(text)

clean_text(sentence)

