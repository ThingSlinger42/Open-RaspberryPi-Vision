This Python 3 script provides a basic "preview" with a time overlay and camera settings optimized for low light use or use in the dark with an IR illuminator.

This script requires picamerax and Pillow, both of which can be installed using pip:

'' pip3 install Pillow picamerax ''

Note that since the camera preview overlay on the Pi is a GPU render overlay, you cannot view anything behind it once launched. You can still press Ctrl + D to kill the script or ssh and "killall python3" if all else fails.

Simply run the program as the user "pi" to use. I set up a systemd module to run the script on boot and it launches it as soon as Xwindows is running. I have included it as "SmartHUD.service". Restart="always" is uesd to ensure it continues attmepting to run the script until X is running.
