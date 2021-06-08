import requests

from app.settings import GEOCODING_ENDPOINT, GEOCODING_API_KEY, PROTOCOL
from core.util.util import validate_response


class Geocoding:

    @staticmethod
    def get_latlong(address: str) -> tuple : 
        """Performs a request to the endpoint defined at app.settings.GEOCODING_ENDPOINT, it retrieves a 
            json from which is extracted the latitude and the longitude. 
            If the Geocode API was not able to find any location matching the address, the functions returns None, None.

        Args:
            address (str): The address to be send to the api as parameter and geocoded as latitude and longitude

        Returns:
            tuple: returns a tuple of floating numbers, the latitude and the longitude of the address
        """

        try:
            url = PROTOCOL + "://" + GEOCODING_ENDPOINT.format(address, GEOCODING_API_KEY)
            response =  requests.get(url)
            validate_response(response)

            if len(response.json()["results"]) != 0:
                data = response.json()["results"][0]
                return data["geometry"]["location"].get("lat", None), data["geometry"]["location"].get("lng", None)
            else:
                return None, None

        except AttributeError as e:
            print("response: ",response.json())
            print(e)
        except Exception as e:
            print(e)



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