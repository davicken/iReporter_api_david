# validate  
def validate_string(r):
    if not isinstance(r, str):
        raise ValueError
    return 'comment should be a string'
