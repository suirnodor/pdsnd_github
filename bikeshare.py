# BikeShare Analysis
# Este programa permite a los usuarios explorar y analizar datos de bicicletas compartidas en diferentes ciudades.
# Proporciona estadísticas y visualización de información relevante.
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    Pide al usuario que especifique una ciudad, mes y día para analizar.

     Devoluciones:
         (str) ciudad - nombre de la ciudad a analizar
         (str) mes: nombre del mes por el que filtrar, o "todos" para aplicar el filtro sin mes
         (str) día - nombre del día de la semana por el que filtrar, o "todos" para aplicar el filtro sin día
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Enter the city you want to analyze (Chicago, New York City, or Washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid city name. Please enter a valid city.")

    # TO DO: get user input for month (all, january, february, ... , june)
    valid_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input("Enter the month you want to filter by (January, February, ..., June) or 'all' for no filter: ").lower()
        if month in valid_months:
            break
        else:
            print("Invalid month name. Please enter a valid month or 'all'.")
   


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    valid_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input("Enter the day of the week you want to filter by (Monday, Tuesday, ..., Sunday) or 'all' for no filter: ").lower()
        if day in valid_days:
            break
        else:
            print("Invalid day of the week. Please enter a valid day or 'all'.")
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load data file into a DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

   # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filter by month if applicable
    if month != 'all':
        # Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # Filter by month to create the new DataFrame
        df = df[df['month'] == month]

        # Filter by day of week if applicable
    if day != 'all':
        # Filter by day of week to create the new DataFrame
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('Most Common Day of Week:', common_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['Trip'].mode()[0]
    print('Most Frequent Trip:', common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of User Types:\n', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('\nCounts of Gender:\n', gender_counts)
    else:
        print('\nGender data not available for this city.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    start_loc = 0
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    while view_data == 'yes':
        columns_order = ['Unnamed: 0', 'Start Time', 'End Time', 'Trip Duration', 'Start Station', 'End Station', 'User Type', 'month', 'day_of_week', 'hour']
        print(df.iloc[start_loc:start_loc+5].reindex(columns=columns_order).to_string(index=False))
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
        
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

    