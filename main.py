import json
import random

def get_names():
    with open('names.json', 'r') as fh:
        content = fh.read()
        names = json.loads(content)
        return names

def random_person(names):
    gender = random.choice(['male', 'female'])



def mult_people():
    pass

def custom_person():
    pass



def menu():
    while(True):
        action = input('choose action: \n'
                       '1. random person \n'
                       '2. multiple random people \n'
                       '3. custom person \n'
                       '4. stop \n')

        if action == '1':
            random_person(get_names)
        if action == '2':
            custom_person()
        if action == '3':
            custom_person()
        if action == '4':
            break
        else:
            print('invalid')

if __name__ == '__main__':
    menu()
