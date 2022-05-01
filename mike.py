import time

localtime = time.asctime( time.localtime(time.time()) )

execTime = localtime

file = open("mike.txt", 'w')
file.write("Time of run : ")
file.write(str(execTime))
file.close()
