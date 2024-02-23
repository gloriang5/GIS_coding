# Create a program to calculate the number of days a project is based on two dates entered. The project might be
# anything from 1 day to more than 1 year in length. (Use of datetime library encouraged.)

from datetime import datetime

def calc_project_duration(start_date, end_date):
    #convert data string to datetime object
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    #calculate the difference between the two dates
    duration = end - start

    num_day = duration.days

    return num_day


start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

project_duration = calc_project_duration(start_date, end_date)
print("The project duration is {} days.".format(project_duration))


