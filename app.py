from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
import socketio
import time

# Create a Flask application
app = Flask(__name__)
socketio_app = SocketIO(app)

# Create a socket.IO client
sio = socketio.Client()

# Initialize a variable to hold the last bot response
last_bot_response = None

# Event handler when connected to the Rasa server
@sio.event
def connect():
    print("Connected to Rasa server.")

# Event handler for bot's response (bot_uttered event)
@sio.on('bot_uttered')
def handle_bot_message(data):
    global last_bot_response
    last_bot_response = data['text']  # Store the last bot response
    print(data['text'] )

# Event handler when disconnected from the Rasa server
@sio.event
def disconnect():
    print("Disconnected from Rasa server.")

# Event handler for connection failure
@sio.event
def connect_error(data):
    print("Failed to connect to the server.")

# Connect to the Rasa Socket.IO server
try:
    sio.connect('http://localhost:5004')
except socketio.exceptions.ConnectionError as e:
    print(f"Connection failed: {e}")

# Function to send a message to the Rasa bot 
def send_message(message):
    print(message)
    sio.emit('user_uttered', {
        'message': message,
        'sender': 'user'
    })

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message_endpoint():
    user_message = request.json.get('message')  # Get the message from the request
    if user_message:
        send_message(user_message)  # Send the message to Rasa bot
        # Wait for a response (this is a blocking call, may need adjustment for production)
        time.sleep(1)  # Adjust as necessary based on response time
        return jsonify({'response': last_bot_response})  # Return the last bot response
    else:
        return jsonify({'error': 'No message provided'}), 400

# Start the Flask app
if __name__ == '__main__':
    socketio_app.run(app)
