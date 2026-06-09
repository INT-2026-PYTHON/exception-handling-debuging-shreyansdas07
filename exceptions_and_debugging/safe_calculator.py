"""
## 1. Safe Calculator with try / except  *(Easy)*

=================================================
SAFE CALCULATOR
=================================================

Problem Statement:
Write a Python FUNCTION called `safe_divide`
that takes two values from the user and
performs a division, but never crashes the
program.

Handle the following error cases gracefully:
   - non-numeric input        -> ValueError
   - division by zero         -> ZeroDivisionError
   - any other unexpected bug -> generic Exception

The function must always return a TUPLE:
        (status, value_or_message)
   - status -> "ok" or "error"
   - value_or_message -> the result on success,
                         or an error string on
                         failure.

-------------------------------------------------
Debugging Skills to Practice:
- Read the FULL traceback. The last line of a
  traceback names the exception class — match
  it to your `except`.
- Use a temporary print(type(a), type(b))
  before the division to confirm the inputs.
- Insert breakpoint() and step through with
  the Python debugger (pdb) commands:
       n  -> next line
       s  -> step into
       p  -> print a variable
       q  -> quit

-------------------------------------------------
Input Example 1:
safe_divide("10", "2")

Output Example 1:
('ok', 5.0)
Calculation finished

-------------------------------------------------
Input Example 2:
safe_divide("10", "0")

Output Example 2:
('error', 'Cannot divide by zero')
Calculation finished

-------------------------------------------------
Input Example 3:
safe_divide("ten", "2")

Output Example 3:
('error', 'Inputs must be numbers')
Calculation finished
=================================================

"""
def safe_divide(numerator_str, denominator_str):
    try:
        numerator = float(numerator_str)
        denominator = float(denominator_str)
    except ValueError:
        return ("error", "Non-numeric input provided.")
    
    try:
        result = numerator / denominator
        return ("ok", result)
    except ZeroDivisionError:
        return ("error", "Division by zero is not allowed.")
    except Exception as e:
        return ("error", f"An unexpected error occurred: {e}")

print("-- - Testing safe_divide ---")

num1 = input("Enter the numerator for a valid division: ")
denom1 = input("Enter the denominator for a valid division: ")
result1 = safe_divide(num1, denom1)
print(f"Result of {num1} / {denom1}: {result1}")

num2 = input("Enter the numerator for division by zero: ")
denom2 = input("Enter the denominator for division by zero: ")
result2 = safe_divide(num2, denom2)
print(f"Result of {num2} / {denom2}: {result2}")

num3 = input("Enter non-numeric numerator: ")
denom3 = input("Enter a numeric denominator: ")
result3 = safe_divide(num3, denom3)
print(f"Result of {num3} / {denom3}: {result3}")

num4 = input("Enter a numeric numerator: ")
denom4 = input("Enter non-numeric denominator: ")
result4 = safe_divide(num4, denom4)
print(f"Result of {num4} / {denom4}: {result4}")

num5 = input("Enter the numerator: ")
denom5 = input("Enter the denominator: ")
result5 = safe_divide(num5, denom5)
print(f"Result of {num5} / {denom5}: {result5}")