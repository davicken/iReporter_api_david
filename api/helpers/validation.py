def validate_create_redflag_data(data):
    # this function helps to validate input data whan creating a red-flag
    try:
        if (
            not isinstance(data['location'], dict)
            or not (data['location'] and len(data['location']) == 2)
        ): 
            raise TypeError("location must be a dictionary with two items; Latitude and Longitude coordinates")

        if(
            not (isinstance(data['comment'], str) and isinstance(data['title'], str))
            or not (data['comment'] and data['title'])
            or (data['comment'].isspace() and data['title'].isspace())
        ):
            raise TypeError("Comment and Title must be strings")


    except (TypeError, ValueError) as error:
        return str(error)
    return None

