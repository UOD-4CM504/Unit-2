import pytest
from io import StringIO
import sys
import subprocess

def test_exercise_1_output():
    # Run the student's script and capture its output
    result = subprocess.run(['python', 'L1_Exercise.py'], capture_output=True, text=True)
    output = result.stdout.strip()

    # Expected output
    expected_output = (
        "The circle with radius = 6 has circumference = 37.68\n"
        "The circle with radius = 15 has circumference = 94.2"
    )

    # Assert that the output matches the expected output
    assert output == expected_output, f"Expected:\n{expected_output}\n\nGot:\n{output}"

# To run this test, save it as test_exercise_1.py and run: pytest test_exercise_1.py