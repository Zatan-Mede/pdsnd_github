import time
import pandas as pd
import numpy as np
from statistics import mode

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
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    citylist = ['chicago', 'new york city', 'washington']
    while True:
        city = input('Enter search city from these options; Chicago, New york city or Washington: ').lower()
        if city not in citylist:
            print('Please Enter a valid city')
            continue
        else: print('Filtering information for {}'.format(city.title()))
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    monthlist = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input('Specify any month from January to June or choose \'all\' to view all months: ').lower()
        if month not in monthlist:
            print('Please enter a valid month')
            continue
        else: print('Filtering information for {} where month is {}'.format(city.title(), month.title()))
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    daylist = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input('Specify the day of the week or select \'all\' to view every day of the week: ').lower()
        if day not in daylist:
            print('Please enter any day from Sunday to Saturday')
            continue
        else: print('Filtering information for {} where month is {} and day of the week is {}'.format(city.title(), month.title(), day.title()))
        break

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]

    if day != 'all':
        df = df[df['Day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is {}'.format(mode(df['Month'])))

    # TO DO: display the most common day of week
    print('The most common day of the week is {}'.format(mode(df['Day_of_week'])))

    # TO DO: display the most common start hour
    print('The most common hour is {}hour(s)'.format(mode(df['Start Time'].dt.hour)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most popularly used start station was {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('The most popularly used end station was {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    combination_of_stations = df['Start Station'] +' and '+ df['End Station']
    print('The most frequent combination of start and end station trip was {}'.format(combination_of_stations.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time was {}'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('The mean travel time was {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
        print(df['Gender'].value_counts())
    except KeyError:
        print('There is no information on gender for this city')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('The earliest year of birth: {}'.format(df['Birth Year'].min()))
        print('The most recent year of birth: {}'.format(df['Birth Year'].max()))
        print('The most common year of birth: {}'.format(df['Birth Year'].mode()[0]))
    except KeyError:
        print('There is no information on birth year for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """Displays data of the first five row of the filtered DafaFrame."""
    view_head = input('Do you want to see the first 5 lines of your filtered search (yes/no)? ').lower()
    if view_head != 'no':
            print(df.head())
            count_from = 0
            count_to = 5
            while True:
                next_lines = input('Do you want to view the next 5 lines?(yes/no)').lower()
                if next_lines != 'no':
                    count_from += 5
                    count_to +=5
                    print(df.iloc[count_from:count_to, :])
                else:
                    break


def sorting(df):
    """Displays a single row of data of the lowest value of a selected column."""
    sorting = input('Do you want to view data sorted by the lowest value of a column (yes/no): ').lower()
    if sorting != 'no':
        columns = ('Month', 'Birth Year', 'Trip Duration', 'End Time', 'Start Time')
        while True:
            name = input('Enter column name to sort by, from either Month, Birth Year, Trip Duration, End Time or Start Time: ').title()
            if name not in columns:
                print('Enter a valid column ')
                continue
            else: print(df.sort_values(name).iloc[0])
            break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        sorting(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
