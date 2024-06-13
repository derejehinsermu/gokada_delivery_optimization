import requests
from datetime import datetime
import time

# Your OpenWeatherMap API key
api_key = '928c31ccec8350a00118f187ae4fd885'

# Cache to store fetched weather data
weather_cache = {}

def get_weather(lat, lon, date):
    """
    Fetch weather data for a specific location and date.
    """
    # Create a unique key for the cache
    cache_key = (lat, lon, date)
    
    # Check if the weather data is already in the cache
    if cache_key in weather_cache:
        return weather_cache[cache_key]
    
    # Convert date to UNIX timestamp
    unix_timestamp = int(time.mktime(datetime.strptime(str(date), "%Y-%m-%d").timetuple()))
    
    # OpenWeatherMap API endpoint for historical data
    url = f'http://api.openweathermap.org/data/2.5/weather?'
    
    # API request parameters
    params = {
        'lat': lat,
        'lon': lon,
        'dt': unix_timestamp,
        'appid': api_key
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        
        # Example condition: If it rained on that date
        if 'current' in data and 'rain' in data['current']:
            weather = 'rain'
        else:
            weather = 'no-rain'
        
        # Store the result in the cache
        weather_cache[cache_key] = weather
        return weather
    
    except Exception as e:
        print(f"Error fetching weather for {lat}, {lon} on {date}: {e}")
        print("Response content:", response.content)
        return 'unknown'

def fetch_weather_data(df):
    """
    Fetch weather data for each row in the dataframe.
    """
    total_rows = len(df)
    for index, row in df.iterrows():
        try:
            df.at[index, 'weather'] = get_weather(row['Trip Origin Lat'], row['Trip Origin Lng'], row['Trip Start Time'].date())
            time.sleep(1)  # Add delay to respect API rate limits
        except Exception as e:
            print(f"Error processing index {index}: {e}")
            df.at[index, 'weather'] = 'unknown'
        
        # Print progress
        if index % 100 == 0:
            print(f"Processed {index}/{total_rows} rows.")
    
    print("Completed fetching weather data.")
    return df
