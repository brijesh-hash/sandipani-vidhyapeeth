#!/bin/bash

# Simple script to start a local web server for the school website

echo "Starting local web server for School Website..."
echo "========================================"
echo ""
echo "The website will be available at:"
echo "http://localhost:8000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start Python's built-in HTTP server
python3 -m http.server 8000
