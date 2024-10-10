# Chatbot_Rasa Application

This is a simple chatbot application built using Flask and Rasa, which utilizes Socket.IO for real-time communication between the frontend and backend. The user interface resembles a chat interface similar to WhatsApp, complete with user and bot icons, message bubbles, and typing indicators.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [How It Works](#how-it-works)
- [License](#license)

## Features
- User-friendly chat interface
- Real-time messaging using Socket.IO
- Typing indicator for bot responses
- Easy setup and customization

## Installation

To set up the project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install required packages**:
   ```bash
   pip install flask flask-socketio python-socketio
   ```

4. **Run the Rasa server** (make sure you have Rasa installed and your model is trained):
   ```bash
   rasa run -m models --enable-api --cors "*" --debug
   ```

5. **Start the Flask application**:
   ```bash
   python app.py
   ```

6. **Open your web browser** and go to `http://127.0.0.1:5000` to see the chatbot in action.

## Usage

1. Type your message in the input box.
2. Click the "Send" button or press "Enter" to send the message.
3. The bot will respond in real-time with its reply.
4. You can see a typing indicator while the bot is processing your message.

## Code Structure

- `app.py`: The main Flask application file that handles routing, message processing, and connection to the Rasa server.
- `templates/index.html`: The HTML file for the frontend chat interface.
- `static/style.css`: The CSS file for styling the chat interface.
- `static/img/user.jpg`: User icon image.
- `static/img/bot.jpg`: Bot icon image.

## How It Works

1. **WebSocket Communication**: 
   - The application uses Flask-SocketIO to handle real-time communication with the Rasa chatbot. The `app.py` file establishes a connection with the Rasa server using Socket.IO.

2. **Sending Messages**:
   - When a user sends a message, it triggers the `send_message` function, which emits the message to the Rasa server using the `user_uttered` event.

3. **Receiving Responses**:
   - The bot's response is received via the `bot_uttered` event. The response is stored and returned to the user interface for display.

4. **User Interface**:
   - The frontend is created using HTML and CSS. The messages are styled to resemble a chat application, with different styles for user and bot messages.

5. **Typing Indicator**:
   - A simple animation of three dots simulates the bot typing, enhancing the user experience.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
```