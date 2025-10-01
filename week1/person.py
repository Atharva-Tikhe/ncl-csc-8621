#!/usr/bin/python3
##
## Calculate some values for a person
##
## Author: Jennifer Warrender

def format(person):
    return f'Name:\t {person["name"]}\n Height:\t {person["height"]}m\n Weight:\t {person["weight"]} kg'
    return "Name:\t" + person['name'] + '\n' + 'Height:\t' + person['height'] + ' m' + '\n' + 'Weight:\t' + person['weight'] + ' kg'

def display(person):
    print(format(person))

## Add height and weight to the person
person = {'name': 'Harry Potter', 'height': 0, 'weight': 0}

def create_person(name, height, weight):
    return {'name': name, 'height': height, 'weight': weight}

person2 = create_person('Harry Potter', '1.2', '45')
# display(person2)