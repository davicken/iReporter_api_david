# validate  location input (should be a string)
def validate_string(r):
    if not isinstance(r,str):
        raise ValueError
    return 'Location is not a string'