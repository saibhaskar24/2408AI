from ppadb.client import Client
import time
import os
import cv2 as cv
import manager
import divimage


os.system('adb start-server')


adb = Client(host='localhost', port=5037)


devices = adb.devices()
device = devices[0]

if len(devices) == 0:
    print( "No devices found")
    
print("Connected devices:",devices)
print(devices)


k= 0


while True:
    image = device.screencap()
    with open(f'live.png','wb') as f:
        f.write(image)
    image = cv.imread(f"live.png")
    image = cv.resize(image,(400,900))
    image = image[328:690,28:370]
    # cv.imshow("Image",image)
    cv.imwrite("live.png",image)
    # cv.imshow("image",image)
    # cv.waitKey()
    # image = cv.imread('myimage.png')

    array = divimage.scanimage(image)
    move = manager.runa(array)
    print(array)
    print(move)


    if move['move'] == 'u':
        device.shell(f'input swipe 500 2000 500 1000 100')
    if move['move'] == 'd':
        device.shell(f'input swipe 500 1000 500 2000 100')
    if move['move'] == 'r':
        device.shell(f'input swipe 200 1000 700 1000 100')  
    if move['move'] == 'l':
        device.shell(f'input swipe 700 1000 200 1000 100') 
    if k == 20:
        break
