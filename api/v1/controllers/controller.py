# validate  location input (should be a string)
def validate_string(r):
    if not isinstance(r,str):
        raise ValueError
    return 'Location is not a string'

# def required_image_field(img):
#     if len(img) == 0:
#         return 'You should attach an image evidance'

# def comment_length(comm):
#     if len(comm) > 4:
#         return 'Please enter at most 4 characters'