import time
import pandas as pd
import numpy as np

# CITY DATA FILES
CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

# CAPTURES USER PREFERNECES
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city_input = input('Please enter your desired city, either Chicago, New York City, or Washington: ')
        city = city_input.title()
        if ( city=='Chicago' or city=='New York City' or city=='Washington'):
            print('  --> Great, \'{}\' it is!'.format(city))
            break
        else:
            print('  --> \'{}\' is an invalid entry, please try again.'.format(city_input))
            continue


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month_input = input('Please enter your desired month, either January, February, March, April, May, June, or all: ')
        month = month_input.title()
        if ( month=='January' or month=='February' or month=='March' or month=='April' or month=='May' or month=='June' or month=='All'):
            print('  --> Great, \'{}\' it is!'.format(month))
            break
        else:
            print('  --> \'{}\' is an invalid entry, please try again.'.format(month_input))
            continue


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day_input = input('Please enter your desired day, either Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all: ')
        day = day_input.title()
        if ( day=='Monday' or day=='Tuesday' or day=='Wednesday' or day=='Thursday' or day=='Friday' or day=='Saturday' or day=='Sunday' or day=='All'):
            print('  --> Great, \'{}\' it is!'.format(day))
            break
        else:
            print('  --> \'{}\' is an invalid entry, please try again.'.format(day_input))
            continue

    print('-'*40)
    return city, month, day

# LOADS CITY DATA AND APPROPRIATE TIME FRAMES
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
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'All':
        df = df[df['day_of_week'] == day.title()]

    return df

# CALCS TIME STATISTICS
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('Calculating The Most Frequent Times of Travel...')

    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print("The month common month is {}".format(common_month))

    # TO DO: display the most common day of week
    df['week_day'] = df['Start Time'].dt.weekday
    common_day = df['week_day'].mode()[0]
    print("The month common week day is {}".format(common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("The month common start hour is {}".format(common_hour))

    print("Note: This took %s seconds." % (time.time() - start_time))
    print('-'*40)

# CALCS STATION INFORMATION
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('Calculating The Most Popular Stations and Trip...')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The month common start station is {}".format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The month common end station is {}".format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['common_trip'] = df['Start Station'] + " TO " + df['End Station']
    common_trip = df['common_trip'].mode()[0]
    print("The most common trip is {}".format(common_trip))

    print("Note: This took %s seconds." % (time.time() - start_time))
    print('-'*40)

# CALCS TRIP DURATIONS
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('Calculating Trip Duration...')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("The total travel time is {}".format(total_travel_time))



    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("The mean travel time is {}".format(mean_travel_time))

    print("Note: This took %s seconds." % (time.time() - start_time))
    print('-'*40)

# DISPLAYS USER INFORMATION
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('Calculating User Stats...')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_types = df['Gender'].value_counts()
        print(gender_types)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        first_birthday = int(df['Birth Year'].min())
        print("The earliest birth year is {}".format(first_birthday))
        last_birthday = int(df['Birth Year'].max())
        print("The most recent birth year is {}".format(last_birthday))
        common_birthday = int(df['Birth Year'].mode())
        print("The most common birth year is {}".format(common_birthday))

    print("Note: This took %s seconds." % (time.time() - start_time))
    print('-'*40)

# DISPLAYS RECORD LEVEL INFORMATION TO REVIEW
def record_check(df):
    record_inquiry = input('Would you like see individual records?  Please type \'Yes\' to view: ')
    if record_inquiry.title() == 'Yes':
        try:
            print(df.size)
            for x in range(df.size):
                print(df[x:x+5])
                continue_inquiry = input('Would you like to see more?  Please type \'y\' to continue: ')
                if continue_inquiry.lower() == 'y':
                    continue
                else:
                    break
        except:
            print("That's all folks!")
    else:
        return

# MAIN PROGRAM
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        record_check(df)
        restart = input('\nWould you like to run again? Enter yes or no: ')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
