def convert_to_12_hour_format(hour, minute):
    if hour < 12:
        if hour == 0 :
          return f"{hour+12:02d}:{minute:02d} AM"
        return f"{hour:02d}:{minute:02d} AM"
    elif hour == 12:
        return f"{hour:02d}:{minute:02d} PM"
    else:
        return f"{hour-12:02d}:{minute:02d} PM"

# Input number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Input time in 24-hour format
    time = input().strip().split(":")
    hour = int(time[0])
    minute = int(time[1])
    
    # Convert to 12-hour format
    twelve_hour_format = convert_to_12_hour_format(hour, minute)
    
    # Output the result
    print(twelve_hour_format)
