import time
import os

def print_thingy():
    print("This Translator isnt really good btw, and also can only translate to integers")
    print("before going in, please remember that your input must NOT contain:")
    print("-spaces")
    print("-any character other then numbers")
    print("and lastly, make sure your input's length is divisible by 8, as that is the amount of switches in a byte")
    print("this is technically a low-leveled base-two decoder btw, and also, rememebr this transtale additively, such as, if your string returns 2 on the first byte (00000010) and two on the next, it will return four")
    print("-----------------------------------")

def decode(user_input):
    temp_userinput = []
    value = 0
    non_binary_numbers = ["2", "3", "4", "5",
                          "6", "7", "8", "9"]
    try:
        int(user_input)
    except:
        return("Invalid input! idk what you did tbh it might be a speacial character")

    if len(user_input) % 8 != 0:
        return("Invalid input!, whole string isnt made of singular bytes!")
    
    for non in non_binary_numbers:
        if non in user_input:
            return("Invalid input! Make sure string ONLY contains 1s and 0s, this is BASE-2!")
    
    while len(user_input) > 0:
        for i in range(8):
            temp_userinput.append(user_input[0])
            user_input = user_input[1:]

        if temp_userinput[0] == "1":
            value += 128
        if temp_userinput[1] == "1":
            value += 64
        if temp_userinput[2] == "1":
            value += 32
        if temp_userinput[3] == "1":
            value += 16
        if temp_userinput[4] == "1":
            value += 8
        if temp_userinput[5] == "1":
            value += 4
        if temp_userinput[6] == "1":
            value += 2
        if temp_userinput[7] == "1":
            value += 1

        temp_userinput = []

    return(value)

while True:
    os.system("cls")
    print_thingy()
    user_input_1 = input("Input string here:").replace(" ","")
    os.system("cls")
    print(decode(user_input_1))
    input("'ENTER' to continue")