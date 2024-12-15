# Simple Bot Chat V 2.0

![Chatbot Demo](samples/chatbot_demo.png)
![Chatbot Demo](samples/chatbot_demo.png)
![Chatbot Demo](samples/chatbot_demo.png)

## Overview
Simple Bot Chat V 2.0 is a beginner-friendly chatbot application built with Python and Streamlit. It provides a conversational interface with pre-defined menu options and free-text input capabilities. This project is ideal for those learning chatbot development and exploring interactive applications with Streamlit.

## Features
- **Interactive Chat Interface**: Users can interact with the bot via menu options or free-text input.
- **Pre-defined Menu Options**: Quick responses for common queries like greetings, business hours, services, and contact information.
- **Dynamic Free-text Responses**: Powered by the `SimpleChatBot` class for handling custom user queries.
- **Session Persistence**: Maintains chat history during the session.
- **Export Conversation**: Print the full chat history for logging or API integration.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/santhosh-anbazhagan/simple-bot-chat.git
   cd simple-bot-chat
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Launch the application in your browser by running the Streamlit app.
2. Use the menu to select predefined options or type a message in the chat input.
3. View the bot's responses in real-time.
4. Optionally, print the full conversation for review or integration with APIs.

## Project Structure
```
.
├── app.py                # Main application file
├── requirements.txt      # Python dependencies
├── responses.py          # Predefined bot responses and fallback messages
├── utils.py              # Utility functions (e.g., generating unique IDs)
├── samples/              # Sample images for documentation
├── README.md             # Project documentation
└── simplechatbot.py      # Chatbot logic implementation
```

## Sample Output

![Sample Chat Output](samples/chat_output.png)

## Contributions
Contributions are welcome! If you'd like to improve this project:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- **Streamlit**: For the interactive web app framework.
- **Streamlit Chat**: For the easy-to-use chat interface.
- **SimpleChatBot**: For the chatbot response logic.

## Contact
For questions or feedback, feel free to reach out:
- Email: santhoshanbazhagan1910@gmail.com
- GitHub: [santhosh-anbazhagan](https://github.com/santhosh-anbazhagan)

