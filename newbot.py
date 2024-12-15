import streamlit as st
from streamlit_chat import message
from simplechatbot import SimpleChatBot
from utils import get_current_time_millis as unique_id
import random
from responses import responses, menu_options, fallback_responses


# Function to display messages
def load_bot_history():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    else:
        for msg in st.session_state.messages:
            message(
                msg["content"],
                is_user=msg["role"] == "user",
                key=f"message_{msg['id']}",
            )


def bot_response_chat(bot_response):
    message(bot_response, is_user=False, key=f"bot_message_{unique_id()}")
    # Add bot response to chat history with its unique ID
    st.session_state.messages.append(
        {"role": "bot", "content": bot_response, "id": unique_id()}
    )


def handle_menu(selected_option):
    # Accept user input based on menu selection
    if selected_option != "Select an option":
        user_message = f"You selected: {selected_option}"
        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_message,
                "id": unique_id(),
            }
        )

        # Generate bot response based on the selected menu option
        if selected_option == "Greeting":
            bot_response = responses["hello"]
        elif selected_option == "Business Hours":
            bot_response = responses["hours"]
        elif selected_option == "Services":
            bot_response = responses["services"]
        elif selected_option == "Contact Us":
            bot_response = responses["contact"]
        else:
            bot_response = random.choice(fallback_responses)  # Fallback if no match

        # Send the bot response to chat and update history
        bot_response_chat(bot_response)


def user_chat(prompt):
    message(prompt, is_user=True, key=f"user_message_{unique_id()}")
    st.session_state.messages.append(
        {"role": "user", "content": prompt, "id": unique_id()}
    )

    # Get the bot's response using SimpleChatBot
    prompt_res = SimpleChatBot().respond(prompt)

    if prompt_res:
        bot_response_chat(prompt_res)
    else:
        bot_response_chat(random.choice(fallback_responses))


# Function to print the entire conversation for API service
def print_conversation():
    conversation_history = [
        {"role": msg["role"], "content": msg["content"]}
        for msg in st.session_state.messages
    ]
    return conversation_history


# Streamlit app title
st.title("Simple Bot Chat V 2.0")

# Initialize chat history if it doesn't exist
load_bot_history()

# Menu for selecting options
selected_option = st.selectbox("Choose an option:", ["Select an option"] + menu_options)

# Handle the selected menu option before accepting free text input
if selected_option != "Select an option":
    handle_menu(selected_option)

if st.button("Print Conversation"):
    conversation_data = print_conversation()
    # Display the conversation data in JSON format (for demonstration purposes)
    print(st.json(conversation_data))  # You can also log this or send it to an API

# Accept free text input for additional queries
if _prompt := st.chat_input("Say something"):
    user_chat(_prompt)
