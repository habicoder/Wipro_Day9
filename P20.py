#Python DateTime.tzinfo() 
import datetime

# Define a custom timezone class
class CustomTimeZone(datetime.tzinfo):
    def utcoffset(self, dt):
        return datetime.timedelta(hours=5, minutes=30)

# Create a datetime object with a custom timezone
dt_with_tz = datetime.datetime(2023, 5, 15, 13, 30, 0, tzinfo=CustomTimeZone())

# Print the datetime object with timezone
print("Datetime with Custom Timezone:", dt_with_tz)

