﻿hour = int(input("Start time (hours): "))
mins = int(input("Start minute (minutes): "))
dura = int(input("Event duration (minutes): "))
mins = mins + dura 
hour = hour + mins // 60 
mins = mins % 60 
hour = hour % 24
print(hour, ":", mins, sep='')
