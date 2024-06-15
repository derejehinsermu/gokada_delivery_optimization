import numpy as np
from geopy.distance import geodesic
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from math import radians, cos, sin, asin, sqrt
from geopy.distance import geodesic
from sklearn.preprocessing import MinMaxScaler

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # Convert decimal degrees to radians 
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r

# Define a function to calculate the distance between two points
def calculate_distance(row):
    origin = (row['Trip Origin Lat'], row['Trip Origin Lng'])
    destination = (row['Trip Destination Lat'], row['Trip Destination Lng'])
    distance = geodesic(origin, destination).km
    return distance


# def compute_additional_features(df):
#     """
#     Compute distances, driving speed, and other key variables.
#     """
#     # Calculate Haversine distance
#     df['distance_km'] = df.apply(lambda row: haversine_distance(row['Trip Origin Lat'], row['Trip Origin Lng'], 
#                                                                 row['Trip Destination Lat'], row['Trip Destination Lng']), axis=1)
    
#     # Calculate driving speed (km/h)
#     df['driving_speed_kmph'] = df['distance_km'] / (df['trip_duration'] / 3600)
    
#     return df

def clean_features(df):
    """
    Clean the trip_duration and driving_speed_kmph features.
    """
    # Remove unrealistic trip_duration values
    df = df[(df['trip_duration'] > 0) & (df['trip_duration'] < 86400)]  # Less than 24 hours

    # Remove unrealistic driving_speed_kmph values
    df = df[(df['driving_speed_kmph'] > 0) & (df['driving_speed_kmph'] < 200)]  # Less than 200 km/h

    return df

def normalize_features(df, columns):
    """
    Normalize specified columns in the dataframe.
    """
    # # Replace infinite values with NaN
    # df[columns] = df[columns].replace([np.inf, -np.inf], np.nan)
    
    # # Check for NaN values and print summary statistics
    # print("Summary statistics before filling NaNs:")
    # print(df[columns].describe())
    # print("Number of NaNs in each column before filling:")
    # print(df[columns].isna().sum())
    
    # # Fill NaN values with the median of each column
    # df[columns] = df[columns].fillna(df[columns].median())
    
    # # Check for NaN values again
    # print("Number of NaNs in each column after filling:")
    # print(df[columns].isna().sum())
    
    scaler = MinMaxScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df

from scipy.spatial import cKDTree

def count_orders_within_radius(df, radius=0.5):
    """
    Count the number of accepted and unfulfilled orders within a given radius (in km).
    """
    # Initialize columns to count orders within the radius
    df['accepted_within_radius'] = 0
    df['unfulfilled_within_radius'] = 0

    # Prepare coordinates for the KDTree
    coords = np.radians(df[['lat', 'lng']].values)
    tree = cKDTree(coords)

    # Radius in radians
    radius_radians = radius / 6371.0

    for index, row in df.iterrows():
        lat, lon = np.radians([row['lat'], row['lng']])
        
        # Query the KDTree for neighbors within the radius
        indices = tree.query_ball_point([lat, lon], radius_radians)

        accepted_count = 0
        unfulfilled_count = 0

        for i in indices:
            if i != index:
                if df.at[i, 'driver_action'] == 'accepted':
                    accepted_count += 1
                elif df.at[i, 'driver_action'] == 'rejected':
                    unfulfilled_count += 1

        # Update the count columns for the current order
        df.at[index, 'accepted_within_radius'] = accepted_count
        df.at[index, 'unfulfilled_within_radius'] = unfulfilled_count

        # Print progress every 100 rows
        if index % 1000 == 0:
            print(f"Processed {index}/{len(df)} rows.")
    
    return df




def compute_clusters(df, n_clusters=10):
    """
    Compute clusters for the starting and destination locations.
    """
    # Clustering for trip origins
    kmeans_origin = KMeans(n_clusters=n_clusters, random_state=0).fit(df[['Trip Origin Lat', 'Trip Origin Lng']])
    df['origin_cluster'] = kmeans_origin.labels_
    
    # Clustering for trip destinations
    kmeans_destination = KMeans(n_clusters=n_clusters, random_state=0).fit(df[['Trip Destination Lat', 'Trip Destination Lng']])
    df['destination_cluster'] = kmeans_destination.labels_
    
    return df, kmeans_origin, kmeans_destination


