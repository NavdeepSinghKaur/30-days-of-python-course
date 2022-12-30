import datetime

print(datetime.datetime.now())


month = datetime.datetime.now().month

day = datetime.datetime.now().day

year = datetime.datetime.now().year

hour = datetime.datetime.now().hour

minutes = datetime.datetime.now().minute

seconds = datetime.datetime.now().second

print(f'{month}m {day}d {year}Y, {hour}H {minutes}M {seconds}S')


string_date = "5 December, 2019"

date_object = datetime.datetime.strptime(string_date, "%d %B, %Y")


today = datetime.datetime.now()

print(today - date_object)


unix = datetime.datetime(1970, 1, 1)

print(today - unix)


"""verify if something is real, to create a clock, and a lot of more things"""