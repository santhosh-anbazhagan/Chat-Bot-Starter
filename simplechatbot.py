import re
import random

from responses import patterns


class SimpleChatBot:
    def __init__(self):
        pass

    def respond(self, user_input):
        # Convert input to lowercase for case-insensitive matching
        user_input = user_input.lower().strip()

        # Check for matching patterns
        for pattern, responses in patterns.items():
            if re.search(pattern, user_input):
                return random.choice(responses)

        # If no pattern matches, return a fallback response
        return ""

    def chat(self):
        print("Chatbot: Hello! I'm a simple chatbot. Type 'bye' to exit.")

        while True:
            # Get user input
            user_input = input("You: ").strip()

            # Check for exit condition
            if user_input.lower() in ["bye", "goodbye", "exit"]:
                print("Chatbot: Goodbye!")
                break

        return user_input
