# Here is a practice scenario designed to use every concept we just covered (Variables, Types, Casting, f-Strings, and Math).
#
# The Scenario: Test Execution Reporter
# You need to write a Python script that stores raw data from a test run and generates a readable summary log for the console.
#
# Requirements:
#
# Create a file named test_summary.py.
#
# Define the following variables:
#
# test_name: A string (e.g., "Checkout_Payment_Flow").
#
# execution_time_sec: A float (e.g., 12.559).
#
# total_steps: An integer (e.g., 10).
#
# failed_steps: An integer (e.g., 2).
#
# is_critical: A boolean (e.g., True).
#
# Math & Casting: Calculate the passed_steps and pass_percentage.
#
# Hint: Percentage = (Passed / Total) * 100. Ensure the result is an int (no decimals) for the report.
#
# String Formatting: Print a summary using f-strings that looks exactly like this:
# Test: Checkout_Payment_Flow | Critical: True
# Result: 8/10 steps passed (80%)
# Time Taken: 12.56s

test_name="Checkout_Payment_Flow"
execution_time_sec=12.559
total_steps=10
failed_steps=2
is_critical=True
print(f"Test: Checkout_Payment_Flow | Critical: {is_critical}")
print(f"Step passed {total_steps-failed_steps}/{total_steps} and passed steps {int(((total_steps-failed_steps)/total_steps)*100)}")
print(f"Time taken {execution_time_sec}")




