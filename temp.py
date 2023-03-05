#Monitor CPU Temperature
#By Andrzej Dawiec
import time

while True:
    with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
        temp = int(f.read()) / 1000.0
    print(f'temp = {temp:.1f} °C')
    time.sleep(5)
