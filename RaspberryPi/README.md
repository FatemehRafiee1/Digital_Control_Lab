**Basic movements of a robot with raspberrypi**

* In this code you can move the robot using WSAD keys on your keyboard. (forward/backward/left/right)

![RaspberryPi](https://user-images.githubusercontent.com/97700019/176919332-dd1f45bb-6d24-4d8e-9f3c-84365f0b7c07.gif)


* At first we have a minimal code to run commands.

* What we need to do here is to let the robot know when and where to move.

* Since we want to support both upper and lower case, we change all of them to lower, by using .lower() method

* Next we want to be able to quit raspberry environment by pressing 'q', so at first we check if the letter enterd is 'q' or not. If so, it won't check other conditions.

* If the client has entered anything but 'q', we'll continue to check whether that letter is one of WSAD or not, if so, we enter of those conditions and as a result a command will be sent to the robot. This is a simple command which +-100 indicated robot's velocity and its direction. The rest (15+00) is its standard format.

* If none of WSAD or q were pressed, it means that we want the robot to stop, so we set the velocity +000; which should always have 3 digits and its maximum is 200 but 100 will suffice.

* Here we can see the code written on raspberryPi:

```
import serial
import getch
serialport = serial.Serial ("/dev/ttyS0")
serialport.baudrate = 115200

while(True):
    x = getch.getch().lower()
    print(type(x))
    print(x)
    if x == "q":
        break
    elif x == "w":
        command = "+100+10015+00"
    elif x == "s":
        command = "-100-10015+00"
    elif x == "a":
        command = "-100+10015+00"
    elif x == "d":
        command = "+100-10015+00"
    else:
        command = "+000-00015+00"
    
    serialport.write(command.encode())
    
```


















﻿


