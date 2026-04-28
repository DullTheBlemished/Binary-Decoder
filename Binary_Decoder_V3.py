"""
Binary Translator Module

This module turns text or numbers into binary code and back again. 
Use the format: [E/D][str/int][Data] (e.g., "EstrHi" or "Dint01001000").

Main Features:
- GetInput(input): Cleans the text and checks for formatting errors.
- GetAnswer(action, type, input): Performs the actual binary conversion logic.
- QuickRun(): Opens an interactive prompt to test the code instantly.

Custom Errors:
- InvalidInputError: Raised if the binary data is broken or incorrect.
- NoTypeError: Raised if 'E', 'D', 'str', or 'int' are missing.

Disclaimer:
- ngl this is about as reliable as my chatbot (which is a 0/10 reliability).
                                                        -(Dull the Blemished)
"""

import os
import time

class InvalidInputError(Exception):
    pass

class NoTypeError(Exception):
    pass

err_int = [2, 3, 4, 5, 6, 7, 8, 9]

def GetInput(input):
    """
    Cleans input, raises InvalidInputError or NoTypeError depending on the error.
    Returns: tuple (str, str, str) containing action ('encode'/'decode'), type ('str'/'int'), 
    and the cleaned data string.

    Format: [Action][Type][Data]
    Action: D (Decode) or E (Encode)
    Type:   str or int
    
    Example: 'Dstr01000100011101010110110001101100001000000111010001101000011001010
    0100000010000100110110001100101011011010110100101110011011010000110010101100100'

    Raises: NoTypeError: if input does not specify action/type (D/E and int/str).
    InvalidInputError: if input is not in 8-byte-sets format
    """
    input = input.replace(" ", "")
    input_action = 0
    input_type = 0

    
    if "E" in input:
        input_action = "encode"
    elif "D" in input:
        input_action = "decode"
    else:
        raise NoTypeError

    if "str" in input:
        input_type = "str"

    elif "int" in input:
        input_type = "int"

    else:
        raise NoTypeError

    input = input[4:]

    for err in err_int:
        if str(err) in input:
            raise InvalidInputError
        
    try:
        int(input)

    except:
        if input_action != "encode":
            raise InvalidInputError
        
    if len(input) % 8 != 0 and input_type != "str":
        raise InvalidInputError
    
    return(input_action, input_type, input)

def GetAnswer(action, type, input):
    """requires 3 arguements which GetInput() returns (refer to docstring of GetInput() for more) returns a string"""
    # ----------DECODE LOGIC----------
    if action == "decode":
        # -----for int-----
        if type == "int":
            value = 0
            while len(input) > 0:
                temp_value = []
                for i in range(8):
                    temp_value.append(input[0])
                    input = input[1:]
                
                for index, bit in enumerate(temp_value):
                    if bit == "1":
                        value += 2 ** (7 - index)
            return(value)
        # -----------------
        # -----for str-----
        elif type == "str":
            temp_value2 = []
            while len(input) > 0:
                value = 0
                temp_value = []
                for i in range(8):
                    temp_value.append(input[0])
                    input = input[1:]
                
                for index, bit in enumerate(temp_value):
                    if bit == "1":
                        value += 2 ** (7 - index)
                temp_value2.append(chr(value))
            value = "".join(temp_value2)
            return(value)
        # -----------------
    # --------------------------------
    # ----------ENCODE LOGIC----------
    if action == "encode":
        temp_value = []
        value = 0
        if type == "int":
        # -----for int-----
            return(f"{int(input) % 256:08b}")
        # -----------------
        # -----for str-----
        elif type == "str":
            input = list(input)
            for word in input:
                temp_value.append(f"{ord(word) % 256:08b}")
            value = "".join(temp_value)
            return(value)
        # -----------------
        # --------------------------------

def QuickRun():
    """This is for a quick run of the program, gets user_input and runs it through GetInput()"""
    user_input = input(">>>:")
    try:
        input_action, input_type, input1 = GetInput(user_input)
    except InvalidInputError:
        print("Invalid Input!")
    except NoTypeError:
        print("No Type Defined!")

    print(GetAnswer(input_action, input_type, input1))