
# using time module
import time

ts = time.time()
print(ts)

file = open("mike.txt", 'w')
file.write(str(ts))
file.close()
