
def create_new_string(input_str):
    if len(input_str) < 3:
        return "Input string should have at least 3 characters"
    
    middle_index = len(input_str) // 2
    
    new_str = input_str[0] + input_str[middle_index] + input_str[-1]
    
    return new_str
