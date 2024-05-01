import requests

class MakeReq:
    @staticmethod
    def getResponse(partenza, destinazione):
        #how to handle exceptions here?
        url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        params = {
            "originLocationCode": partenza,
            "destinationLocationCode": destinazione,
            "departureDate": "2024-05-01",
            "adults": 1,
            "nonStop": "true",
            "max": 4
        }
        headers = {
            "accept": "application/vnd.amadeus+json",
            "Authorization": "Bearer PELdn9be9CZz2Zr7Fje4YUiVJkLn"
        }
        response = requests.get(url, headers=headers, params=params)
        
        return response.status_code, response.json()
    
    @staticmethod
    def sup():
        #how to handle exceptions here?
        try:
            response = requests.get("https://www.google.it")
            return response.status_code, response.text
        except Exception as e:
            print("Exception occurred... " + str(e))
            return -1, -1
        
#testing
if __name__ == '__main__':
    obj = MakeReq.sup()
    print(obj[0], obj[1])