import pandas as pd
import tensorflow as tf


def consolidate_weather_description(data: pd.DataFrame) -> pd.DataFrame:
    """
    Combine one-hot encoded weather description columns into a single feature.

    :param data: Input DataFrame with one-hot encoded weather description columns.
    :return: DataFrame with a single consolidated weather_condition column.
    """
    # Define the weather columns
    # weather_columns = [
    #     'weather_description_broken clouds',
    #     'weather_description_clear sky',
    #     'weather_description_extreme rain',
    #     'weather_description_few clouds',
    #     'weather_description_heavy intensity rain',
    #     'weather_description_light rain',
    #     'weather_description_moderate rain',
    #     'weather_description_overcast clouds',
    #     'weather_description_scattered clouds',
    #     'weather_description_very heavy rain',
    # ]
    #
    # # Function to consolidate weather condition
    # def get_weather_condition(row):
    #     for col in weather_columns:
    #         if row[col]:
    #             return col.replace('weather_description_', '').replace('_', ' ')
    #     return 'unknown'
    #
    # # Apply the function to add a new column
    # data['weather_description'] = data.apply(get_weather_condition, axis=1)
    #
    # # Drop the original one-hot encoded columns
    # data = data.drop(columns=weather_columns)

    return data
