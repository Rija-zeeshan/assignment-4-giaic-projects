import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)  # Minutes and seconds calculated
        time_format = '{:02d}:{:02d}'.format(mins, secs)  # Formatting time
        print(time_format, end='\r')  # Print on the same line
        time.sleep(1)  # Delay of 1 second
        seconds -= 1  # Decrease seconds

    print("00:00 \nTime's up!")  # Timer finished message

# ✅ User input for countdown time
total_seconds = int(input('Enter the time in seconds for countdown: '))
countdown_timer(total_seconds)  # Function call
