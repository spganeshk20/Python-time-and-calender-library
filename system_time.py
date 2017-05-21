#usr/bin/python2.7

'''
Author name: Ganesh

About the module:  
This is the 'current_system_time.py' module, and it provides you the lot of front end function to make your work ease interms of current system time and calender. For detail understanding about the usage of this library.'''
# Important: Go through read me file

import datetime
import calendar

#calender
def calender_disp(year, month):		#pass two input arguments to calender_disp function (year, month) whereas month starts from 1 to 12
	cal = calendar.month(year, month)
	return cal

#return current system date and time
def date_time_all():
	current_date_time_raw=datetime.datetime.now()
	current_date_time=current_date_time_raw.strftime('%Y-%m-%d %H:%M:%S')
	return (current_date_time)

#return current system date
def date_y_m_d():
	today_date_raw=datetime.datetime.now()
	today_date=today_date_raw.strftime('%Y-%m-%d')
	return (today_date)

#return the today date interms of number
def date_d():
	today_date_raw=datetime.datetime.now()
	today_date=today_date_raw.strftime('%d')
	return (today_date)

#return the present month interms of number
def month_m():
	present_month_raw=datetime.datetime.now()
	present_month=present_month_raw.strftime('%m')
	return (present_month)

#return the present year interms of number
def year_y():
	present_year_raw=datetime.datetime.now()
	present_year=present_year_raw.strftime('%Y')
	return (present_year)


''' Display the month and day interms of characters functions'''
 
#return the today day interms of characters
def day_word():
	today_day_word_raw=datetime.datetime.now()
	today_day_word=today_day_word_raw.strftime('%A')
	return (today_day_word)

#return the current month interms of characters
def month_word():
	current_month_word_raw=datetime.datetime.now()
	current_month_word=current_month_word_raw.strftime('%B')
	return (current_month_word)

'''12 and 24 time format functions'''
 
#return the current system time in 24 hr format (Hour-Minutes-Seconds)
def time_24():
	current_time_raw=datetime.datetime.now()
	current_time=current_time_raw.strftime('%H:%M:%S')
	return (current_time)

#return the current system time in 24 hr format (Hour-Minutes)
def time_24_h_m():
	current_time_raw_h_m=datetime.datetime.now()
	current_time_h_m=current_time_raw_h_m.strftime('%H:%M')
	return (current_time_h_m)


#12hour time-format
#return the current system time in 12 hr format (Hour-Minutes-Seconds AM/PM)
def time_12():
	current_time_raw=datetime.datetime.now()
	current_time=current_time_raw.strftime("%I:%M:%S %p")
	return (current_time)

#return the current system time in 12 hr format (Hour-Minutes AM/PM)
def time_12_h_m():
	current_time_raw_h_m=datetime.datetime.now()
	current_time_h_m=current_time_raw_h_m.strftime("%I:%M %p")
	return (current_time_h_m)

#return the current system time in 12 hr format (Hour-Minutes-Seconds)
def time_12_h_m_s():
	current_time_raw_h_m_s=datetime.datetime.now()
	current_time_h_m_s=current_time_raw_h_m_s.strftime("%I:%M:%S")
	return (current_time_h_m_s)

#return the current system time status as (AM/PM)
def time_12_am():
	current_time_raw_am_pm=datetime.datetime.now()
	current_time_am_pm=current_time_raw_am_pm.strftime("%p")
	return (current_time_am_pm)
