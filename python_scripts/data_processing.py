import pandas as pd

class DataProcessor:
    def __init__(self, file_path):
        """
        Initializes a DataProcessor object.

        Parameters:
        - file_path (str): The path to the CSV file containing the data.
        """
        self.data = pd.read_csv(file_path)

    def handle_missing_values(self):
        """
        Handles missing values in the dataset by removing rows with NaN values in any column.
        """
        self.data.dropna(inplace=True)

    def remove_duplicates(self):
        """
        Removes duplicate rows from the dataset.
        """
        self.data.drop_duplicates(inplace=True)

    def feature_engineering(self):
        """
        Performs feature engineering on the dataset by creating new columns based on date-time features.
        """
        self.data['start_date'] = pd.to_datetime(self.data['start_date'])
        self.data['end_date'] = pd.to_datetime(self.data['end_date'])

        self.data["Start_Day"] = self.data["start_date"].dt.day
        self.data["Start_Weekday"] = self.data["start_date"].dt.weekday
        self.data["Start_Hour"] = self.data["start_date"].dt.hour

        self.data["End_Day"] = self.data["end_date"].dt.day
        self.data["End_Weekday"] = self.data["end_date"].dt.weekday
        self.data["End_Hour"] = self.data["end_date"].dt.hour

    def get_data(self):
        """
        Returns the processed dataset.

        Returns:
        - pd.DataFrame: The processed dataset.
        """
        return self.data
