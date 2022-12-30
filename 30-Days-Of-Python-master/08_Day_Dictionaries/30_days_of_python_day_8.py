dog = dict()


dog["name"] = "value1"

dog["color"] = "binary0101"

dog["age"] = "value3"


student = {
    "name": "big_brother",
    "gender": "Male",
    "age": 974,
    'skills': ['noskill']
   }


print(len(student))


print(student.get('skills'))

print(type(student))


student["skills"].append("skill2")

print(student)


print(student.keys())


print(student.values())


print(student.items())


student.pop('age')


del student