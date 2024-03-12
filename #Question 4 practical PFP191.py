from datetime import datetime, time

def read_temperatures(filename):
    daily_temperatures = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            measurement_time = datetime.strptime(lines[i].strip(), "%d-%m-%Y %H:%M:%S")
            temperature = float(lines[i+1].strip())
            date = measurement_time.date()
            if date not in daily_temperatures:
                daily_temperatures[date] = []
            daily_temperatures[date].append((measurement_time, temperature))
            i += 2
    return daily_temperatures

def calculate_average_temperature(temperatures):
    total_daily_temperature = 0
    count = 0
    for temp in temperatures:
        total_daily_temperature += temp[1]
        count += 1
    return round(total_daily_temperature / count, 3)

def calculate_average_temperature_range(temperatures, start_time, end_time):
    total_temperature = 0
    count = 0
    for temp in temperatures:
        if start_time <= temp[0].time() <= end_time:
            total_temperature += temp[1]
            count += 1
    if count == 0:
        return 0
    return round(total_temperature / count, 3)

def main():
    filename = "temp.txt"
    daily_temperatures = read_temperatures(filename)
    for date, temps in daily_temperatures.items():
        print("Date:", date.strftime("%d-%m-%Y"))
        print("Average Daily Temperature:", calculate_average_temperature(temps))
        print("Average Temperature from 5:00 to 15:59:", calculate_average_temperature_range(temps, time(5, 0), time(15, 59, 59)))
        print("Average Temperature from 16:00 to 21:59:", calculate_average_temperature_range(temps, time(16, 0), time(21, 59, 59)))
        print()

if __name__ == "__main__":
    main()
