import time
time = time.time()

ts = time

file = open("mike.txt", 'w')
file.write("Time x : ")
file.write(str(ts))
file.close()
