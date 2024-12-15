# Predefined responses
responses = {
    "hello": "Hi there! How can I help you today?",
    "hours": "Our business hours are 9 AM to 5 PM, Monday through Friday.",
    "services": "We offer various services including web development, SEO, and marketing.",
    "contact": "You can contact us at contact@example.com.",
}

# Menu options
menu_options = [
    "Select an option",
    "Greeting",
    "Business Hours",
    "Services",
    "Contact Us",
]

patterns = {
    r"hi|hello|hey": [
        "Hello there!",
        "Hi! How are you?",
        "Greetings! Nice to meet you.",
    ],
    r"how are you": [
        "I'm doing well, thanks for asking!",
        "I'm great! How about you?",
        "Feeling good today!",
    ],
    r"what is your name": [
        "I'm a simple chatbot.",
        "You can call me ChatBot.",
        "I'm an AI assistant.",
    ],
    r"bye|goodbye": ["Goodbye!", "See you later!", "Have a great day!"],
}

fallback_responses = [
    "I'm not sure how to respond to that.",
    "Could you rephrase that?",
    "That's interesting, but I don't understand completely.",
    "Tell me more about that.",
]
