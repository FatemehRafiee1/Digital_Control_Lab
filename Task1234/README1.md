**Main goal: Moving straight to reach the desired point (without changing direction)**

* This code makes the robot move to reach the specific posion (which is set beforehand) without turning around.

* In this code we find the difference between the desired point coordinates and the current position of robot, then make the error minimum using PID (or P,PI,PD) controllers.

* It works well when using P controller, but adding PI would make it get more accurate since PI makes the permanent error to be zero. when adding PD at first we face a problem and the velocity goes futher beyond the limit, and the reason is that Kd should be really small (in order of 10^-6) but the total time to get stable is 10 seconds in all of them. Also when testing PID, no change was noticed.

* PI controller is implemented by forward difference method and PD controller is implemented by backward difference method; normally we prefer backward since it's not likely to cause instability but for PI we tested FD and there was no problem in our case (as it is only one simple task at a time).

* Dead zone is considered in this project, meaning that both motors will stop working if their velocity is less than a certain amount. It's completely up to your task and in this case we determined 0.05 to be the borderline.

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


