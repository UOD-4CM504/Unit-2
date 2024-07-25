import pytest
import subprocess
import sys

@pytest.mark.parametrize("base,height,expected_output", [
    ("5.4", "6.2", "The area of the rectangle with base = 5.4 and height = 6.2 is 33.48."),
    ("3", "4", "The area of the rectangle with base = 3.0 and height = 4.0 is 12.0.")
])
def test_rectangle_area(base, height, expected_output):
    # Run the student's script as a subprocess
    process = subprocess.Popen(
        [sys.executable, 'Exercise_2.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Provide input to the script
    stdout, stderr = process.communicate(input=f"{base}\n{height}\n")

    # Check if there were any errors
    assert not stderr, f"Error occurred: {stderr}"

    # Get the last line of output (ignoring the input prompts)
    result = stdout.strip().split('\n')[-1]

    # Check if the output matches the expected result
    assert result == expected_output, f"Expected '{expected_output}', but got '{result}'"
