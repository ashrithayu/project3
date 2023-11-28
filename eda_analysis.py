
import seaborn as sns
import matplotlib.pyplot as plt

class EDAAnalyzer:
    def __init__(self, data):
        """
        Initializes an EDAAnalyzer object.

        Parameters:
        - data (pd.DataFrame): The input dataset for exploratory data analysis.
        """
        self.data = data

    def plot_member_distribution(self, col1):
        """
        Plots the distribution of member and non-member rides based on the specified column.

        Parameters:
        - col1 (str): The column to visualize for member distribution.
        """
        plt.figure(figsize=(6, 4))
        sns.countplot(x=col1, data=self.data)
        plt.title('Distribution of Member and Non-Member Rides')
        plt.show()

    def plot_duration_distribution(self, col1):
        """
        Plots the distribution of ride durations based on the specified column.

        Parameters:
        - col1 (str): The column representing ride durations.
        """
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data[col1], bins=50, kde=True)
        plt.title('Distribution of Ride Durations')
        plt.xlabel('Duration (seconds)')
        plt.ylabel('Frequency')
        plt.show()

    def display_missing_values(self):
        """
        Displays the count of missing values in the dataset.
        """
        print("\n\nMissing Values:\n", self.data.isna().sum())

    def display_data_info(self):
        """
        Displays general information about the dataset using the pandas info method.
        """
        print("\n\n Data Information:\n")
        print(self.data.info())
