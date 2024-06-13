import pandas as pd

def handle_missing_values(df, columns, method='ffill'):
    """
    Handle missing values in specified columns using the specified method.
    
    Parameters:
    df (pd.DataFrame): The dataframe to handle missing values.
    columns (list): List of column names to handle missing values.
    method (str): Method to handle missing values. Default is 'ffill'.
    
    Returns:
    pd.DataFrame: Dataframe with missing values handled.
    """
    if method == 'ffill':
        for column in columns:
            df[column] = df[column].ffill()
    return df

def convert_to_datetime(df, columns):
    """
    Convert specified columns to datetime.
    
    Parameters:
    df (pd.DataFrame): The dataframe to convert columns.
    columns (list): List of column names to convert.
    
    Returns:
    pd.DataFrame: Dataframe with columns converted to datetime.
    """
    for column in columns:
        df[column] = pd.to_datetime(df[column])
    return df

def calculate_trip_duration(df, start_column, end_column, new_column='trip_duration'):
    """
    Calculate the trip duration from start and end time columns.
    
    Parameters:
    df (pd.DataFrame): The dataframe to calculate trip duration.
    start_column (str): Name of the start time column.
    end_column (str): Name of the end time column.
    new_column (str): Name of the new column to store trip duration.
    
    Returns:
    pd.DataFrame: Dataframe with trip duration column added.
    """
    df[new_column] = (df[end_column] - df[start_column]).dt.total_seconds()
    return df

def calculate_iqr_bounds(df, column):
    """
    Calculate the lower and upper bounds for outliers using the IQR method.
    
    Parameters:
    df (pd.DataFrame): The dataframe to calculate IQR bounds.
    column (str): The column name to calculate IQR for.
    
    Returns:
    tuple: Lower and upper bounds for outliers.
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return lower_bound, upper_bound

def remove_outliers(df, column, lower_bound, upper_bound):
    """
    Remove outliers based on the specified column and bounds.
    
    Parameters:
    df (pd.DataFrame): The dataframe to remove outliers.
    column (str): The column name to check for outliers.
    lower_bound (float): The lower bound for the column values.
    upper_bound (float): The upper bound for the column values.
    
    Returns:
    pd.DataFrame: Dataframe with outliers removed.
    """
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

def drop_columns_with_missing_values(df, columns):
    """
    Drop specified columns with missing values.
    
    Parameters:
    df (pd.DataFrame): The dataframe to drop columns.
    columns (list): List of column names to drop.
    
    Returns:
    pd.DataFrame: Dataframe with specified columns dropped.
    """
    return df.drop(columns=columns)


def detect_outliers(df, column, lower_bound, upper_bound):
    """
    Detect outliers in the dataframe based on the specified column and bounds.
    
    Parameters:
    df (pd.DataFrame): The dataframe to detect outliers.
    column (str): The column name to check for outliers.
    lower_bound (float): The lower bound for the column values.
    upper_bound (float): The upper bound for the column values.
    
    Returns:
    pd.DataFrame: Dataframe with outliers detected.
    """
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers
