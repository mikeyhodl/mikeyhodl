import time
time = time.time()

ts = time

file = open("mike.txt", 'w')
file.write("Time of run (...) : ")
file.write(str(ts))
file.close()
