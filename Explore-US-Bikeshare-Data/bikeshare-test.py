import pandas as pd
import numpy as np
import time

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

    return city, month, day




def load_data(city, month=None, day=None):
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



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        print(df.head())  # Zeigt die ersten Zeilen der Daten als schnelle Überprüfung

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()
