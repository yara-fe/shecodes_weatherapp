# Weather Project - Python Module

## Overview
This project uses Python to process csv files containing data about the weather and convert them into meaningful text-based summaries. 

**Task:** Complete the functions defined in *weather.py* based on the docstrings provided, so that each unit testing will pass when *run_tests.py* is executed.

## Functions in *weather.py*
No | Function | Description
| :---: | :---: | :--- 
1 | convert_date(iso_string) | Converts an iso date format to a string, formatted as Weekday Date Month Year
2 | convert_f_to_c(temp_in_fahrenheit) | Converts temperature in fahrenheit to degrees Celsius, rounded to 1 decimal place
3 | calculate_mean(weather_data) | Calculates the mean value from a list of numbers.
4 | load_data_from_csv(csv_file) | Reads a csv file and stores the data in a list.
5 | find_min(weather_data) | Calculates the minimum value in a list of numbers, as well as finds its position within the list.
6 | find_max(weather_data)| Calculates the maximum value in a list of numbers, as well as finds its position within the list.
7 | generate_summary(weather_data) | Outputs a summary for the given weather data, containing: <ul><li>the number of days that the data covers, </li><li>the lowest temperature and day it occurs, </li><li> the highest temperature and day it occurs, </li><li> average low temperature and high temperature for the period</li></ul>
8 | generate_daily_summary(weather_data) | Outputs a daily summary for the given weather data, containing:<ul><li>the date in Weekday Date Month Year fomat,</li><li>minimum temperature and maximum temperature for the day</li></ul>

## Project Result
- All 8 functions passed unit testing. Below is a screenshot of successful result when executing *run_tests.py*:
- ![Screenshot of test result](https://github.com/yara-fe/shecodes_weatherapp/blob/main/weatherapp_OK.png)
