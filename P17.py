#python time class
import datetime

# Get the current time
current_time = datetime.datetime.now().time()
print("Current Time:", current_time)

# Create a specific time
specific_time = datetime.time(hour=9, minute=15, second=30)
print("Specific Time:", specific_time)
