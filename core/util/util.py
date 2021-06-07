def validate_response(response):
    """This function perform a simple validation of the response of a request.

    Args:
        response (response class): A response from a http request.
    """

    if response.status_code != 200:
        print(response.status_code)
        print(response.json())
        raise "Response invalid."


def handle_response(response):
    """This function solves a problem for when the address passed to the geocode api is ambiguous. 
    In this case the response is a list of all possible location. 
    This function performs a validation filtering for the country US.

    Args:
        response (response class): A response from a http request.

    Returns:
        json: A json with all information from a localitty. 
    """
    if len(response.json()["data"]) > 1:
        for js in response.json()["data"]:
            if js["country"] == "United States":
                return js