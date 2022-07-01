**Main goal: Changing the HEADING of the robot without moving forward/backward**

* This code will cause the robot to turn around to reach a desired angle which is set beforehand. 

* In this code we get the heading data of the robot at every instance, then find the difference between that and the desired angle and we try to make this error zero.

* At first we start by P controller, it works well but we need to make sure the coefficient is not greater than 0.1 cause in this way robot would jump into a unstable mode after 0.5 second. Then by adding I term we test PI controller which makes the result more accurate. In this code PD controller doesn't work that well unless you choose Kd very small, like 0.0001. And totally the result is satisfying using PI controller.

* In all these tasks we have implemented the integral term by forward difference and the differentiator by backward difference since it's more stable in various situation.

* We have considered 0.05 as the dead zone velocity for right and left motors, so that when it realizes the velocity it less than that, robot simply stops. This will prevent unwanted moves.

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


