def main():
    time = 0
    day_count = 0
    clock_advance(time)
    if time == 24 or time == 48 or time == 72 or time == 96 or time == 120 or time == 144:
            day_count += 1
            if day_count == 1:
                print("1 day has passed")
            else:
                print(f"{day_count} days have passed")
    
    
def clock_advance(time):
    time += 1
    if time == 1:
        print("1 hour has passed")
    else:
        print(f"{time} hours have passed")
main()