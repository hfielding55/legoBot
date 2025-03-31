Arduino code: the code has a UI for the tft screen. The screen displays three options which the user can scroll between with the left and right buttons. The user can then use the middle button to select. The Arduino will then put its output signal HIGH for a set amount of time based on the item selected.
ev3 code: The code is a small loop that runs a function when it detects a signal from its touch sensor. The touch sensor is linked to the arduino so the arduino can send signals. When a signal is detected, it reads every 50ms till the signal is LOW again. it then runs a routine which turns a certain amount before lowering and raising its crane before returning to the beginning.

Circuit: 
The circuit has a cable to an ev3 touch sensor cut open and plugged into a breadboard to trick the ev3 into thinking its a regular touch sensor.
The touch sensor
