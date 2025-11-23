#!/bin/bash

# Ensure the script is run from the repository root
echo "Setting up the chat command..."

# Make the chat.py script executable
chmod +x src/finalversion/chat.py

# Create a symbolic link in /usr/local/bin (requires sudo)
echo "Creating a symbolic link to /usr/local/bin/chat..."
sudo ln -sf $(pwd)/src/finalversion/chat.py /usr/local/bin/chat

# Confirm setup
echo "Setup complete! You can now run the chat interface by typing 'chat' in your terminal."