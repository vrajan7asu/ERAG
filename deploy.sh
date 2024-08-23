#!/bin/bash

# Kill any running Streamlit processes
pkill -f streamlit

# Start the Streamlit app in the background
nohup streamlit run app.py > streamlit.log 2>&1 &

echo "Streamlit app deployed and running on localhost:8501"