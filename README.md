# chatbot_specified
smart chatbot gui with specialized information with topics you choose yourself.
------------------------------------------------------------------------------

# ChatbotApp

ChatbotApp is a multi-topic chatbot application developed using the Kivy framework, designed to provide specialized interactions across different subjects such as Math, History, Old Cars, and Geography.

## Features

- **Multiple Chatbots**: Select from various topics like Math, History, Old Cars, and Geography to interact with a specialized chatbot.
- **Interactive UI**: Features buttons to select topics, a text input for user queries, and a scrollable area to view chatbot responses.
- **Background Image**: Utilizes a full-screen background image for an engaging user experience.
- **Token Counting**: Monitors and displays the number of tokens used in each conversation, supporting models from GPT-3.5 Turbo to GPT-4.

## Installation:
---------------------

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Rasmusalbertsson/chatbot_specified.git
   cd chatbotapp
   
Install dependencies:
---------------------
pip install kivy tiktoken
Run the application:
python main.py

Usage:
---------------------
Starting the App: Run the application and the main window will open with buttons for each topic.
Interacting with Chatbots: Click on a topic button to activate the corresponding chatbot. Enter your questions in the text input area and press Enter to get responses.
Ending the Chat: Click the 'End Chat' button to terminate the current session.
Customization
Adding More Chatbots: Implement additional chatbot classes and add corresponding buttons to the UI to expand the app's topics.
Background and Styles: Modify the backround.png and button styles in the source code to customize the look and feel.

Dependencies:
---------------------
Python 3.6+
Kivy
tiktoken (for token counting functionality)
License
This project is licensed under the MIT License - see the LICENSE.md file for details.

Contributing:
----------------------
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.
