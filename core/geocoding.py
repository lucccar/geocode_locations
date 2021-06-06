import requests

from app.settings import GEOCODING_ENDPOINT, GEOCODING_API_KEY, PROTOCOL
from core.util.util import validate_response, handle_response


class Geocoding:
    # def __init__(self, *args, **kwargs) -> None:
    #     super().__init__(*args, **kwargs)

        

    @staticmethod
    def get_latlong(address: str) -> tuple : 
        """[Performs a request to the endpoint defined at app.settings.GEOCODING_ENDPOINT, it retrieves a 
            json from which is extracted the latitude and the longitude]

        Args:
            address (str): [The address to be send to the api as parameter and geocoded as latitude and longitude]

        Returns:
            tuple: [returns a tuple of floating numbers, the latitude and the longitude of the address]
        """
        url = PROTOCOL + "://" + GEOCODING_ENDPOINT.format(GEOCODING_API_KEY ,address)
        response =  requests.get(url)
        validate_response(response)
        local = handle_response(response)
        return local.get("latitude", None), local.get("longitude", None)



    def get_latlong_batch(self) -> list : 
        """[Performs a request to the endpoint defined at app.settings.GEOCODING_API, it retrieves a 
            json from which is extracted the latitude and the longitude for each address]

        Returns:
            tuple: [returns a list with all the informations of the customers.csv added by its latitude and longitude]
        """

        batch = {
            "batch": []
        }

        for customer in self.customers:
        # for address in addresses:
            query = {
                "query": customer[6]
            }
            batch["batch"].append(query)

        print(batch)
        
        url = PROTOCOL + "://" + GEOCODING_ENDPOINT.format(GEOCODING_API_KEY)
        response =  requests.post(url, data=batch)

        print("response: ", response)

        data = response.json()["data"]
        for result in data:
            self.customers.append(result.get("latitude", None), result.get("longitude", None))

        return self.customers