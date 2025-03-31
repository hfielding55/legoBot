Arduino code: the code has a UI for the tft screen. The screen displays three options which the user can scroll between with the left and right buttons. The user can then use the middle button to select. The Arduino will then put its output signal HIGH for a set amount of time based on the item selected.

ev3 code: The code is a small loop that runs a function when it detects a signal from its touch sensor. The touch sensor is linked to the arduino so the arduino can send signals. When a signal is detected, it reads every 50ms till the signal is LOW again. it then runs a routine which turns a certain amount before lowering and raising its crane before returning to the beginning. We found this website[10] that showed us how to control the motors using micropython.

Circuit: 

The circuit went through various stages of development. I first found a website[1] that gave a description of another way to interface. I used this design to begin experimenting with the different wires as I was still unsure of each ones purpose. I cut open the cable and isolated the six cables in on a breadboard. I found the power(green) and 5v ground(red) could be used to power the circuit to avoid having the arduino connected to any external sources.
<br/>We have found a development for the ev3 named ev3dev that lets you program micropython onto the ev3 and have much finer control over everything, we found this was the best version[3]. It needs to be flashed onto a microSD and inserted into the ev3. We used the recommended software, Balena Etcher, however found we needed an older version of it. We found 1.6.0 was a viable option, found here[4].
<br/>I attempted to create a mock circuit, albiet missing some of the parts, based from a better design I found here[2]. I found that we could get the arduino to control the ev3 in its scratch-like development mode found here[5]. This is because ev3dev debugs before it runs the program, one of its processes is to ensure it detects the right inputs and outputs in the right ports and it could tell there wasn't a touch sensor where the arduino was connected.
<br/>We solved this by connecting an ev3 touch sensor to the breadboard and allowing the circuit to intercept signals where it wants to. I found this website[6], which gave a much better explanation of the cables:
<br/>Blue: serial data
<br/>Yellow: serial clock
<br/>Green: power
<br/>Red: ground - using this as the ground creates a circuit of 5v
<br/>Black: ground - using this as the ground creates a circuit of 3.3v
<br/>White: analog

By adding a diode in the blue serial cable, allowing signals to go from the touch sensor to the ev3 but not the other way, we were able to make the ev3 detect the touch sensor correctly and also take signals from the Arduino. The diode also stops the arduino signals from travelling to the touch sensor instead of the ev3.

The TFT screen inputs setup can be found here[7], for arduino uno you'll need to scroll quite far down.
<br/> The full circuit diagram can be found in "circuit.png" as well as the component list in "components.txt" in the same folder as this file.

TO USE:
<br/>1. Ensure visual studio code[8], balena etcher 1.6.0[4] and the arduino IDE[9] are installed and setup.
<br/>2. Build circuit according to specifications shown in circuit.png and components.txt and connect arduino to shown ports.
<br/>3. Extract "aruinoCode.zip" and open in the arduino IDE. Connect computer to the Arduino and upload the program.
<br/>4. Download "ev3dev-stretch" file from this website[3], then flash to microSD card using balena etcher.
<br/>5. Insert microSD into ev3 brick and turn on
<br/>6. Extract and open "micropython.zip" in visual studio code
<br/>7. In visual studio code, go to "view" at the top and selcet "Extensions". Search for an install "LEGO® MINDSTORMS® EV3 MicroPython"
<br/>8. Connect ev3 to computer using its USB Mini port. In the bottom of the explorer tab there should be a section called "EV3 DEVICE BROWSER"
<br/>9. Open the device browser menu and select "Click to connect to a device" and the ev3 brick should appear as an open. Select it.
<br/>10. Run the program to upload it to the ev3, it will crash immediatly but that is expected.
<br/>11. Disconnect ev3 brick from computer and build lego crane following (INSERT LEGO INSTRUCTION FILE NAME)
<br/>12. Ensure cable to the breadboard is connected in port 1 of the ev3 brick.
<br/>13. Navigate to file browser on the ev3 and find the name of the project. Open it and run "main.py".
<br/>14. Everything should be running correctly now


wesbites:
<br/>[1] https://www.dexterindustries.com/Arduberry/example-projects-with-arduberry-and-raspberry-pi/connecting-ev3-arduino/
<br/>[2] https://makezine.com/projects/hacking-the-lego-ev3-build-your-own-object-sensor-eyes/
<br/>[3] https://www.ev3dev.org/downloads/
<br/>[4] https://etcher.en.uptodown.com/windows/download/3970628
<br/>[5] https://education.lego.com/en-gb/downloads/mindstorms-ev3/software/
<br/>[6] https://www.informit.com/articles/article.aspx?p=2454873
<br/>[7] https://docs.arduino.cc/retired/getting-started-guides/TFT/
<br/>[8] https://code.visualstudio.com/download
<br/>[9] https://support.arduino.cc/hc/en-us/articles/360019833020-Download-and-install-Arduino-IDE
<br/>[10] https://pybricks.com/ev3-micropython/ev3devices.html
