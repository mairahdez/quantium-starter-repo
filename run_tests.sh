#!/bin/bash

source venv/Scripts/activate

echo "Running the test suite..."
pytest -v test_app.py

if [ $? -eq 0 ]; then
    echo "All tests passed successfully!"
    exit 0
else
    echo "Error: The tests failed."
    exit 1
fi