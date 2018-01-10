from collections import defaultdict

import requests
import housecanary
from pyquery import PyQuery
import json
from googleplaces import GooglePlaces

CANARY_KEY = '1IDZ8YXOD4XAZQKIIGH3'
CANARY_SECRET = 'Bhuvt3vl5fmARuc8PE9dBcQN2T7MI2k8'

if __name__ == "__main__":

    gp = GooglePlaces('AIzaSyA90uHAZ0H3xm6S6vd5SXVRCZ9yFY8tJBU')
    addresses = []
    responses = []
    client = housecanary.ApiClient(CANARY_KEY, CANARY_SECRET)
    with open("./addresses.txt", "r") as addressFile:
        for address in addressFile:
            addresses = [tuple(x) for x in json.loads(address)]

    for addr in addresses:
        response = client.property.details(addr).json()
        responses.append({"address": addr, "response": response})
    x=3