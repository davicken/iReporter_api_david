def validate_create_redflag_data(data):
    # this function helps to validate input data whan creating a red-flag
    try:
        if (
            not isinstance(data['location'], dict)
            or not data['location']
            or not len(data['location']) == 2  
        ): 
            raise TypeError("location must be a dictionary with two items; Latitude and Longitude coordinates")

        if(
            not isinstance(data['comment'], str)
            or not data['comment']
            or data['comment'].isspace()
        ):
            raise TypeError("comment must be a string")

        if(
            not isinstance(data['title'], str)
            or not data['title']
            or data['title'].isspace()
        ):
            raise TypeError("title must be a string")

    except (TypeError, ValueError) as error:
        return str(error)
    return None

