import serial 
import time
import codecs

#Setup for the USB relay to turn the lights on
relay = serial.Serial(
port='/dev/ttyUSB0',
baudrate=9600
)
# connects to the USB relay device over serial
relay.open

def open_relay():
    # python2 syntax 
    # relay.write('A00101A2'.decode('hex')) 
    relay.write(codecs.decode(b'A00101A2','hex'))
    print('Relay Activated')
    
def close_relay():
    # python2 syntax
    # relay.write('A00100A1'.decode('hex'))
    relay.write(codecs.decode(b'A00100A1','hex'))
    print('Relay Shut Off')

if __name__ == '__main__':
    # turns the relay on for 5 seconds
    open_relay()
    time.sleep(5)
    close_relay()
        