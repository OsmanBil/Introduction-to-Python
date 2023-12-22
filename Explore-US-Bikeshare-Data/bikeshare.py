import pandas as pd
import numpy as np
import time
import os

CITY_DATA = { 'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv' }


def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input("Please enter the city you want to explore (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            print(f'You have chosen {city.title()}')
            break
        else:
            print('Please enter a valid city name: chicago, new york city, or washington.')

    time_filter = input("Would you like to filter the data by month, day, or not at all? Type 'none' for no time filter: ").lower()
    while time_filter not in ['month', 'day', 'none']:
        time_filter = input("Please type 'month', 'day', or 'none' for no time filter: ").lower()

    month = day = None
    if time_filter == 'month':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = input("Which month? January, February, March, April, May, or June: ").lower()
        while month not in months:
            month = input("Please enter a valid month name: ").lower()
    elif time_filter == 'day':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday: ").lower()
        while day not in days:
            day = input("Please enter a valid day: ").lower()
    print('-'*40)
    return city, month, day




def load_data(city, month=None, day=None):
    # Überprüfen, ob die Datei existiert
    filename = CITY_DATA[city]
    if not os.path.isfile(filename):
        print(f"Die Datei {filename} wurde nicht gefunden. Bitte überprüfe den Dateipfad und den Namen.")
        return None  # oder handle den Fehler, wie du möchtest
    
    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

        # Filter by month if applicable
    if month:
        # Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1  # +1 because the index is zero-based
        df = df[df['month'] == month]

        # Filter by day of the week if applicable
    if day:
        # Filter by day of week to create the new dataframe
        df = df[df['day_of_week'].str.lower() == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print("Most Common Month:", most_common_month)


    # display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print("Most Common Day of Week:", most_common_day_of_week)


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print("Most Common Start Hour:", most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("Most Commonly used start station:", most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("Most Commonly used end station:", most_common_end_station)

    # display most frequent combination of start station and end station trip
    df['Start_End_Combination'] = df['Start Station'] + " to " + df['End Station']
    most_common_start_end_combination = df['Start_End_Combination'].mode()[0]
    print("Most frequent combination of start station and end station trip:", most_common_start_end_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time:", total_travel_time, "seconds")

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time:", mean_travel_time, "seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types:\n", user_types)

    # Display counts of gender
    # Check if 'Gender' column exists
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of gender:\n", gender_counts)
    else:
        print("\nNo gender data to display.")

    # Display earliest, most recent, and most common year of birth
    # Check if 'Birth Year' column exists
    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        print("\nEarliest year of birth:", earliest_year)
        print("Most recent year of birth:", most_recent_year)
        print("Most common year of birth:", most_common_year)
    else:
        print("\nNo birth year data to display.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()
