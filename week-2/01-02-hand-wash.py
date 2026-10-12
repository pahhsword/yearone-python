TIME_TAKEN = 21
DAY_PER_MONTH = 30

def wash_hands(times_per_day, months):
    i_seconds = TIME_TAKEN * times_per_day * DAY_PER_MONTH * months

    i_minutes = i_seconds // 60
    i_seconds = i_seconds % 60
    return f"{i_minutes} minutes, {i_seconds} seconds"

print(wash_hands(8,7))
print(wash_hands(0,0))
print(wash_hands(7,9))