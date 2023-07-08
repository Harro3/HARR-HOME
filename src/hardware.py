from sense_emu import SenseHat
# from sense_hat import SenseHat


sense = SenseHat()

def display_message(message):
    sense.show_message(message)