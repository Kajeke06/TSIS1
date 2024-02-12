def day_of_week():
    return 3

def day_name(day_number):
    day_names = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
    return day_names.get(day_number, "Invalid Day")

def description_of_yesterday(day_name):
    return "The day before " + day_name

def description_of_today(day_name):
    return day_name

def description_of_tomorrow(day_name):
    return "The day after " + day_name

day_number = day_of_week()
day_name = day_name(day_number)

print("Yesterday:", description_of_yesterday(day_name))
print("Today:", description_of_today(day_name))
print("Tomorrow:", description_of_tomorrow(day_name))