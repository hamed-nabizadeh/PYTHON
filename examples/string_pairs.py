def string_pairs(input_string):
    pairs = []

    # Iterate through the string with a step of 2
    for i in range(0, len(input_string), 2):
        # Check if there is another character after the current one
        if i + 1 < len(input_string):
            # Add the pair to the list
            pairs.append(input_string[i:i+2])
        else:
            # If the string has an odd number of characters, add an asterisk in the final pair
            pairs.append(input_string[i] + '*')

    return pairs

# Example usage:
input_str = "abcdefgh"
result = string_pairs(input_str)
print(result)
