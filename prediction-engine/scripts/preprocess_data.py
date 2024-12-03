import pandas as pd

def preprocess_data(input_file, output_file):
    """
    Preprocess raw data by cleaning, normalizing, and saving.
    """
    # Load raw data
    raw_data = pd.read_csv(input_file)

    # Drop rows with missing values
    clean_data = raw_data.dropna()

    # Add feature engineering (if needed)
    # Example: clean_data['temperature_humidity_ratio'] = clean_data['temperature'] / clean_data['humidity']

    # Save the processed data
    clean_data.to_csv(output_file, index=False)
    print(f"Processed data saved to {output_file}")

# Example usage
if __name__ == "__main__":
    preprocess_data("../data/raw/air_quality_data.csv", "../data/processed/training_data.csv")
