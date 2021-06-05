from app.settings import GEOCODING_API, GEOCODING_API_KEY, PROTOCOL
import requests

class Geocoding:

    @staticmethod
    def get_latlong(address: str) -> tuple : 
        """[Performs a request to the endpoint defined at app.settings.GEOCODING_API, it retrieves a 
            json from which is extracted the latitude and the longitude]

        Args:
            address (str): [The address to be send to the api as parameter and geocoded as latitude and longitude]

        Returns:
            tuple: [returns a tuple of floating numbers, the latitude and the longitude of the address]
        """
        url = PROTOCOL + "://" + GEOCODING_API.format(GEOCODING_API_KEY ,address)
        response =  requests.get(url)

        return response.json().get("latitude", None), response.json().get("longitude", None)
