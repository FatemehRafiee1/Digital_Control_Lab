**Main goal: Following the ball all over the soccer field and moving forward the oponent's goal**

* This code is slightly different from others, since this time it reacts to ball and goes after it.

* Here we have 2 parameters called 'direction' and 'strength' in ball_date, they change it ball position varies. Specifically, 'direction' gives us sine and cosine of the angle created between the ball and robot. 'strength' is read from and IR sensor which its inverse will give us the position error between ball and robot. Therefore we can find both angle and distance errors by these 2 parameters. (Note that it's possible to find the angle using atan2(sine, cosine))

* This time proportional and integrator coefficients need to be large enough to meet the needs of this task, since ball moves relatively fast, the robot need a higher speed, so we have chosen Kp and Ki 100 times greater otherwise robot would never catch the ball. Needless to say that D term didn't come in handy here because of its small impact.

* We are aware that forward difference method may end up making our system unstable but it doesn't happen all the time, so we tested various situations and it worked just fine, so we implemented PI controller using FD.

* For dead zone we set 0.1 as the lower bound, so that if motors' velocity reaches this number the robot won't move. Dead zone will cause the system work efficiently cause there might be some unwanted vibrations specially in non-ideal situations.

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


