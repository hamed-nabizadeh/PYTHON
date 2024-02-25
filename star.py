   
def inverted_star_pattern_recursive(height):
    if height > 0:
        print("*" * height)
        inverted_star_pattern_recursive(height - 1)
 
height = 5
inverted_star_pattern_recursive(height)
