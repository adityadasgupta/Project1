from sense_hat import SenseHat
import threading
import csv

sense = SenseHat()

black = (0,0,0)


def weather():
    threading.Timer(1800.0, weather).start()

    x = sense.temp
    z = sense.get_humidity
    a = sense.get_pressure()

    y = (x * 1.8) + 32
    update()
    write2file()
    if y<0:
        y = 0
    elif y > 255:
        y = 255

    if y < 60.0:
        colour = (int(y),int(y),255)
    else:
        y >= 60.0
        colour = (255,150 - int(y),150 - int(y))

from sense_hat import SenseHat
import threading

sense = SenseHat()

black = (0,0,0)

def weather():
    threading.Timer(1800.0, weather).start()

    x = sense.temp
    z = sense.get_humidity
    a = sense.get_pressure()

    y = (x * 1.8) + 32

    if y<0:
        y = 0
    elif y > 255:
        y = 255

    if y < 60.0:
        colour = (int(y),int(y),255)
    else:
        y >= 60.0
        colour = (255,150 - int(y),150 - int(y))

from sense_hat import SenseHat
import threading

sense = SenseHat()

black = (0,0,0)

def weather():
    threading.Timer(1800.0, weather).start()

    x = sense.temp
    z = sense.get_humidity
    a = sense.get_pressure()

    y = (x * 1.8) + 32

    if y<0:
        y = 0
    elif y > 255:
        y = 255

    if y < 60.0:
        colour = (int(y),int(y),255)
    else:
        y >= 60.0
        colour = (255,150 - int(y),150 - int(y))

    print("Temperature: " + "%.2f" % y)
    print("Humidity: " + "%.2f" % z)
    print("Pressure: " + "%.2f" % a)
    string_value1 = str("%.2f" % y) + 'F'
    sense.show_message(string_value1, text_colour=colour, back_colour=black, scroll_speed=0.05)

    if y < 0.0:
        sense.show_message('Stay Inside!', text_colour=(0,0,255), back_colour=black, scroll_speed=0.05)
    elif y < 40.0:    
        sense.show_message('Winter Clothes Recommended!', text_colour=colour, back_colour=black, scroll_speed=0.05)
    elif y < 60.0:
        sense.show_message('Jacket is Recomended!', text_colour=colour, back_colour=black, scroll_speed=0.05)
    elif y < 100.0:
        sense.show_message('Enjoy the Warmth!', text_colour=colour, back_colour=black, scroll_speed=0.05)
    else:
        y > 100.0
        sense.show_message('Stay Inside!', text_colour=colour, back_colour=black, scroll_speed=0.05)
#weather()
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
