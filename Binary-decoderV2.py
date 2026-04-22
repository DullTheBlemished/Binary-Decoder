import os

def print_thingy():
    print("BINARY BASE-2 DECODER - VERSION 2")
    print("made by Hung")
    print("----------------------------------")
    print("TUTORIAL")
    print("this version has two 'modes', before you input your binary string, input either:")
    print("'INTEGER' for translating into integer")
    print("'STRING' for translating into letters") 
    print("----------------------------------")

def decode(type, input):
    value = 0
    temp_value = 0
    temp_value2 = 0
    temp_value3 = 0
    non_allowed_integers = ["2", "3",
                            "4", "5",
                            "6", "7",
                            "8", "9",
                            ]

    try:
        int(input)

    except:
        return("Invalid input! string is not of ONLY 0s and 1s!")
    
    for i in non_allowed_integers:
        if i in input:
            return("Invalid input! string is not of ONLY 0s and 1s!")
    
    if type == "undefined":
        return("Invalid input! No type given!")
    
    if len(input) % 8 != 0:
        return("Invalid input! len(input) % 8 != 0!")

    elif type == "integer":
        temp_value = []
        
        while len(input) > 0:
            temp_value = []
            for i in range(8):
                temp_value.append(input[0])
                input = input[1:]
            
            for index, bit in enumerate(temp_value):
                if bit == "1":
                    value += 2 ** (7 - index)

        return(value)

    elif type == "string":
        temp_value = []
        temp_value2 = 0
        temp_value3 = []

        while len(input) > 0:
            temp_value2 = 0
            temp_value3 = []
            for i in range(8):
                temp_value3.append(input[0])
                input = input[1:]
            
            for index, bit in enumerate(temp_value3):
                if bit == "1":
                    temp_value2 += 2 ** (7 - index)

            temp_value.append(chr(int(temp_value2)))

        value = "".join(temp_value)
        return(value)
    
user_input_type = "undefined"
thingy = [" ", "/", ".", ",", "-", "_"]
while True:
    os.system("cls")
    print_thingy()
    user_input = input("input string here:").lower()

    os.system("cls")

    for stuff in thingy:
        user_input = user_input.replace(stuff, "")

    if "integer" in user_input:
        user_input_type = "integer"
        user_input = user_input[7:]

    elif "string" in user_input:
        user_input_type = "string"
        user_input = user_input[6:]

    else:
        user_input_type = "undefined"

    print(decode(user_input_type, user_input))
    input("'ENTER' to continue")