To link a Lego Mindstorms EV3 block to Wi-Fi and then to a web page, a couple of steps are involved. The EV3 brick must have ev3dev operating system installed first, a Debian-based Linux distribution tailored for the EV3. The EV3 is able to support Wi-Fi with ev3dev using compatible USB Wi-Fi adapters. After the dongle is plugged into the EV3's USB connector, the Wi-Fi network options can be set up either locally on the brick's display or remotely via a USB or Bluetooth link using terminal commands.

After the Wi-Fi setup, the EV3 is capable of accessing the internet just like any Linux device. To interact with a website, the EV3 requires a programming environment like Python, which is compatible with ev3dev. With libraries like requests in Python, the EV3 can send data to or retrieve data from a web site. For example, the EV3 could send sensor readings to a web server or retrieve instructions from a remote control panel. This is generally a matter of creating an HTTP request with the correct URL, headers, and data payload. Successful networking of an EV3 via Wi-Fi and a website provides remote monitoring, control, or data logging, significantly enhancing the capability of a Lego Mindstorms robot.

TO USE:
1. Ensure visual studio code[8], balena etcher 1.6.0[4] are installed and setup.
2. Built the Minifigure dispenser as the pictures show. 
3. Download "ev3dev-stretch" file from this website[3], then flash to microSD card using balena etcher.
4. Insert microSD into ev3 brick and turn on
5. Plug a compatible wifi dongle in to the ev3 and connect to a wifi network. (We use NETGEAR A6100) 
6. In visual studio code, go to "view" at the top and selcet "Extensions". Search for an install "LEGO® MINDSTORMS® EV3 MicroPython"
7. Connect ev3 to computer using its USB Mini port. In the bottom of the explorer tab there should be a section called "EV3 DEVICE BROWSER"
8. Open the device browser menu and select "Click to connect to a device" and the ev3 brick should appear as an open. Select it.
9. Run main.py to upload it to the ev3, it will crash immediatly but that is expected.
10. Disconnect ev3 brick from computer and connect to the model following the wire setup image. 
11. Navigate to file browser on the ev3 and find the name of the project. Open it and run "main.py".
12. Open index.html in visual studio code and navigate to line 56. 
13. Ensure that the IP Address on this line matches the IP address of the EV3 block (top left of screen) 
14. Before you run the program, make sure the push are is as far left as it can and the lift is all the bottom. The bounty hunter must all be facing right and be in the right order. (From left to right: Dengar, IG-88a, Boba Fett, Bossk, LOM-4, Zuckuss)
15. Run the file locally and press a bounty hunter. 
16. Bounty Hunter will be selected.

wesbites:
See ardunioBot README
