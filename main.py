import json
import random


def get_names():
    with open('names.json', 'r') as fh:
        content = fh.read()
        names = json.loads(content)

    return names


def random_person(names, multiple):
    iterations = 1
    people = []

    if multiple:
        iterations = int(input('How many people? \n'))

    for i in range(iterations):
        person = {}
        gender = random.choice(['male', 'female'])
        person['gender'] = gender
        if gender == 'male':
            person['name'] = random.choice(names['male_names'])
            person['surname'] = random.choice(names['male_surnames'])
        else:
            person['name'] = random.choice(names['female_names'])
            person['surname'] = random.choice(names['female_surnames'])

        people.append(person)
        print(people)

    return people


def custom_person():
    pass

def pesel_gen():
    pesel = ''
    date_of_birth = input('year of birth(YYYY-MM-DD): ')
    gender = input('gender(F/M): ')
    date_of_birth = date_of_birth.split('-')
    print(date_of_birth)


def menu():
    while (True):
        action = input('choose action: \n'
                       '1. random person \n'
                       '2. multiple random people \n'
                       '3. custom person \n'
                       '4. stop \n')

        if action == '1':
            random_person(get_names(), False)
        elif action == '2':
            random_person(get_names(), True)
        elif action == '3':
            custom_person()
        elif action == '5':
            pesel_gen()
        else:
            print('invalid')


if __name__ == '__main__':
    menu()
