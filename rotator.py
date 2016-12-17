# import external modules
import RPi.GPIO as GPIO
import time
from scipy.ndimage.interpolation import rotate

# import data structures
import shapes

# default layer pings
LAYERS = [2, 3, 4, 14, 15, 18, 17, 27]
FACES = [5, 7, 8, 11, 9, 25, 10, 24]
DATA_PINS = [21, 20, 16, 26, 19, 13, 6, 12]
example = [1, 1, 1, 1, 0, 1, 1, 1]
a = [1, 0, 1, 0, 1, 0, 1, 0]
b = [0, 1, 0, 1, 0, 1, 0, 1]
c = [a, b, a, b, a, b, a, b]
d = [b, a, b, a, b, a, b, a]

s = [\
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0]]
wall = [s for i in range(8)]
ex3d = [c, d, c, d, c, d, c, d]

# data_structure import
line, current_shape_num = shapes.next_shape(3)

'''
initialize LED cube
'''
def initialize_cube():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for i in DATA_PINS + FACES + LAYERS:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.LOW)
    print "cube initialized"
    return line

'''
turn off lights at all layers
'''
def all_layers_off():
    for i in LAYERS:
        GPIO.output(i, GPIO.LOW)

'''
turn on lights at a specific layer
'''
def select_layer(layer_num):
    for i in LAYERS:
        GPIO.output(i, GPIO.LOW)
    GPIO.output(LAYERS[layer_num], GPIO.HIGH)

'''
write to each face (vertical LED layer) register, then 
select a layer to display the layer
'''
def write_to_register(data, face):
    for i in range(8):
        if data[i]:
            GPIO.output(DATA_PINS[i], GPIO.HIGH)
        else:
            GPIO.output(DATA_PINS[i], GPIO.LOW)
    GPIO.output(FACES[face], GPIO.HIGH)
    GPIO.output(FACES[face], GPIO.LOW)

'''
write a 2d object
'''
def write_layer(data2d, layer):
    for i in range(8):
        write_to_register(data2d[i], i)

'''
write a 3d object through displaying each layer for 0.001 seconds
'''
def write_3d(data3d):
    for i in range(8):
        write_layer(data3d[i], i)
        select_layer(i)
        time.sleep(0.001)
        all_layers_off()

'''
display a 3d object for t/0.008 times
'''
def display_3d(data3d, t):
    while t>0:
        write_3d(data3d)
        t-=.008

'''
display 3d rotation
'''
def display_3d_rot(data3d, speed, direction):
    rotational_direction = 1
    if direction <= 0:
        rotational_direction = -1
    if speed < 100:
        speed = 100
    step = int(((speed-100) * 23 / 300)) + 2
    for j in range(0, 360, step):
		to_display = []
		for i in range(8):
			to_display.append(rotate(data3d[i], rotational_direction*j, reshape=False))
		display_3d(to_display, float(2)/360)

'''
change to the next shape to display
'''
def change_shape():
    global line, current_shape_num
    line, current_shape_num = shapes.next_shape(current_shape_num)
    return line

'''
display special effect
'''
def explosion():
    lst = [shapes.s0, shapes.s1, shapes.s2, shapes.s3, shapes.s4, shapes.s3, shapes.s2, shapes.s1]
    lst = lst*4
    for i in lst:
        display_3d(i, .05)


    
		



        
    
        
