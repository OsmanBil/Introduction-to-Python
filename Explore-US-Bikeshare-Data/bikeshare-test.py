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

    return city, month, day




def load_data(city):
    df = pd.read_csv(CITY_DATA[city])


    return df




def main():
    while True:
        city = get_filters()
        df = load_data(city)
        print(df.head())  # Zeigt die ersten Zeilen der Daten als schnelle Überprüfung

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
