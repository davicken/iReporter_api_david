def validate_create_redflag_data(data):
    # this function helps to validate input data whan creating a red-flag
    try:
        if (
            not isinstance(data['location'], dict)
            or not (data['location']
            or len(data['location']) == 2)
        ): 
            raise TypeError("location must be a dictionary with two items; Latitude and Longitude coordinates")

        if(
            not isinstance(data['title'], str)
            or not isinstance(data['comment'], str)
            or not data['title']
            or not data['comment']
            or data['title'].isspace()
            or data['comment'].isspace()
        ):
            raise TypeError("Comment and Title must be strings")

    except (TypeError, ValueError) as error:
        return str(error)
    return None

