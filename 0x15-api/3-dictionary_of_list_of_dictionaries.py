#!/usr/bin/python3
"""
my_script.py

This script demonstrates the requiards for a simple Python project.
It includes a function that prints a message from a predefined dictionary.

Functions:
- main(): The main function that retrieves and prints messages for all users.
"""

import os
import sys


def main():
    """
    Main function to print messages for all users.
    Retrieves messages using keys and prints them. Defaults to a
    fallback message if the key is not found.
    """
    messages = {
        "user1": "Hello, Alice!",
        "user2": "Hello, Bob!",
        "user3": "Hello, Charlie!"
    }

    users = ["user1", "user2", "user3", "user4"]

    for user in users:
        print(messages.get(user, f"No message found for {user}"))


if __name__ == "__main__":
    main()
