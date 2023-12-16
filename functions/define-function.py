def cylinder_volume(height, radius):
    pi = 3.14159
    volume = height * pi * radius ** 2
    return volume

#print(cylinder_volume(10, 3))


def print_greeting():
    print("Hello world!")

#print_greeting()


def readable_timedelta(days):
    weeks = days // 7
    remaining_days = days % 7
    
    return f"{weeks} week(s), {remaining_days} day(s)."

print(readable_timedelta(1))