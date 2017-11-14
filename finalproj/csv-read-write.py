import sense_hat from SenseHat
import csv
import time
"""with open('proj.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        print row"""
def update() :
    sense = sensehat()
    temp = sense.get_temperature()
    pressure = sense.get_pressure()
    hum = sense.get_humidity()
    update_list = [temp,pressure,hum]
    return update_list
def write2file() :
    with open('proj.csv', 'wb') as csvfile :
        writer = csv.writer(csvfile,quoting = csv.QUOTE_ALL)
        new_list = update()
        writer = writerow(new_list)
