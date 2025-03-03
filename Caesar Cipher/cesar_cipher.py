"""
Modules:
    os: This module is used to interact with operating system.

Utilizations:
    os.path.isfile(path): To check if path is an existing file.
"""

import os


def welcome():
    """
    Prints a welcome message for the Caesar Cipher.

    Parameters:
        None

    Returns:
        None
    """

    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")


def enter_message():
    """
    Prompts the user to either encrypt or decrypt a message or process a file.
    First calls `message_or_file()` to determine user's choices and filename if applicable.

    Parameters:
        None

    Returns:
        None
    """

    user_primary_choice, user_secondary_choice, user_file_name = message_or_file()
    if user_primary_choice == "e" and user_secondary_choice == "c":
        message = input("What message would you like to encrypt: ")
        shift = ask_shift()
        print(encrypt(message, shift))
    elif user_primary_choice == "d" and user_secondary_choice == "c":
        message = input("What message would you like to decrypt: ")
        shift = ask_shift()
        print(decrypt(message, shift))
    else:
        process_file(user_file_name, user_primary_choice)


def ask_shift():
    """
    Prompts the user to input a shift number.

    Parameters:
        None

    Returns:
        shift (int): Shift number provided by the user.
    """

    while True:
        shift = input("What is the shift number: ")
        if shift.isdigit():
            shift = int(shift)
            break
        else:
            print("Invalid Shift")
    return shift


def message_or_file():
    """
    Prompts the user to choose between encryption or decryption.
    Prompts the user whether to read from a file or the console.
    Asks for a filename if user wants to read from a file.

    Parameters:
        None

    Returns:
        user_primary_choice (str): 'e' for encryption or 'd' for decryption.
        user_secondary_choice (str): 'f' for file or 'c' for console.
        user_file_name (str or None): Filename if 'f' is chosen, otherwise None.
    """

    while True:
        user_primary_choice = input(
            "Would you like to encrypt (e) or decrypt (d): "
        ).lower()
        if user_primary_choice in ["e", "d"]:
            break
        else:
            print("Invalid Mode")
    while True:
        user_secondary_choice = input(
            "Would you like to read from a file (f) or the console (c): "
        ).lower()
        if user_secondary_choice in ["f", "c"]:
            break
        else:
            print("Invalid Mode")
    if user_secondary_choice == "f":
        while True:
            user_file_name = input("Enter a filename: ")
            if is_file(user_file_name):
                break
            else:
                print("Invalid Filename")
        return user_primary_choice, user_secondary_choice, user_file_name
    else:
        return user_primary_choice, user_secondary_choice, None


def is_file(user_file_name):
    """
    Checks if a given path is a file.

    Parameters:
        user_file_name (str): Path to the file.

    Returns:
        bool: True if the path is a file, False otherwise.
    """

    return os.path.isfile(user_file_name)


def process_file(user_file_name, user_primary_choice):
    """
    Processes a file to encrypt or decrypt its contents as per user's choice.

    Parameters:
        user_file_name (str): Name of the file to be processed.
        user_primary_choice (str): 'e' for encryption or 'd' for decryption.

    Returns:
        None
    """

    shift = ask_shift()
    message_list = []
    with open(user_file_name, "r", encoding="utf-8") as file:
        for line in file.readlines():
            message = line.strip()
            if user_primary_choice == "e":
                message_list.append(encrypt(message, shift))
            elif user_primary_choice == "d":
                message_list.append(decrypt(message, shift))
    write_messages(message_list)
    return message_list


def write_messages(message_list):
    """
    Writes a list of messages to a file named 'results.txt'.

    Parameters:
        message_list (list of str): A list of messages to be written to the file.

    Returns:
        None
    """

    with open("results.txt", "w", encoding="utf-8") as file:
        for message in message_list:
            file.write(message + "\n")
    print("Output written to results.txt")


def encrypt(message, shift):
    """
    Encrypts a message using the Caesar cipher technique.

    Parameters:
        message (str): The message to be encrypted.
        shift (int): The number of positions to shift each character in the message.

    Returns:
        encrypted_message (str): Encrypted message. Non-alphabetic characters remain unchanged.
    """

    encrypted_message = ""
    shift = shift % 26
    message = message.upper()
    for char in message:
        if char.isalpha():
            shifted_unicode = ord(char) + shift
            if shifted_unicode > ord("Z"):
                shifted_unicode -= 26
            encrypted_message += chr(shifted_unicode)
        else:
            encrypted_message += char
    return encrypted_message


def decrypt(message, shift):
    """
    Decrypts a message using the Caesar cipher technique.

    Parameters:
        message (str): The encrypted message to be decrypted.
        shift (int): The number of positions to shift each character in the message.

    Returns:
        decrypted_message (str): Decrypted message. Non-alphabetic characters remain unchanged.
    """

    decrypted_message = ""
    shift = shift % 26
    message = message.upper()
    for char in message:
        if char.isalpha():
            shifted_unicode = ord(char) - shift
            if shifted_unicode < ord("A"):
                shifted_unicode += 26
            decrypted_message += chr(shifted_unicode)
        else:
            decrypted_message += char
    return decrypted_message


def ask_again():
    """
    Continuously prompts the user to choose whether they want to encrypt or decrypt another message.

    Parameters:
        None

    Returns:
        None
    """

    while True:
        user_primary_choice = input(
            "Would you like to encrypt or decrypt another message? (y/n): "
        ).lower()
        if user_primary_choice == "y":
            enter_message()
        elif user_primary_choice == "n":
            print("Thanks for using the program, goodbye!")
            break


def main():
    """
    Main function that calls other functions for the complete program execution.
    """

    welcome()
    enter_message()
    ask_again()


if __name__ == "__main__":
    main()
