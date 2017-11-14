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

    print("%.2f" % y)
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

weather()
