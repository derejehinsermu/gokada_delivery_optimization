import requests
from datetime import datetime
import time
import pandas as pd

# Your OpenWeatherMap API key
api_key = '928c31ccec8350a00118f187ae4fd885'



# Cache to store fetched weather data
weather_cache = {}


def get_weather(lat, lon, retries=3):
    """
    Fetch weather data for a specific location with retries and exponential backoff.
    """
    # Create a unique key for the cache
    cache_key = (lat, lon)
    
    # Check if the weather data is already in the cache
    if cache_key in weather_cache:
        return weather_cache[cache_key]
    
    # OpenWeatherMap API endpoint for current weather data
    url = f'http://api.openweathermap.org/data/2.5/weather'
    
    # API request parameters
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key
    }
    
    attempt = 0
    while attempt <= retries:
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()
            
            # Check if it rained
            if 'rain' in data:
                weather = 'rain'
            else:
                weather = 'no-rain'
            
            # Store the result in the cache
            weather_cache[cache_key] = weather
            return weather
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather for {lat}, {lon}: {e}")
            attempt += 1
            if attempt > retries:
                print("Max retries reached. Moving to next.")
                return 'unknown'
            wait_time = 2 ** attempt  # Exponential backoff
            print(f"Retrying in {wait_time} seconds...")
            time.sleep(wait_time)

def fetch_weather_data(df, save_interval=50, retries=3):
    """
    Fetch weather data for each row in the dataframe with retries and periodic saving.
    """
    total_rows = len(df)
    for index, row in df.iterrows():
        # Skip rows that already have weather data
        if pd.notna(row.get('weather')):
            continue
        
        try:
            weather_condition = get_weather(row['lat'], row['lng'], retries=retries)
            df.at[index, 'weather'] = weather_condition
        except Exception as e:
            print(f"Error processing index {index}: {e}")
            df.at[index, 'weather'] = 'unknown'
        
        # Save progress periodically
        if (index + 1) % save_interval == 0:
            df.to_csv('weather_data_progress.csv', index=False)
            print(f"Progress saved at row {index+1}")
        
        # Print progress with weather condition
        print(f"Processed {index+1}/{total_rows} rows. Weather condition: {df.at[index, 'weather']}")
    
    # Final save
    df.to_csv('weather_data_progress.csv', index=False)
    print("Completed fetching weather data.")
    return df

# # Check if CSV file exists and load it, otherwise create a new dataframe
# save_path = 'weather_data.csv'
# if os.path.exists(save_path):
#     df = pd.read_csv(save_path)
# else:
#     data = {
#         'City': ['Lagos'],
#         'Trip Origin Lat': [6.5833],
#         'Trip Origin Lng': [3.75],
#         'Trip Start Time': [datetime(2023, 6, 1)],
#         'weather': [None]  # Initialize weather column with None
#     }
#     df = pd.DataFrame(data)

# df = fetch_weather_data(df, save_interval=2, save_path=save_path)
# print(df)


# Check if CSV file exists and load it, otherwise create a new dataframe
# save_path = 'weather_data.csv'
# # Example usage with a sample dataframe including city name
# data = {
#     'City': ['Lagos'],
#     'Trip Origin Lat': [0.5833],
#     'Trip Origin Lng': [3.75],
#     'Trip Start Time': [datetime(2023, 6, 1)]
# }
# df = pd.DataFrame(data)
# df = fetch_weather_data(df)
# print(df)
