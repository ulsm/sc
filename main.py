import csv
from datetime import datetime


def get_temperatures():
    avg_tmps = None
    with open("input.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        avg_tmps = [row for row in reader]

    average_temps = {}
    for row in avg_tmps:
        date_str = row["date"]
        temp = float(row["temperature"])
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        if date in average_temps:
            average_temps[date]["sum"] += temp
            average_temps[date]["count"] += 1
        else:
            average_temps[date] = {"sum": temp, "count": 1}
    result = {}
    for date, values in average_temps.items():
        result[date.strftime("%Y-%m-%d")] = round(values["sum"] / values["count"], 2)
    average_temps = result

    max_tmps = None
    with open("input.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        max_tmps = [row for row in reader]

    max_temperature = float("-inf")
    max_date = None
    for row in max_tmps:
        temperature = float(row["temperature"])
        if temperature > max_temperature:
            max_temperature = temperature
            max_date = row["date"]
    max_temperature = {
        "max_date": max_date,
        "max_temperature": round(max_temperature, 2),
    }

    return average_temps, max_temperature


def get_average_temperatures():
    pass


def get_max_temperature():
    pass
