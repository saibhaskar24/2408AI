from ppadb.client import Client
import time
import os
import cv2 as cv
import manager
os.system('adb start-server')


adb = Client(host='localhost', port=5037)


devices = adb.devices()
device = devices[0]

if len(devices) == 0:
    # print("No devices found")
    print( "No devices found")
    
print("Connected devices:",devices)
print(devices)

image = device.screencap()
with open(f'screen.png','wb') as f:
    f.write(image)
image = cv.imread(f"screen.png")







move = manager.runa()
if move['move'] == 'u':
    device.shell(f'input swipe 400 400 100 100 2000')
if move['move'] == 'd':
    device.shell(f'input swipe 400 400 100 100 2000')
if move['move'] == 'l':
    device.shell(f'input swipe 400 400 100 100 2000')
if move['move'] == 'r':
    device.shell(f'input swipe 400 400 100 100 2000')
