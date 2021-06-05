from app.settings import GEOCODING_API, API_KEY
import requests

def get_latlong(address: str) -> tuple : 
    """[Performs a request to the endpoint defined at app.settings.GEOCODING_API, it retrieves a 
        json from which is extracted the latitude and the longitude]

    Args:
        address (str): [The address to be send to the api as parameter and geocoded as latitude and longitude]

    Returns:
        tuple: [returns a tuple of floating numbers, the latitude and the longitude of the address]
    """

    response =  requests.get(GEOCODING_API.format(API_KEY ,address))
    pass
