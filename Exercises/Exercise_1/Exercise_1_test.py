import pytest
import subprocess
import sys
import re


@pytest.mark.parametrize("celsius_input,expected_fahrenheit", [
    ("20.2", "68.36"),
    ("0", "32.0")
])
def test_temperature_conversion(celsius_input, expected_fahrenheit):
    # Run the student's script as a subprocess
    process = subprocess.Popen(
        [sys.executable, 'Exercise_1.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Provide input to the script
    stdout, stderr = process.communicate(input=celsius_input)

    # Check if there were any errors
    assert not stderr, f"Error occurred: {stderr}"

    # Get the last line of output (ignoring the input prompt)
    result = stdout.strip().split('\n')[-1]

    # Use regex to extract the Celsius and Fahrenheit values
    match = re.search(r'([-\d.]+)\s*Celsius is equivalent to\s*([-\d.]+)\s*Fahrenheit', result)
    assert match, f"Output format is incorrect: {result}"

    celsius_output, fahrenheit_output = match.groups()

    # Check if the Celsius output is equivalent to the input
    assert float(celsius_output) == float(
        celsius_input), f"Input Celsius {celsius_input} does not match output {celsius_output}"

    # Check if the Fahrenheit output matches the expected value
    assert fahrenheit_output == expected_fahrenheit, f"Expected Fahrenheit {expected_fahrenheit}, but got {fahrenheit_output}"