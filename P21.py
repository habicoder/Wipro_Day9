import datetime
import pytz

# Get the current datetime in UTC timezone
current_utc_time = datetime.datetime.now(datetime.timezone.utc)
print("Current UTC Time:", current_utc_time)

# Convert UTC time to a specific timezone (e.g., 'Asia/Kolkata')
local_timezone = pytz.timezone('Asia/Kolkata')
current_local_time = current_utc_time.astimezone(local_timezone)
print("Current Local Time (Asia/Kolkata):", current_local_time)

# List first 10 available timezones
first_10_timezones = pytz.all_timezones[:10]
print("\nAvailable Timezones:")
for timezone in first_10_timezones:
    print(timezone)

