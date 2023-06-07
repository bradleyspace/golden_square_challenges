def make_snippet(string):
    string_list = string.split(" ")

    if len(string_list) < 5:
        return string
    
    first_five = string_list[:5]
    output_string = " ".join(first_five)
    output_string += "..."
    return output_string