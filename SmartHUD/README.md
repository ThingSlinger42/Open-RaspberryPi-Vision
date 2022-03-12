This Python 3 script provides a basic "preview" with a time overlay and camera settings optimized for low light use or use in the dark with an IR illuminator.

This script requires picamerax and Pillow, both of which can be installed using pip:

```bash
pip3 install Pillow picamerax
```

Note that since the camera preview overlay on the Pi is a GPU render overlay, you cannot view anything behind it once launched. You can still press Ctrl + D to kill the script or ssh and "killall python3" if all else fails.

Simply run the program as the user "pi" to use. I set up a systemd module to run the script on boot and it launches it as soon as Xwindows is running. I have included it as "SmartHUD.service". Restart="always" is uesd to ensure it continues attmepting to run the script until X is running.

To install the systemd module, change "ExecPath=(directory)" to the full path of the directory SmartHUD.py is in or place SmartHUD.py in /home/pi/SmartHUD. Future versions of the SmartHUD script will use /home/pi/SmartHUD as the active directory so it may be more convenient to just create that folder and place the script in it. Once that's done copy the module to /lib/systemd/system. Once that's done you can run "sudo systemctl enable SmartHUD". To verify that it works reboot the Raspberry Pi and it should launch the camera preview just before the desktop loads.

Currently the only way to access the desktop locally is to disable the SmartHUD service and reboot, as it just relaunches within a few seconds if you kill it. The preview does not appear on VNC since it is done through the GPU as a hard overlay and can only be seen on the main hardware display.
