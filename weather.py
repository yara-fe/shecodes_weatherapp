import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """

    #create a date object with iso_string
    date_object = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")

    #convert the date_object to the a string date
    date_new = datetime.strftime(date_object, "%A %d %B %Y")

    return date_new


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    # print (type(temp_in_farenheit))

    # convert input into a float
    temp_float = float(temp_in_farenheit)

    # convert temp from F to C, round to 1 dp
    temp_c = round(((temp_float-32)*5/9),1)

    # return temp in degrees C
    return temp_c


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """

    # Initialize a list that will store the sum of the values in the list
    sum_of_list = 0

    # Convert the elements within weather_data to float
    float_weather_data = [float(i) for i in weather_data]
    
    # Get the sum of the elements
    for i in range(len(float_weather_data)):
        sum_of_list += float_weather_data[i]

    # Calculate the mean 
    mean = sum_of_list/len(float_weather_data)
    return mean

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    # Open the file and create a dictionary.
    # Key will be from the first row of the file so this is automatically skipped.
    with open(csv_file, mode="r", encoding="utf-8") as weather_file:
        csv_reader = csv.DictReader(weather_file)

        #create a list to store all rows in weather_file:
        weather_data = []
        for row in csv_reader:
            weather_data.append([row['date'], int(row['min']),int(row['max'])])
        
        return weather_data

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and its position in the list.
    """
    #check if the list is empty
    if not weather_data:
        return ()

    #convert each temperature in the list to a float
    weather_data = [float(temp) for temp in (weather_data)]
    # print(weather_data)
        
    # find the minimum in the list
    minimum = min(weather_data)

    # handle duplicates of minimum value
    # create a new list called min_positions that contains the indices of elements in weather_data, 
    # where the element is equal to the minimum value
    min_positions = [index for index, temp in enumerate(weather_data) if temp == minimum]
  
    if len(min_positions) > 1:
        #the minimum position will be the last occurence
        position = min_positions[-1]
    else:
        position = min_positions[0]

    #display the minimum value and its position
    return (minimum, position)

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and its position in the list.
    """
    # check if the list is empty
    if not weather_data:
        return ()
    
    # convert each temperature in the list to a float
    weather_data = [float(temp) for temp in (weather_data)]

    # find maximum value
    maximum = max(weather_data)
    
    # find all positions of the maximum value within the list.
    # this will handle instances where maximum value appears more than once.
    max_positions = [index for index, temp in enumerate(weather_data) if temp == maximum]
    
    #determines what position to use if there are multiple occurrences of max value
    if len(max_positions) > 1:
        position = max_positions[-1] #if more than one, use last occurrence
    else:
        position = max_positions[0]
   
    #return the maximum value and its position
    return (maximum,position)

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    """Sample Output:
    5 Day Overview
    The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021.
    The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
    The average low this week is 12.2°C.
    The average high this week is 17.8°C.    
    """
    
    # Initialize three lists that will store the dates, min temps and max temps
    dates = []
    min_temps = []
    max_temps = []

    # Get the list from the sublist
    # Add each element to their corresponding list (i.e. put all dates into the "dates" list, min temp into "min_temps", etc)
    for row in weather_data:
        dates.append(row[0])
        min_temps.append(row[1])
        max_temps.append(row[2])

    # Find the lowest temperature and it's position from the list.
    min_temp = find_min(min_temps)[0]
    min_temp_pos = find_min(min_temps)[1]
    
    # Use position to find min_date
    min_date = dates[min_temp_pos]

    # Find the highest temperature and it's position from the list.
    max_temp = find_max(max_temps)[0]
    max_temp_pos = find_max(max_temps)[1]

    # Use position to find min_date
    max_date = dates[max_temp_pos]

    # Find the average low temperature
    ave_low_temp = calculate_mean(min_temps)

    # Find the average low temperature
    ave_high_temp = calculate_mean(max_temps)
    
    summary = f"{len(weather_data)} Day Overview\n"
    summary += f"  The lowest temperature will be {format_temperature(convert_f_to_c(min_temp))}, and will occur on {convert_date(min_date)}.\n"
    summary += f"  The highest temperature will be {format_temperature(convert_f_to_c(max_temp))}, and will occur on {convert_date(max_date)}.\n"
    summary += f"  The average low this week is {format_temperature(convert_f_to_c(ave_low_temp))}.\n"
    summary += f"  The average high this week is {format_temperature(convert_f_to_c(ave_high_temp))}.\n"

    return(summary)

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # pass

    ''' Sample Output:
    ---- Friday 19 June 2020 ----
    Minimum Temperature: 8.3°C
    Maximum Temperature: 7.8°C
    '''
    
    # Initialize an empty string to store the summary
    summary = ""

    # loop over the data in the list and assign a variable to each element within the row
    for row in weather_data:
        date = convert_date(row[0]) #convert to readable date
        min_temp = format_temperature(convert_f_to_c(row[1])) #convert min temp to Celsius and add degreesC
        max_temp = format_temperature(convert_f_to_c(row[2])) #convert max temp to Celsius and add degreesC

        # Adding data to the summary
        summary += f"---- {date} ----\n"
        summary += f"  Minimum Temperature: {min_temp}\n"
        summary += f"  Maximum Temperature: {max_temp}\n\n"

    return(summary)

