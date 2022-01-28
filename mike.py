from datetime import datetime
import pytz

sasa = datetime.now()
# sleep(1)
# current_time = sasa.strftime("%H:%M:%S")
# print("The time is", current_time)

# sleep(1)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S", t)
# print("The time is", current_time)

# sleep(1)
# tz_NY = pytz.timezone('America/New_York') 
# datetime_NY = datetime.now(tz_NY)
# print("NY time:", datetime_NY.strftime("%H:%M:%S"))

KenyaTime = pytz.timezone('Africa/Nairobi')
datetime_Kenya = datetime.now(KenyaTime)

dafa = datetime_Kenya.strftime("%H:%M:%S")

print("Kenyan time:", datetime_Kenya.strftime("%H:%M:%S"))




file = open("mike.txt", 'w')
file.write("Kenyan Time is: ")
file.write(str(dafa))
file.close()
