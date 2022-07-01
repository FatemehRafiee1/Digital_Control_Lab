**Main goal: Change HEADING and move FORWARD/BACKWARD simultaneously**

* This code will make the robot set the new heading and also move to a certain coordinate, in a nutshell the robot goes from point A to point B which requires the robot to chane its heading cause they're not in the same direction.

* In this part we have combined task 1 and task 2. We set robotpos and a desired heading to reach point B, then initialize the controllers to make this error zero. Note that this time we have two errors and they are seperately working. It means that heading reaches the finall value in 2 seconds but it takes longer for position_error to reach the finall value.

* In this part it's recommended to use PI with proportional coeffient of 0.05 for both angle and position, since it's a little bit more complex than the previous ones. we used two Ki as mentioned before and their valuse are less than 0.1, cause otherwise the robot will speed up and pass the desired point.

* As said before we did this implementation using BD for differentiator and FD for Integrator cause their combination still remains stable.

* We chose 0.05 as the limit for vr and vl to make the motors stop if they have a lower velocity. we always need a dead zone for out robots cause it makes the simulation less ideal and more realistic.

**Here is [my video](https://youtu.be/XCejqwPlNNo) of all 4 tasks**

***

* How can YOU run this project?
First You should install the latest 64-bit version of Python 3.10, 3.9, 3.8 or 3.7 from the official Python website, in case you don't have that. 
If you want to check just run the following command in terminal and if it shows ther current version then it means you already have it installed.

```
$ python -V 
```
or 
```
$ python --version 
```
Otherwise you need to run this command to get the desired version.

```
$ sudo apt-get install python3.9
```
Just in case you don't have pip, check [this website](https://www.tecmint.com/install-pip-in-linux/) to learn getting it based on your system.

Next by visiting [this website](https://cyberbotics.com/) you can easily download Webots app on your OS.

Now you can get the zip file on my github and export them on you system.

Then you open webots by simply typing "webots" in your terminal.

By pressing Ctrl+Shift+O you can open soccer.wbt which is in the file you extracted.
And as you open it, it will run automatically.

If you have problems opening the git file it might show that you haven't install git yet. 
To do so one of the easiest ways is to visiting [git website](https://git-scm.com/) and on the right side you can choose your system and download it.

Inorder to make sure that the installation was successful run this command:

```
$ git --version
```
And you'll get a result like this:

```
$ git version 2.9.2
```

















﻿


