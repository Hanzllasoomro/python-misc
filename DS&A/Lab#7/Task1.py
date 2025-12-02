class PracticalError(Exception):
    """Base class for custom exceptions for this practical."""
    pass

class InvalidRangeError(PracticalError):
    """Raised when the provided number range is invalid (non-positive or not int)."""
    def __init__(self, message="Input must be a positive integer (>= 1)."):
        super().__init__(message)

def get_even_numbers(n):
    """
    Return a list of even numbers from 1 to n (inclusive).
    Raises InvalidRangeError for invalid inputs.
    """
    if not isinstance(n, int) or n < 1:
        raise InvalidRangeError(f"Invalid n={n!r}. n must be a positive integer >= 1.")
    return [i for i in range(1, n + 1) if i % 2 == 0]

def get_odd_numbers(n):
    """
    Return a list of odd numbers from 1 to n (inclusive).
    Raises InvalidRangeError for invalid inputs.
    """
    if not isinstance(n, int) or n < 1:
        raise InvalidRangeError(f"Invalid n={n!r}. n must be a positive integer >= 1.")
    return [i for i in range(1, n + 1) if i % 2 == 1]

def print_even(n):
    """Print even numbers up to n in a friendly format."""
    evens = get_even_numbers(n)
    print(f"Even numbers from 1 to {n}:")
    if evens:
        print(", ".join(map(str, evens)))
    else:
        print("(None)")

def print_odd(n):
    """Print odd numbers up to n in a friendly format."""
    odds = get_odd_numbers(n)
    print(f"Odd numbers from 1 to {n}:")
    if odds:
        print(", ".join(map(str, odds)))
    else:
        print("(None)")

def save_numbers_to_file(evens, odds, filename="numbers_output.txt"):
    """
    Save the even and odd lists to a file using a context manager.
    Demonstrates file I/O and handles IOError.
    """
    try:
        with open(filename, "w") as fh:
            fh.write(f"Even numbers ({len(evens)}):\n")
            fh.write(", ".join(map(str, evens)) + "\n\n")
            fh.write(f"Odd numbers ({len(odds)}):\n")
            fh.write(", ".join(map(str, odds)) + "\n")
    except IOError as e:
        # Handle possible file-related errors
        print("File I/O error while writing to", filename, ":", e)
        raise

# Example usage and demonstration of exception handling
if __name__ == "__main__":
    while True:
        try:
            # Ask user for input
            user_input = input("\nEnter a positive integer (or 'q' to quit): ")
            if user_input.lower() == 'q':
                print("Exiting program.")
                break

            n = int(user_input)  # may raise ValueError

            # Attempt to get evens and odds (this may raise InvalidRangeError)
            evens = get_even_numbers(n)
            odds  = get_odd_numbers(n)

        except ValueError:
            print("Invalid input! Please enter a valid integer.")
        except InvalidRangeError as err:
            print("Caught custom exception:", err)
        except Exception as err:
            print("An unexpected error occurred:", type(err).__name__, err)
        else:
            # If no exception: print and save to file
            print_even(n)
            print_odd(n)

            # Save results to file and show success message
            out_fn = f"numbers_n_{n}.txt"
            try:
                save_numbers_to_file(evens, odds, filename=out_fn)
            except IOError:
                print("Failed to save to file:", out_fn)
            else:
                print(f"Results saved to file: {out_fn}")
        finally:
            print("Finished processing input.")
