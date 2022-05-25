import datetime

WEEKDAY_INIT_HOUR_1 = datetime.datetime.strptime('00:01', '%H:%M')
WEEKDAY_ENDING_HOUR_1 = datetime.datetime.strptime('09:00', '%H:%M')
WEEKDAY_INIT_HOUR_2 = datetime.datetime.strptime('09:01', '%H:%M')
WEEKDAY_ENDING_HOUR_2 = datetime.datetime.strptime('18:00', '%H:%M')
WEEKDAY_INIT_HOUR_3 = datetime.datetime.strptime('18:01', '%H:%M')
WEEKDAY_ENDING_HOUR_3 = datetime.datetime.strptime('00:00', '%H:%M')

WEEKDAY_PAYMENT_1 = 25
WEEKDAY_PAYMENT_1_SEC = WEEKDAY_PAYMENT_1 / (60 * 60)
WEEKDAY_PAYMENT_2 = 15
WEEKDAY_PAYMENT_2_SEC = WEEKDAY_PAYMENT_2 / (60 * 60)
WEEKDAY_PAYMENT_3 = 20
WEEKDAY_PAYMENT_3_SEC = WEEKDAY_PAYMENT_2 / (60 * 60)

WEEKEND_INIT_HOUR_1 = datetime.datetime.strptime('00:01', '%H:%M')
WEEKEND_ENDING_HOUR_1 = datetime.datetime.strptime('09:00', '%H:%M')
WEEKEND_INIT_HOUR_2 = datetime.datetime.strptime('09:01', '%H:%M')
WEEKEND_ENDING_HOUR_2 = datetime.datetime.strptime('18:00', '%H:%M')
WEEKEND_INIT_HOUR_3 = datetime.datetime.strptime('18:01', '%H:%M')
WEEKEND_ENDING_HOUR_3 = datetime.datetime.strptime('00:00', '%H:%M')

WEEKEND_PAYMENT_1 = 30
WEEKEND_PAYMENT_1_SEC = WEEKEND_PAYMENT_1 / (60 * 60)
WEEKEND_PAYMENT_2 = 20
WEEKEND_PAYMENT_2_SEC = WEEKEND_PAYMENT_2 / (60 * 60)
WEEKEND_PAYMENT_3 = 25
WEEKEND_PAYMENT_3_SEC = WEEKEND_PAYMENT_3 / (60 * 60)

def main(input_file = "input.txt"):
    """
    Takes a file with the names of the employees and their schedule and prints the corresponding payment
    """
    with open(input_file, "r") as f:
        for count, line in enumerate(f):
            if line != '\n':
                line = line.replace('\n','')
                employee = schedule = None
                try:
                    employee,schedule = line.split('=')
                    schedule = schedule.split(',')
                except:
                    raise Exception("Format error in input file in line %s " % count)
                payment = 0
                for day_hour in schedule:
                    if len(day_hour) < 3:
                        raise Exception("Format error in Schedule in line %s" % count)
                    day = day_hour[:2]
                    hour = day_hour[2:]
                    init_hour = ending_hour = None
                    try:
                        init_hour, ending_hour = hour.split('-')
                    except:
                        raise Exception("Format error in Schedule in line %s " % count)
                    payment += calculate_payment(init_hour, ending_hour, day, count)
                print("The amount to pay %s is: %s USD" % (employee, payment))

def calculate_payment(init_hour, ending_hour, day, count):
    """
    Calculate payment based on day, hour, and time worked
    It is calculated by checking how much time is worked in each time slot
    """
    payment = 0
    init_hour_datetime = ending_hour_datetime = None
    try:
        init_hour_datetime = datetime.datetime.strptime(init_hour, '%H:%M')
        ending_hour_datetime = datetime.datetime.strptime(ending_hour, '%H:%M')
    except:
        raise Exception("Format error in time in line %s " % count)
    if init_hour_datetime >= ending_hour_datetime:
        raise Exception("Ending Hour grater or equal than Initial Hour in line %s" % count)
    if day in ['MO', 'TU', 'WE', 'TH', 'FR']:
        if WEEKDAY_INIT_HOUR_1 <= init_hour_datetime < WEEKDAY_ENDING_HOUR_1:
            worked_time = min(WEEKDAY_ENDING_HOUR_1, ending_hour_datetime) - init_hour_datetime
            payment += WEEKDAY_PAYMENT_1_SEC * worked_time.total_seconds()
        if ((WEEKDAY_INIT_HOUR_2 <= init_hour_datetime < WEEKDAY_ENDING_HOUR_2) or 
            (WEEKDAY_INIT_HOUR_2 < ending_hour_datetime <= WEEKDAY_ENDING_HOUR_2)):
            worked_time = min(WEEKDAY_ENDING_HOUR_2, ending_hour_datetime) - max(WEEKDAY_INIT_HOUR_2, init_hour_datetime)
            payment += WEEKDAY_PAYMENT_2_SEC * worked_time.total_seconds()
        if WEEKDAY_INIT_HOUR_3 <= init_hour_datetime or WEEKDAY_INIT_HOUR_3 <= ending_hour_datetime:
            worked_time = ending_hour_datetime - max(WEEKDAY_INIT_HOUR_3, init_hour_datetime)
            payment += WEEKDAY_PAYMENT_2_SEC * worked_time.total_seconds()
    elif day in ['SA', 'SU']:
        if WEEKEND_INIT_HOUR_1 <= init_hour_datetime < WEEKEND_ENDING_HOUR_1:
            worked_time = min(WEEKEND_ENDING_HOUR_1, ending_hour_datetime) - init_hour_datetime
            payment += WEEKEND_PAYMENT_1_SEC * worked_time.total_seconds()
        if ((WEEKEND_INIT_HOUR_2 <= init_hour_datetime < WEEKEND_ENDING_HOUR_2)
            or (WEEKEND_INIT_HOUR_2 < ending_hour_datetime <= WEEKEND_ENDING_HOUR_2)):
            worked_time = min(WEEKEND_ENDING_HOUR_2, ending_hour_datetime) - max(WEEKEND_INIT_HOUR_2, init_hour_datetime)
            payment += WEEKEND_PAYMENT_2_SEC * worked_time.total_seconds()
        if WEEKEND_INIT_HOUR_3 <= init_hour_datetime or WEEKEND_INIT_HOUR_3 <= ending_hour_datetime:
            worked_time = ending_hour_datetime - max(WEEKEND_INIT_HOUR_3, init_hour_datetime)
            payment += WEEKEND_PAYMENT_3_SEC * worked_time.total_seconds()
    else:
        raise Exception("Wrong format in Day value in line %s" % count)
    return payment

main()