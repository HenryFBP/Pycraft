![PycraftGitHub](https://user-images.githubusercontent.com/81379254/133644694-2c1149b8-01be-40f7-88ee-6110922bcf8a.png)

This is a project in which I aim to test my abilities and learn new skills, and show what I can do to the community thank you all very much for coming here and I hope you enjoy and are inspired to fire up IDLE yourself. Made with Python 3.9 64-bit and Windows Visual Studio Code for ease of use and id strongly recommend these!

[![](https://img.shields.io/badge/python-3.9+-blue.svg)](www.python.org/downloads/release/python-390)

Progress towards Pycraft v0.9.2: ![Progress](https://progress-bar.dev/10)

## About

Pycraft is a 3D open-source, open-world video game made in Python. For a long time attempts to make large 3D games in python has been ignored, I believe there are two reasons: one; People use Python primarily for data handling and processing and not graphics and, two; there is little to no documentation out there to do anything more than make a 3D rotating cube in Python. Making a 3D game in Python for me hasn’t been an easy experience, far from it but I have decided to share my project, complete with tutorials, explanations, articles and code explanations in the hope that 3D game development in Python can be seen as a more easily attainable target, and to fill that ga in documentation. Pycraft then is a trial project, as I learn and experiment on what goes best where and how thing go together, this is why development can sometimes appear to have stopped, because I’m learning and testing what I've learned, so hopefully for people in the future it will be an easier experience. Also, don’t forget there is more to game development than just graphics, there is AI, sound, physics and all the other GUIs that go with it, and as I learn the quality of the overall program will improve. Pycraft is not going to be the final name of the game, however until something better becomes available, we shall stick to it

## Preview video

Here is a Youtube link to a showcase of Pycraft v0.9.1 (Developer Build): (https://youtu.be/shAprkrcaiI)

## Setup

When setting up and installing this project you can either run the bare bones file which is likely found above this 'README.md' file if your viewing this on the GitHub website then please follow the steps below for more information on the setup and installation of this project however where possible it is recommended that you use the executable file (.exe) under the most recent releases page as this will run regardless of where you place the file or if you have python or even if you have any of the installed modules this project depends on because its compiled into one file (hence the larger file size). which makes removing the file much easier and also sharing and transporting the file easier and more convenient. However, if you are planning to use the project in its uncompiled format (which as mentioned will be at the top of this page if you are on the GitHub website) then it is recommended you follow the below steps to make sure the project works properly.

The project will download as a (.zip) compressed file. Please make sure you have the project decompressed before use. Next make sure that any folders and files outside of the 'Pycraft' folder are removed and that the 'Pycraft' file is in the intended place for the file to be run from. This file can be freely moved around, transported between drives, computers and folders in this form. A video guide to this will be uploaded here and in YouTube in the coming months.

When running the program please make sure you have a minimum of 1GB of free space on the drive and also have Python 3 installed on your device. This can be found here: (www.python.org/downloads). The sub version of Python isn't too important in this circumstance however the project has been tested in Python 3.9.5 and is known to work. In addition to all this please make sure you have the following modules installed on your device:
Pygame, Numpy, PyOpenGL, Pillow, PyAutoGUI, Psutil, PyWaveFront, CPUinfo and Ctypes. 
For those not familiar they can be found here: (pypi.org) and you can use the following syntax to install, update and remove these modules:
```
pip install <module>
pip uninstall <module>
pip update <module>
```

Here is a short video tutorial explain all this (It’s really not too bad), this is the link to the YouTube video: (youtu.be/DG5YbE-umw0)

## Running the program

When running the program, you will either have a (.exe) file, downloaded from the releases page, or you will have the developer preview, if you have the developer preview, which can be found in the files section of this repository then this is how you run that program. Pycraft has recently undergone some large structural redesigning, so to run the program the advice is now different:

Now you have the program properly installed hopefully (you’ll find out if you haven’t promptly!) you need to locate the file "main.py" basically all this program does is run the right modules, initiates the main program, and catches any errors that might arise in the program in a nicely rendered error screen, if it crashes on your first run then chances are you haven’t installed the program correctly, if it still doesn’t work then you can drop me an email @ "ThomasJebbo@gmail.com" or comment here on the repository, I do hope however that it works alright for you and you have a pleasant experience. I might also add this program has been developed on a Windows 64-bit computer however should run fine on a 32-bit Windows machine (uncompiled) or through MacOS although they remain untested for now. 

I recommend creating a shortcut for the "main.py" file too so it’s easier to locate.

## Credits

#### With thanks to; <br />
- Thomas Jebson <br />
- Python 3 @ www.python.org <br />
- OpenGL @ www.opengl.org <br />
- Pypi @ www.pypi.org <br />
- Pillow (PIL) @ www.python-pillow.org <br />
- Pygame @ www.pygame.org <br />
- Windows 10 - Visual Studio Code @ https://code.visualstudio.com/ <br />
- Freesound: - Erokia's "ambient wave compilation" @ www.freesound.org/s/473545 <br />
- Freesound: - Soundholder's "ambient meadow near forest" @ www.freesound.org/s/425368 <br />
- Freesound: - monte32's "Footsteps_6_Dirt_shoe" @ www.freesound.org/people/monte32/sounds/353799 <br />
- Blender @ www.blender.org <br />

## Uncompiled Pycraft's Dependencies <br />

When your installing the uncompiled Pycraft variant from here you need to install the following 'modules', which can be done through your Control Panel in Windows (First; press the windows key + r then type "cmd" then run the below syntax) or on Apple systems in Terminal.

```
pip install <module>
pip uninstall <module>
pip update <module>
```
pip is usually installed by default when installing Python with most versions.

- PIL (Pillow or Python Imgaging Libary) <br />
- Pygame<br />
- Numpy <br />
- PyOpenGL (and its counterpart PyopenGL-accelerate) <br />
- PyAutoGUI <br />
- PyWaveFront<br />
- CPUinfo <br />

_Disclaimer; unfortunately, lots of these python modules (first and third party) can require some external modules that will be installed during the installing process of the above modules, unfortunately this makes it really difficult to give credit to those modules, if you have any recommendations, please contact me appropriately._

## Changes

Pycraft v0.9.1 is now live! Here is a list of all the added features to this sub-release:

- Some UI improvements to the home screen, which now displays an animation on the 'geometric rose' design.
- Added OpenGL benchmarks to the benchmark function, which has seen some minor graphical changes too.
- The ENTIRE programming structure of the game has changed, improving performance and load times, and will hopefully make adding features and inevitably debugging them much easier, also this is a feature we hope you don't notice as the games reprogramming from before to after has been extensively checked and modified to make sure everything works and is just as seamless as before.
- Screenshots have been fixed and hopefully for the final time.
- Windows 11 compatibility is now also added, although the game should work fine on Windows 10 as possibly earlier machines, however this hasn’t been tested at present.
- Many, many, many bug fixes.

Again, feedback would be much appreciated this update was released on; 10/10/2021 (UK date) DD/MM/YYYY. As always, we hope you enjoy this new release and feel free to leave feedback.

## Our update policy
New releases will be introduced regularly, it is likely that there will be some form of error or bug, therefore unless you intend to use this project for development and feedback purposes (Thank you all!) we recommend you use the latest stable release; below is how to identify the stable releases.

## Version naming
Versions have changed pretty dramatically the past few days, don’t panic I'm here to help! In sort the new version naming system more closely follows the Semantic Naming system; in short the first number in this example 'v0.8.1' stands for release number, this project has not yet been released officially so is still in development, which is why the second number increases, because that indicates each pre-release, and finally that last number which won’t appear in most releases will indicate a special release over the 'normal' file style release, which actually won’t be the typical standard actually in the far future, but that’s a (long) way off for now!

## Pycraft's update plan

Pycraft will be continually updated for a long time yet. The next release, Pycraft v0.9.1 will not feature as a (.exe) release but only as a code release, it will feature some small UI changes and some larger code restructuring and reprogramming, most of this will go on behind the scenes and won't result in much of a change for the adverage user, then Pycraft v0.9.2 will include changes to the 3D space, and thus will continue for multiple releases to come, Pycraft will now updated gradually, not all in one go, however (.exe) releases will likely only occur at major releases like the upcoming Pycraft v0.10!

## (.exe) releases

Right time to tackle some of the confusion behind the (.exe) releases that will now be a feature of all main releases. Now when installing and running the (.exe) release its actually much, much easier to do, you just have to download the file attached and simply double click on the file to run it, typically the file will be downloaded to the downloads folder on your computer. The project might take a second or two to appear to start to do something (as everything it requires is loaded) then from there it will work without having any modules installed, any connection (like ALL other releases) or any extra downloads required, its all-in-one for much easier use, and this isn’t an app that installs anything onto your computer outside of the file so to remove you simply have to delete the 'Pycraft.exe' file. Simple!

## The Planned Storyline

In Pycraft the plan is that you will start at sea on a boat, there you will learn that you have left your home on a separate island to find work and safety on this new one, when you arrive you are shown to your room and the next day join a small groups of trainee knights, each training to be part of the Royal Guards system that protects the island from the dangers on the island, you quickly rise in rank as your skills shine until one day all your skills are put to the test. Will you follow through? Well, you don't know yet, I've got to make the game first!

## Other sources

I have started writing an article on medium which is released at the start of every month, this compliments the weekly updates that are posted on my twitter profile, it would be greatly appreciated if you wanted to check it out here at this link: (link.medium.com/Mhqd8qIAhjb). And recommendations and feedback are, as always, greatly appreciated, a lot of time and work goes into making this happen!

## Final Notices

Thank you greatly for supporting this project simply by running it, I am sorry in advance for any spelling mistakes. The programs will be updated frequently and I shall do my best to keep this up to date too. I also want to add that you are welcome to view and change the program and share it with your friends however please may I have some credit, just a name would do and if you find any bugs or errors, please feel free to comment in the comments section any feedback so I can improve my program, it will all be much appreciated and give as much detail as you wish to give out. BY INSTALLING THIS PROJECT ONTO YOUR COMPUTER AND RUNNING IT I; Tom Jebbo DOES NOT TAKE ANY RESPONSIBILITY FOR ANY DAMAGES THIS MAY CAUSE HOWEVER UNLIKELY, AND YOU AGREE TO HAVE EXTERNAL MODULES INSTALLED ONTO YOUR COMPUTER (WHEN NOT CHOOSING THE RECOMMENDED EXECUTABLE VERSION) ALSO, OF WHICH I HAVE NO CONTROL OVER, PLEASE USE THIS PROGRAM RESPONSIBLY AND DO NOT USE IT TO CAUSE HARM. YOU MUST ALSO HAVE PERMISSION FROM THE DEVICES MANAGER OR ADMINISTRATOR TO INSTALL AND USE COMMAND PROMPT OR TERMINAL. NO DATA THIS PROGRAM COLLECTS IS STORED ANYWHERE BUT, ON YOUR DEVICE, AND AT ANY POINT NO CONNECTION TO A NETWORK IS REQUIRED. THIS PROGRAM DOES NOT SEND ANY DATA TO THE DEVELOPER OR ANYONE ELSE ABOUT THIS PROGRAM. Thank you.
