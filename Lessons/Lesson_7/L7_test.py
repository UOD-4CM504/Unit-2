import pytest
import subprocess
import sys

@pytest.mark.parametrize("firstname,surname,expected_outputs", [
    (
        "John",
        "Doe",
        [
            "The first character of the first name is J",
            "The last character of the surname is e",
            "The person's initials are J.D",
            "The first 3 characters of the first name are Joh",
            "The last 4 characters of the surname are Doe"
        ]
    ),
    (
        "Alice",
        "Smith",
        [
            "The first character of the first name is A",
            "The last character of the surname is h",
            "The person's initials are A.S",
            "The first 3 characters of the first name are Ali",
            "The last 4 characters of the surname are mith"
        ]
    )
])
def test_string_manipulation(firstname, surname, expected_outputs):
    # Run the student's script as a subprocess
    process = subprocess.Popen(
        [sys.executable, 'L7_Exercise.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Provide input to the script
    stdout, stderr = process.communicate(input=f"{firstname}\n{surname}\n")

    # Check if there were any errors
    assert not stderr, f"Error occurred: {stderr}"

    # Split the output into lines
    output_lines = stdout.strip().split('\n')

    # Check the outputs
    for i, expected in enumerate(expected_outputs):
        assert output_lines[i+2] == expected, f"Expected '{expected}', but got '{output_lines[i+2]}'"

# To run this test, save it as L6_test.py and run: pytest L6_test.py