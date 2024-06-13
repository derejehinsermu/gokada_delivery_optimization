
import holidays

def add_holiday_feature(df):
    """
    Add a holiday feature to the dataframe.
    """

    # Generate holiday feature
    ng_holidays = holidays.Nigeria(years=df['Trip Start Time'].dt.year.unique())
    df['is_holiday'] = df['Trip Start Time'].dt.date.apply(lambda x: x in ng_holidays)
    
    print("Completed adding holiday feature.")
    return df