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
# Example usage
print(rearrange_number_difference(213))      # Output: 198
print(rearrange_number_difference(9870))     # Output: 8700
print(rearrange_number_difference(1203))     # Output: 3087
