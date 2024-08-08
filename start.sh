#!/bin/bash

# Start the Flask app in the background
gunicorn app:fcm &

# Start the Streamlit app
streamlit run main.py --server.port=$PORT2
