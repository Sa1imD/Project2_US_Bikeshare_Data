#!/usr/bin/env python3

import pandas as pd



CITY_DATA = {'Chicago': 'chicago.csv', 'New York City': 'new_york_city.csv', 'Washington': 'washington.csv', 'C': 'chicago.csv', 'N': 'new_york_city.csv', 'W': 'washington.csv'}
Cities = ['Chicago', 'C', 'New York City', 'N', 'Washington', 'W']
Months = ['All', 'January', 'February', 'March', 'April', 'May', 'June']
Weekdays = ['Saturday', 'Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','All']

print('Welcome to US bikeshare :)')



def get_filters():
	
	
# Ask user choose one city.
	city = input('Please choose one city [[Chicago (c), New York City (n) or Washington (w)]]: \n').capitalize()
	
	while city not in Cities:
		city = input('Please choose one city [[Chicago (c), New York City (n) or Washington (w)]]: \n').capitalize()


# Ask user choose the month.
	month = input('Please choose one month or choose or type all for all months: \n').capitalize()
	
	while month not in Months:
		month = input('Please choose one month or choose or type all for all months: \n').capitalize()


# Ask user choose one weekday.
	weekday = input('Please choose one day or type all for all days: \n').capitalize()
	
	while weekday not in Weekdays:
		weekday = input('Please choose one day or type all for all days: \n').capitalize()
		
	return city, month, weekday

####################################################################


def load_data(city, month, weekday):

	# load data file into a dataframe
	df = pd.read_csv(CITY_DATA[city])
	
	# convert the Start Time column to datetime
	df['Start Time'] = pd.to_datetime(df['Start Time'])
	
	# extract month and day of week from Start Time to create new columns
	df['month'] = df['Start Time'].dt.month
	df['day'] = df['Start Time'].dt.day_name()
	df['hour'] = df['Start Time'].dt.hour
	
	# filter by month if applicable
	if month != 'All':
		# use the index of the months list to get the corresponding int
		month = Months.index(month)
		
		# filter by month to create the new dataframe
		df = df[df['month'] == month]
		
	# filter by day of week if applicable
	if weekday != 'All':
		# filter by day of week to create the new dataframe
		df = df[df['day'] == weekday.title()]
		
	return df



#-------------------------



def popular_times_p1(df, city):
	'''#1 Popular times of travel (i.e., occurs most often in the start time)'''

	print('\n' + '='*30 + '#1 Popular times of travel' + '='*30 + '\n')
	
	
	# 1- most common month
	
	month = df['month'].mode()[0]
	print('The popular bikeshare month for {} in: {}'.format(city, Months[month]))
	
	# 2- most common day of week
	weekday = df['day'].mode()[0]
	print('And the popular bikeshare day is: {}'.format(weekday))
	
	# 3- most common hour of day
	
	hour = df['hour'].mode()[0]
	print('And the popular bikeshare hour is: {}'.format(hour))
	

#-----------------------------------------------


def popular_stations_p2(df, city):
	
		'''#2 Popular stations and trip'''
	
		print('\n' + '='*30 + '#2 Popular stations and trip' + '='*30 + '\n')
		
		# 1- most common start station
	
		Start_Station = df['Start Station'].mode()[0]
		print('The popular bikeshare Start Station in {} is: {}'.format(city, Start_Station))
	
	
		# 2- most common end station
		End_Station = df['End Station'].mode()[0]
		print('And the popular bikeshare End Station is:', End_Station)
	
	
	# 3- most common trip from start to end (i.e., most frequent combination of start station and end station)
	
		comm_trip_s_e = df.groupby(['Start Station', 'End Station'])
		trip_s_e = comm_trip_s_e['Trip Duration'].count().idxmax()
		
		print('And the popular bikeshare trip start from {} station to {} station.'.format(trip_s_e[0], trip_s_e[1]))
	
#-----------------------------------------------


def trip_duration_p3(df, city):
	'''#3 Trip duration'''
	
	print('\n' + '='*30 + '#3 Trip duration' + '='*30 + '\n')
	
	# 1- total travel time
	t_t_t = df['Trip Duration'].sum()
	print('The total travel time for trip duration in {} is: {}'.format(city, t_t_t))
	
	# 2- average travel time
	a_t_t = df['Trip Duration'].mean()
	print('And the average travel time for trip duration is: {}'.format(a_t_t))


#--------------------------------------------------

def user_info_p4(df, city):
	'''#4 User info'''
	
	print('\n' + '='*30 + '#4 User info' + '='*30 + '\n')

	
	# 1- counts of each user type
	print('\n' + 'The counts of each user typefor {} bikeshare are:'.format(city))
	print(df['User Type'].value_counts().to_frame())
	
	# 2- counts of each gender (only available for NYC and Chicago)
	if 'Gender' in(df.columns):
		print('\n' + 'The counts of each gender for {} bikeshare are:'.format(city))
		print(df['Gender'].value_counts().to_frame())
		
	# 3- earliest, most recent, most common year of birth (only available for NYC and Chicago)
	if 'Birth Year' in(df.columns):
		print('\n' + 'The earliest, most recent, most common year of birth for {} bikeshare are:'.format(city))
		print('The earliest year of birth is: {}'.format(int(df['Birth Year'].min())))
		print('And most recent year of birth is: {}'.format(int(df['Birth Year'].max())))
		print('And most common year of birth is: {}'.format(int(df['Birth Year'].mode()[0])))
		
	print('='*80)



def raw_data(df, city):
		"""Raw data is displayed upon request by show 5 rows at time"""
	
		raw = input('\n' + 'Did you want show raws data for {city}?\n').capitalize()
		if raw != 'No':
			moreRaw = 0
			while True:
				print(df.iloc[moreRaw: moreRaw+5])
#				print(df.describe())
				moreRaw += 5
				more_raw = input('Did you want show Next 5 raws?').capitalize()
				if more_raw == 'No':
					break


def main():
		while True:
				city, month,  weekday= get_filters()
				df = load_data(city, month, weekday)
				popular_times_p1(df, city)
				popular_stations_p2(df, city)
				trip_duration_p3(df, city)
				user_info_p4(df, city)
				raw_data(df, city)

				tryAgin = input('\n'+ 'If you want try for same city or another city please type yes or no for stop.\n').capitalize()
				if tryAgin == 'No':
						break
			
			
if __name__ == "__main__":
	main()
	
			