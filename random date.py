import random
import time

def get_random_date(startDate, endDate):
    print("Printing a random date between", startDate, "and", endDate)
    random_generator = random.random()
    date_format = '%m/%d/%Y'

    starttime = time.mktime(time.strptime(startDate, date_format))
    endtime = time.mktime(time.strptime(endDate, date_format))

    randomtime = starttime + random_generator * (endtime - starttime)
    random_date = time.strftime(date_format, time. localtime(randomtime))
    return random_date
print("random date = ", get_random_date("1/4/2026", "12/31/2030"))