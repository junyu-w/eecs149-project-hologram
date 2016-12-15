import RPi.GPIO as GPIO
import time

LAYERS = [2, 3, 4, 14, 15, 18, 17, 27]
FACES = [5, 7, 8, 11, 9, 25, 10, 24]
DATA_PINS = [21, 20, 16, 26, 19, 13, 6, 12]
example = [1, 1, 1, 1, 0, 1, 1, 1]
a = [1, 0, 1, 0, 1, 0, 1, 0]
b = [0, 1, 0, 1, 0, 1, 0, 1]
c = [a, b, a, b, a, b, a, b]
d = [b, a, b, a, b, a, b, a]

e = [0, 0, 0, 0, 0, 0, 0, 0]
f = [e, e, e, e, e, e, e, e]
my_3d = [[[0]*8 for i in range(8)] for i in range(8)]

ex3d = [c, d, c, d, c, d, c, d]
def initialize():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for i in DATA_PINS + FACES + LAYERS:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.LOW)

def all_layers_off():
    for i in LAYERS:
        GPIO.output(i, GPIO.LOW)

def select_layer(layer_num):
    for i in LAYERS:
        GPIO.output(i, GPIO.LOW)
    GPIO.output(LAYERS[layer_num], GPIO.HIGH)

def write_to_register(data, face):
    for i in range(8):
        if data[i]:
            GPIO.output(DATA_PINS[i], GPIO.HIGH)
        else:
            GPIO.output(DATA_PINS[i], GPIO.LOW)
    GPIO.output(FACES[face], GPIO.HIGH)
    GPIO.output(FACES[face], GPIO.LOW)

def write_layer(data2d, layer):
    for i in range(8):
        write_to_register(data2d[i], i)

def write_3d(data3d):
    for i in range(8):
        write_layer(data3d[i], i)
        select_layer(i)
        time.sleep(0.001)
        all_layers_off()

def display_3d(data3d, t):
    while t>0:
        write_3d(data3d)
        t-=.008

def testing():
    initialize()
    display_3d(ex3d, 120)

def testing1():
    initialize()
    display_3d(my_3d, 120)

#testing()
initialize();
while (1):
   for i in range(8):
       for j in range(8):
           for k in range(8):
   	       my_3d[i][j][k] = 1;
               display_3d(my_3d, 0.2)
   	       my_3d[i][j][k] = 0;
        
    
        
