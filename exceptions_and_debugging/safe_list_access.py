"""
## 2. Safe List Access  *(Easy)*

=================================================
SAFE LIST ACCESS
=================================================

Problem Statement:
Write a Python FUNCTION called `safe_get`
that takes a list and an index, and returns
the value at that index WITHOUT crashing the
program when the index is invalid.

The function must return a TUPLE:
        (status, value_or_message)
   - status -> "ok" or "error"
   - value_or_message -> the value on success,
                         or an error string on
                         failure.

Handle these error cases:
   - IndexError      -> "Index out of range"
   - TypeError       -> "Index must be an int"
   - other Exception -> "Unexpected error: ..."

-------------------------------------------------
Instructions:
1. Define a function:
      def safe_get(items, index):
2. Use a try block that returns items[index].
3. Add a separate `except` block for each
   expected exception in the correct order
   (most specific first).
4. Add a final `except Exception as e:` block
   that includes str(e) in the error message.
5. Do NOT use:
   - the `in` operator to guess validity
     beforehand
   - if-checks like `if 0 <= index < len(items)`
     to AVOID the exception.
   The whole point is to LET the exception be
   raised and HANDLE it.

-------------------------------------------------
Debugging Skills to Practice:
- Use print(repr(index), type(index)) when the
  function misbehaves; `repr` shows quotes
  around strings so you can tell "3" from 3.
- Read the exception MESSAGE — IndexError on a
  list of length 5 tells you the index that
  was rejected.
- Try `import traceback; traceback.print_exc()`
  inside the except block to print the full
  traceback while still handling the error.

-------------------------------------------------
Input Example 1:
safe_get([10, 20, 30, 40], 2)

Output Example 1:
('ok', 30)

-------------------------------------------------
Input Example 2:
safe_get([10, 20, 30], 7)

Output Example 2:
('error', 'Index out of range')

-------------------------------------------------
Input Example 3:
safe_get([10, 20, 30], "1")

Output Example 3:
('error', 'Index must be an int')

=================================================

"""
import json

def safe_get(items, index):
    try:
        value = items[index]
        return ("ok", value)
    except IndexError:
        return ("error", "Index out of range")
    except TypeError:
        return ("error", "Index must be an int")
    except Exception as e:
        return ("error", f"Unexpected error: {e}")

full_user_input = input("Enter a JSON string for a list and an index, separated by a comma (e.g., '[1, 2, 3]', 1): ")

try:
    # Find the last comma to separate the list JSON string from the index
    last_comma_index = full_user_input.rfind(',')
    if last_comma_index == -1:
        raise ValueError("Input must contain a comma separating the list and index.")

    user_list_str = full_user_input[:last_comma_index].strip()
    user_index_str = full_user_input[last_comma_index + 1:].strip()

    my_list_from_user = json.loads(user_list_str)

    try:
        user_index = int(user_index_str)
    except ValueError:
        user_index = user_index_str

    result = safe_get(my_list_from_user, user_index)
    print(f"Result for list {my_list_from_user} at index {user_index_str}: {result}")

except ValueError as ve:
    print(f"Input format error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred during processing: {e}")