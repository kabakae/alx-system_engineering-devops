#!/usr/bin/python3
"""
my_script.py

This script demonstrates the required coding standards for a simple Python
It includes a function that prints a message from a predefined dictionary.

Functions:
- main(): The main function that retrieves and prints a message.
"""

import os
import sys


def main():
    """
    Main function to print a message from a dictionary.
    Retrieves a message using a key and prints it. Defaults to a
    fallback message if the key is not found.
    """
    messages = {
        "greeting": "Hello, World!",
        "farewell": "Goodbye, World!"
    }

    message_key = "greeting"
    print(messages.get(message_key, "No message found"))


if __name__ == "__main__":
    main()
