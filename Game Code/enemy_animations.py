import os

def attack(name):
    #print(f"Animating attack for: {name}")debug
    file_path = os.path.join(name, "Attack.txt")
    try:
        with open(file_path, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File not found: {file_path}")


def damage1(name):

    #print(f"Animating attack for: {name}")debug
    file_path = os.path.join(name, "damage.txt")  
    try:
        with open(file_path, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File not found: {file_path}")


def nutral(name):

    #print(f"Animating attack for: {name}") debug
    file_path = os.path.join(name, "nutral.txt")  
    try:
        with open(file_path, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File not found: {file_path}")