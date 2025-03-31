Arduino code: the code has a UI for the tft screen. The screen displays three options which the user can scroll between with the left and right buttons. The user can then use the middle button to select. The Arduino will then put its output signal HIGH for a set amount of time based on the item selected.

ev3 code: The code is a small loop that runs a function when it detects a signal from its touch sensor. The touch sensor is linked to the arduino so the arduino can send signals. When a signal is detected, it reads every 50ms till the signal is LOW again. it then runs a routine which turns a certain amount before lowering and raising its crane before returning to the beginning.

Circuit: 

The circuit went through various stages of development. I first found a website[1] that gave a description of another way to interface. I used this design to begin experimenting with the different wires as I was still unsure of each ones purpose. I cut open the cable and isolated the six cables in on a breadboard. I found the power(green) and 5v ground(red) could be used to power the circuit to avoid having the arduino connected to any external sources.
We have found a development for the ev3 named ev3dev that lets you program micropython onto the ev3 and have much finer control over everything, we found this was the best version[3]. It needs to be flashed onto a microSD and inserted into the ev3. We used the recommended software, Balena Etcher, however found we needed an older version of it. We found 1.6.0 was a viable option, found here[4].
I attempted to create a mock circuit, albiet missing some of the parts, based from a better design I found here[2]. I found that we could get the arduino to control the ev3 in its scratch-like development mode found here[5]. This is because ev3dev debugs before it runs the program, one of its processes is to ensure it detects the right inputs and outputs in the right ports and it could tell there wasn't a touch sensor where the arduino was connected.
We solved this by connecting an ev3 touch sensor to the breadboard and allowing the circuit to intercept signals where it wants to. I found this website[6], which gave a much better explanation of the cables:
Blue: serial data
Yellow: serial clock
Green: power
Red: ground - using this as the ground creates a circuit of 5v
Black: ground - using this as the ground creates a circuit of 3.3v
White: analog
By adding



wesbites:

[1] https://www.dexterindustries.com/Arduberry/example-projects-with-arduberry-and-raspberry-pi/connecting-ev3-arduino/
[2] https://makezine.com/projects/hacking-the-lego-ev3-build-your-own-object-sensor-eyes/
[3] https://www.ev3dev.org/news/2018/06/14/ev3dev-stretch/
[4] https://etcher.en.uptodown.com/windows/download/3970628
[5] https://education.lego.com/en-gb/downloads/mindstorms-ev3/software/
[6] https://www.informit.com/articles/article.aspx?p=2454873
