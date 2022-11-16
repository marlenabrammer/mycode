#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime
import reverse_geocoder as rg

URL= "http://api.open-notify.org/iss-now.json"
def main():
    #get the timestamp
    resp= requests.get(URL).json()
    timestamp = resp["timestamp"]
    adjusted_ts = datetime.datetime.fromtimestamp(timestamp)
    long = resp["iss_position"]["longitude"]
    lat = resp["iss_position"]["latitude"]
    
    #convert to city
    resp_city = rg.search((lat, long))
    city = resp_city[0]["name"]
    country = resp_city[0]["cc"]

    print(f"Current location of the ISS:\n Timestamp: {adjusted_ts}\n Long:{long}\n Lat:{lat}\n City/Country: {city}, {country}\n")

if __name__ == "__main__":
    main()

