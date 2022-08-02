def get_details(): # gets user name, height, favourite colour, and spirit animal
    name = input("Please eneter your name: ")
    height = int(input("please enter your height (cm): "))
    favourite_colour = input("please enter your favourite colour: ")
    spirit_animal = input("please tell me your spirit animal: ")

    tailored_message(name, height, favourite_colour, spirit_animal)

def tailored_message(name, height, colour, spirit_animal): # prints a tailored message encasing their name, height, colour, and spirit animal
    print(f"Hello {name}! You're really tall, being {height}cm. Wow you like the colour {colour} too?!")
    calculate_secret(spirit_animal)

def calculate_secret(spirit_animal): # prints the spirit animal's first & last letter and it's length
    print(spirit_animal[0] + spirit_animal[len(spirit_animal)-1], len(spirit_animal))

def starter(): # starts off the code
    get_details()

starter()