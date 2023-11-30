import seaborn as sns
import matplotlib.pyplot as plt

class ResearchQuestionsAnalyzer:
    def __init__(self, data):
        """
        Initializes a ResearchQuestionsAnalyzer object.

        Parameters:
        - data (pd.DataFrame): The input dataset for research questions analysis.
        """
        self.data = data

    def add_is_weekend_column(self):
        """
        Adds a new column 'is_weekend' to the dataset indicating whether a ride occurred on a weekend.

        Returns:
        - pd.DataFrame: The dataset with the 'is_weekend' column added.
        """
        data = self.data
        data['is_weekend'] = data['Start_Weekday'].apply(lambda x: True if x >= 5 else False)
        return data

    def temporal_dynamics_analysis(self):
        """
        Performs temporal dynamics analysis, plotting the distribution of rides during the day for weekdays and weekends.
        """
        data = self.data

        # Plot distribution of rides during the day for weekdays
        plt.figure(figsize=(12, 6))
        sns.countplot(x='Start_Hour', data=data[data['is_weekend'] == False])
        plt.title('Distribution of Rides During the Day on Weekdays')
        plt.show()

        # Plot distribution of rides during the day for weekends
        plt.figure(figsize=(12, 6))
        sns.countplot(x='Start_Hour', data=data[data['is_weekend'] == True])
        plt.title('Distribution of Rides During the Day on Weekends')
        plt.show()

    def duration_distribution_analysis(self):
        """
        Analyzes the distribution of bike rental durations.
        """
        # Research Question 2
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data['duration_sec'], bins=50, kde=True)
        plt.title('Distribution of BIXI Bike Rental Durations')
        plt.xlabel('Duration (seconds)')
        plt.ylabel('Frequency')
        plt.show()

    def temporal_peak_hours_analysis(self):
        """
        Analyzes the temporal peak hours of bike rentals.
        """
        # Research Question 3
        rentals_by_hour = self.data['Start_Hour'].value_counts().sort_index()
        rentals_by_hour.plot(kind='line')
        plt.title('Hourly Trends in BIXI Bike Usage')
        plt.xlabel('Hour of the Day')
        plt.ylabel('Number of Rentals')
        plt.show()

        popular_hour = self.data['Start_Hour'].mode()[0]
        print(f'The most popular time of day for bike rentals is {popular_hour}:00.')

    def longitudinal_trends_analysis(self):
        """
        Analyzes the longitudinal trends of bike rentals.
        """
        # Research Question 4
        daily_rentals = self.data.groupby(self.data['start_date'].dt.date).size()
        plt.figure(figsize=(12, 6))
        daily_rentals.plot(title='Daily Trend of Bike Rentals', xlabel='Date', ylabel='Number of Rentals')
        plt.show()

    def frequent_stations_analysis(self):
        """
        Analyzes the most frequent start and end stations for bike rentals.
        """
        # Research Question 5
        start_stations = self.data['start_station_code'].value_counts().head(10)
        end_stations = self.data['end_station_code'].value_counts().head(10)
        plt.figure(figsize=(14, 6))
        plt.subplot(1, 2, 1)
        start_stations.plot(kind='barh', color='skyblue')
        plt.title('Top 10 Start Stations')
        plt.xlabel('Number of Rentals')
        plt.ylabel('Station Code')

        plt.subplot(1, 2, 2)
        end_stations.plot(kind='barh', color='skyblue')
        plt.title('Top 10 End Stations')
        plt.xlabel('Number of Rentals')
        plt.ylabel('Station Code')

        plt.tight_layout()
        plt.show()

    def user_type_duration_analysis(self):
        """
        Analyzes the distribution of rental durations for different user types (members and occasional users).
        """
        # Research Question 6
        members = self.data[self.data['is_member'] == 1]
        occasional_users = self.data[self.data['is_member'] == 0]

        plt.hist(members['duration_sec'] / 60, bins=range(0, 100, 4), alpha=0.5, label='Members', color='skyblue', edgecolor='black')
        plt.hist(occasional_users['duration_sec'] / 60, bins=range(0, 100, 4), alpha=0.5, label='Occasional Users', color='orange', edgecolor='black')
        plt.title('Distribution of Rental Durations for Each User Type')
        plt.xlabel('Duration (minutes)')
        plt.ylabel('Number of Rentals')
        plt.legend()
        plt.show()

    def weekly_variations_analysis(self):
        """
        Analyzes the number of bike trips by day of the week.
        """
        # Research Question 7
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        trip_counts_per_day = self.data['Start_Weekday'].value_counts()

        plt.figure(figsize=(12, 6))
        plt.bar(days, trip_counts_per_day, color='skyblue')
        plt.xlabel('Day of the Week')
        plt.ylabel('Number of Trips')
        plt.title('Number of Bike Trips by Day of the Week')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def weekly_duration_variations_analysis(self):
        """
        Analyzes the average trip duration by weekday for members and non-members.
        """
        # Research Question 8
        avg_duration_by_weekday_member = self.data[self.data['is_member'] == 1].groupby('Start_Weekday')['duration_sec'].mean()
        avg_duration_by_weekday_non_member = self.data[self.data['is_member'] == 0].groupby('Start_Weekday')['duration_sec'].mean()

        plt.figure(figsize=(10, 6))
        plt.plot(avg_duration_by_weekday_member, label='Member', marker='o')
        plt.plot(avg_duration_by_weekday_non_member, label='Non-Member', marker='o')
        plt.title('Average Trip Duration by Weekday for Members vs. Non-Members')
        plt.xlabel('Day of the Week')
        plt.ylabel('Average Duration (seconds)')
        plt.legend()
        plt.show()


