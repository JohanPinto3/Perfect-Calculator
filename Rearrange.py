def rearrange_number_difference(num):
    # Make sure the input is a non-negative integer
    if not isinstance(num, int) or num < 0:
        raise ValueError("Input must be a non-negative integer")

    # Convert number to string, extract and sort digits
    digits = list(str(num))
    smallest = int(''.join(sorted(digits)))
    largest = int(''.join(sorted(digits, reverse=True)))

    # Return the difference
    return largest - smallest
