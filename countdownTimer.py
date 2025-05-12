#Countdown Timer Program
import time
import os



duration = int(input("Set countdown duration(in seconds): "))

for i in reversed(range(1,duration + 1)):
    seconds = int(i % 60)
    minutes = int(i / 60) % 60
    hours = int(i /3600)
    time.sleep(1)
    print(f"{hours:02}: {minutes:02} :{seconds:02}")


