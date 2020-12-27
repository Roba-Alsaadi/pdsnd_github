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

    """

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Would you like to see data for Chicago, New York City or Washington? ").lower().strip()
    while city not in ["chicago" , "new york city" , "washington"]:
        city = input("invalid city name! please enter a valid city name:").lower().strip()

    # TO DO: get user input for month ( january, february, ... , june)
    month = input("Which month? January, February, March, April, May, June or all.").lower().strip()
    while month not in ["january", "february", "march", "april", "may", "june", "all"]:
        month = input("invalid month name! please enter a valid month name:").lower().strip()

    # TO DO: get user input for day of week ( monday, tuesday, ... sunday)
    day = input("Which day of the week? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or all.").lower().strip()
    while day not in ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"]:
        day = input("invalid day name! please enter a valid day name:").lower().strip()


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

    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["End Time"] = pd.to_datetime(df["End Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()
    df["hour"] = df["Start Time"].dt.hour

    #Filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df["month"].mode()[0]


    # TO DO: display the most common day of week
    popular_day_of_week = df["day_of_week"].mode()[0]

    # TO DO: display the most common start hour
    popular_hour = df["Start Time"].mode()[0]

    print("the most common month is {} and the most common day of week is {} and the most common start hour is {}".format(popular_month, popular_day_of_week, popular_hour))




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df["Start Station"].mode()[0]


    # TO DO: display most commonly used end station
    popular_end_station = df["End Station"].mode()[0]


    # TO DO: display most frequent combination of start station and end station trip
    df["popular combination"] = df["Start Station"] + " TO " + df["End Station"].mode()[0]


    print("the most common start station is {} and the most common end station is {}".format(popular_start_station, popular_end_station))
    print("the most common trip is:",  df["popular combination"])






    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df ["Trip Duration"].sum()


    # TO DO: display mean travel time
    mean_travel_time = df ["Trip Duration"].mean()

    print("the total travel time is :", total_travel_time)
    print("the mean travel time is:", mean_travel_time)




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_counts = df["User Type"].value_counts()
    print(user_types_counts)


    # TO DO: Display counts of gender
    try:
        gender_counts = df["Gender"].value_counts()
        print(gender_counts)
    except:
        print("no gender data")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df["Birth Year"].min()
        recent_birth_year = df["Birth Year"].max()
        popular_birth_year = df["Birth Year"].mode()[0]
        print("earliest birth year is:", earliest_birth_year)
        print("recent_birth_year:", recent_birth_year)
        print("mos common year is:",popular_birth_year)
    except:
        print("no year of birth data")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #Display row data
        row_data = input("Would you like to see the row data?").lower().strip()
        start_row = 0
        end_row = 5
        while(row_data == "yes"):
            rows = df[start_row:end_row]
            print(rows)
            start_row += 5
            end_row += 5
            row_data = input("Would you like to see more row data?").lower().strip()

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        #restart the program

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
