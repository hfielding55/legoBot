#!/usr/bin/env pybricks-micropython

import sys
import os
try:
    import socket
except ImportError:
    import usocket as socket

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

ev3 = EV3Brick()

motorA = Motor(Port.A)
motorB = Motor(Port.B)
motorC = Motor(Port.C)
motorD = Motor(Port.D)
sensor4 = ColorSensor(Port.S4)

def handle_dengar():
    motorD.run_angle(700, 360)
    motorD.stop()
    while True:
        if sensor4.reflection() >= 15:
            motorB.stop()
            wait(1000) 
            motorB.run_angle(200, 200)
            break
        motorB.run(500)
        wait(200) 
    wait(1000)
    motorC.run_angle(200, -320)
    motorC.stop()
    wait(1000)
    motorC.run_angle(200, 320)

def handle_ig():
    motorA.run_angle(360, -475)
    motorD.run_angle(500, 360)
    motorD.stop()
    while True:
        if sensor4.reflection() >= 15:
            motorB.stop()
            wait(1000) 
            motorB.run_angle(200, 200)
            break
        motorB.run(500)
        wait(10)
    wait(1000)
    motorC.run_angle(200, -320)
    motorC.stop()
    wait(1000)
    motorC.run_angle(200, 320)
    motorA.run_angle(360, 475)

def handle_boba():
    motorA.run_angle(360, -950)
    motorD.run_angle(500, 360)
    motorD.stop()
    while True:
        if sensor4.reflection() >= 15:
            motorB.stop()
            wait(1000) 
            motorB.run_angle(200, 200)
            break
        motorB.run(500)
        wait(10)
    wait(1000)
    motorC.run_angle(200, -320)
    motorC.stop()
    wait(1000)
    motorC.run_angle(200, 320)
    motorA.run_angle(360, 950)

def handle_bossk():
    motorA.run_angle(360, -1850)
    motorD.run_angle(500, -360)
    motorD.stop()
    while True:
        if sensor4.reflection() >= 15:
            motorB.stop()
            wait(1000) 
            motorB.run_angle(200, 200)
            break
        motorB.run(500)
        wait(10)
    wait(1000)
    motorC.run_angle(200, -320)
    motorC.stop()
    wait(1000)
    motorC.run_angle(200, 320)
    motorA.run_angle(360, 1850)

def handle_lom():
    motorA.run_angle(360, -2350)
    motorD.run_angle(500, -360)
    motorD.stop()
    while True:
        if sensor4.reflection() >= 15:
            motorB.stop()
            wait(1000) 
            motorB.run_angle(200, 200)
            break
        motorB.run(500)
        wait(10)
    wait(1000)
    motorC.run_angle(200, -320)
    motorC.stop()
    wait(1000)
    motorC.run_angle(200, 320)
    motorA.run_angle(360, 2350)

def handle_zuckuss():
    motorA.run_angle(360, -2800)
    motorD.run_angle(500, -360)
    motorD.stop()
    while True:
        if sensor4.reflection() >= 4:
            motorB.stop()
            wait(1000) 
            motorB.run_angle(200, 200)
            break
        motorB.run(500)
        wait(10)
    wait(1000)
    motorC.run_angle(200, -320)
    motorC.stop()
    wait(1000)
    motorC.run_angle(200, 320)
    motorA.run_angle(360, 2800)

def start_server(port=8089):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', port))
    s.listen(1)

    while True:
        client, addr = s.accept()
        request = client.recv(1024).decode('utf-8')

        if "GET /dengar" in request:
            handle_dengar()
            response = "HTTP/1.1 200 OK\r\n\r\nOK"
        elif "GET /ig" in request:
            handle_ig()
            response = "HTTP/1.1 200 OK\r\n\r\nOK"
        elif "GET /boba" in request:
            handle_boba()
            response = "HTTP/1.1 200 OK\r\n\r\nOK"
        elif "GET /bossk" in request:
            handle_bossk()
            response = "HTTP/1.1 200 OK\r\n\r\nOK"
        elif "GET /lom" in request:
            handle_lom()
            response = "HTTP/1.1 200 OK\r\n\r\nOK"
        elif "GET /zuckuss" in request:
            handle_zuckuss()
            response = "HTTP/1.1 200 OK\r\n\r\nOK"
        else:
            # Unknown path
            response = "HTTP/1.1 404 Not Found\r\n\r\nNot Found"

        # Send the response and close the client connection
        client.send(response.encode('utf-8'))
        client.close()

        # If it was one of the recognized paths, run the command and exit
        if any(cmd in request for cmd in ["/zuckuss", "/lom", "/bossk", "/boba", "/ig", "/dengar"]):
            os.system('ps -A | grep micropython')
            os.system('ps -A | grep micropython')
            os.system('ps -A | grep micropython')
            os.system('ps -A | grep micropython')
            os.system('ps -A | grep micropython')
            os.system('ps -A | grep micropython')
            os.system('ps -A | grep micropython')
            sys.exit()  # Terminate the program

if __name__ == '__main__':
    start_server(8089)