#Bayer AG, through its acquisition of Monsanto, is a significant player in the agricultural sector, 
#making it another great example for a Weather-based Stock Analysis App. Analyzing the impact of weather 
#on Bayer’s agricultural division could provide valuable insights for investors interested in the 
#intersection of agriculture and financial markets.

import requests
import random

def get_weather_data(lat, lon):
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/117.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    ]
    headers = {
        'User-Agent': random.choice(user_agents)
    }
    #Lat and Lon of Kossuth County, Iowa
    lat = 43.2513
    lon = 94.2333
    
    #Get metadata for the location
    api_url = f'https://api.weather.gov/points/{lat},{lon}'
    response = requests.get(api_url, headers=headers)
    if response.status_code != 200:
        print('Failed to get location metadata:', response.text)
        return None
    
    metadata = response.json
    
    #Get the forcast URL from the metadata
    forecast_url = metadata.get('properties', {}).get('forecast')
    if not forecast_url:
        print('Failed to find forecast URL in metadata')
        return None
    
    #Get the weather data
    response = requests.get(forecast_url, headers = headers)
    if response.status_code != 200:
        print('Failed to get weather data:', response.text)
        return None
    
    weather_data = response.json()
    return weather_data
get_weather_data()
    
    
'Research: New weather API to get california, arizona, and chile weather data for the past year - https://open-meteo.com/en/docs'