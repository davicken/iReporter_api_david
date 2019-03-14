import re

def validate_create_redflag_data(data):
    # this function helps to validate input data whan creating a red-flag
    try:
        if (
            not isinstance(data['location'], dict)
            or not data['location']
            or not len(data['location']) == 2  
        ): 
            raise TypeError("location should be a dictionary with two items; Latitude and Longitude coordinates")

        if(
            not isinstance(data['comment'], str)
            or not data['comment']
            or data['comment'].isspace()
        ):
            raise TypeError("comment should be a string")

        if(
            not isinstance(data['title'], str)
            or not data['title']
            or data['title'].isspace()
        ):
            raise TypeError("title should be a string")

    except (TypeError) as error:
        return str(error)
    return None

def validate_create_user_data(data):
    # this function helps to validate input data whan creating a red-flag
    try:
        if not isinstance(data['first_name'], str) or not isinstance(data['last_name'], str) or not isinstance(data['other_names'],str):
            raise TypeError("All the names have to be of type string")

        if len(data['phone_number']) < 10:
            raise ValueError("The phone number should be a string of atleast 10 digits")

        if not re.match("[0-9]", data['phone_number']):
            raise ValueError("The phone number should be a string of only digits from 0 to 9")

        if not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", data['email']):
            raise ValueError("The email address is in the wrong format")

    except (TypeError, ValueError) as error:
        return str(error)
    return None

def validate_login_data(login_data):
    # this function validates login information
    try:
        if (
            not isinstance(login_data['user_name'], str)
            or not login_data['user_name']
            or not len(login_data['user_name']) > 3
        ): 
            raise TypeError("Username should be a string with atleast 4 characters")

        if (
            not login_data['password']
            or not len(login_data['password']) > 4
        ): 
            raise ValueError("password should atleast 5 characters in length")

    except (TypeError, ValueError) as error:
        return str(error)
    return None



