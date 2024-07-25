import pytest
import subprocess
import sys
import re

@pytest.mark.parametrize("num1,num2,expected_result", [
    ("2.1", "3", "6.3"),
    ("5.2", "3.4", "17.68"),
    ("10", "0.5", "5.0"),
    ("0", "100", "0.0")
])
def test_multiplication_calculator(num1, num2, expected_result):
    # Run the student's script as a subprocess
    process = subprocess.Popen(
        [sys.executable, 'L5_Exercise.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Provide input to the script
    stdout, stderr = process.communicate(input=f"{num1}\n{num2}\n")

    # Check if there were any errors
    assert not stderr, f"Error occurred: {stderr}"

    # Get the last line of output (ignoring the input prompts)
    result = stdout.strip().split('\n')[-1]

    # Extract the calculated result using regex
    match = re.search(r'is ([\d.]+)$', result)
    assert match, f"Output format is incorrect: {result}"
    calculated_result = match.group(1)

    # Check if the output format is correct
    expected_format = f"The result of multiplying {float(num1)} by {float(num2)} is"
    assert result.startswith(expected_format), f"Expected output to start with '{expected_format}', but got '{result}'"

    # Check if the calculation is accurate (allowing for small floating-point differences)
    assert abs(float(calculated_result) - float(expected_result)) < 1e-9, \
        f"Expected result close to {expected_result}, but got {calculated_result}"

# To run this test, save it as L5_test.py and run: pytest L5_test.py