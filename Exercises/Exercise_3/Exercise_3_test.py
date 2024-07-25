import pytest
import subprocess
import sys
import re


@pytest.mark.parametrize("child,adult,senior,expected_total", [
    ("3", "4", "2", "71"),
    ("0", "1", "1", "18"),
    ("5", "0", "0", "25"),
    ("2", "2", "2", "46"),
])
def test_ticket_price_calculator(child, adult, senior, expected_total):
    # Run the student's script as a subprocess
    process = subprocess.Popen(
        [sys.executable, 'Exercise_3.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding='utf-8'  # Specify UTF-8 encoding
    )

    # Provide input to the script
    stdout, stderr = process.communicate(input=f"{child}\n{adult}\n{senior}\n")

    # Check if there were any errors
    assert not stderr, f"Error occurred: {stderr}"

    # Get the last line of output (ignoring the input prompts)
    result = stdout.strip().split('\n')[-1]

    # Use regex to extract the total price
    match = re.search(r'Total Price: .?(\d+)', result)
    assert match, f"Output format is incorrect: {result}"

    actual_total = match.group(1)

    # Check if the total price matches the expected result
    assert actual_total == expected_total, f"Expected total of '{expected_total}', but got '{actual_total}'"

    # Check if the output starts with "Total Price: " (allowing for potential encoding issues with £)
    assert result.startswith("Total Price:"), f"Output does not start with 'Total Price:': {result}"

# To run this test, save it as test_exercise_3.py and run: pytest test_exercise_3.py