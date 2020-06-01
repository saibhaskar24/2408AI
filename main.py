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
    print( "No devices found")
    
print("Connected devices:",devices)
print(devices)

image = device.screencap()
with open(f'screen.png','wb') as f:
    f.write(image)
image = cv.imread(f"screen.png")
ge = cv.imread('screen.png')
image = cv.resize(image,(400,900))
image = image[320:600,20:380]
cv.imwrite("screen.png",image)






# move = manager.runa()
# if move['move'] == 'u':
#     device.shell(f'input swipe 500 2000 500 1000 100')
# if move['move'] == 'd':
#     device.shell(f'input swipe 500 1000 500 2000 100')
# if move['move'] == 'l':
#     device.shell(f'input swipe 200 1000 700 1000 100')  //corr
# if move['move'] == 'r':
#     device.shell(f'input swipe 700 1000 200 1000 100')  //corr
