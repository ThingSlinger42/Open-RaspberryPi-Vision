# Open-RaspberryPi-Vision
Open Source "night vision" for the masses made using easily available components with a Raspberry Pi Zero W at its core.

The display I used in developing all of this is a cheap hobby drone FPV headset with a 480x320 display. These are the 5.8GHz headsets that typically go for around $50-60 USD from the usual suspects. I am currently developing this to support the basic Raspberry Pi camera module v1 NoIR w/12 lens and FLIR's Lepton 3 series. Future plans currently include:
- Reworking the hardware layout to allow easier access to the GPIO pins of the Pi
- A way to access the desktop without needing to connect to the device via VNC or SSH
- Developing and releasing 3D printable addons including a bigger battery compartment for better battery life and power delivery
- Broadening sensor support to include other readily available sensors including:
  - Low light and global shutter camera modules
  - Other readily available uncooled LWIR sensors such as the FLIR Boson and Tau series, the Seek Micro and Mosaic series, and some of the sensors that can be salvaged from old fire department thermals.
  - Other sensors such as gyroscopes, GPS/GLONASS modules, and possibly more
- Adding networking features to allow the video feed to be streamed over local network or a WiFi AP using the Pi's own WiFi radio
- A more discrete wearable version of this same system because it turns out people don't like it when you run around with a suspicious black box with a camera on the front strapped to your face.
- A compact monocular version is also in the works, more details to come at a later date

For best results with these displays I recommend setting the framebuffer size to 480x320 in /boot/config.txt unless you plan to incorporate any features that require a higher resolution. With the default 720p composite video resolution I found that it is often difficult to read text displayed on the desktop. I removed the FPV receiver hardware from my headset to make more room in the cramped front section of the case and to expose the solder pads for the composite video input and 5v power supply.
The main IC in the headset has all markings obfuscated so identification currently isn't possible, however there does appear to be a 5 pin ISP connection broken out on the main PCB. The 5v power supply is only active while the device is powered on.
The 5v power supply built into the headset can power the Raspberry Pi Zero W (CPU @700MHz average) with the 5MP NoIR camera module and WiFi + Bluetooth enabled for about 1 hour and 30 minutes starting from a full charge. Interestingly enough the device does not seem to charge while powered on as the Pi consumes nearly all the input current, however it will maintain current charge seemingly indefinitely powered on and plugged in.

To fit the Pi and M12 lens equipped camera module in the headset:
1. Move the battery to the space underneath the 4 button PCB, cutting the thin plastic wall between the front screw hole/through-hole post beneath the button panel (right next to the LCD/main PCB) and the outer shell to allow it to fit.
2. The Pi Zero goes where the battery was previously with the flat bottom of the pi facing towards the inside of the headset. I used the bottom half of a 3D printed Pi Zero slim case as a shim to keep the Pi in place.
3. The Pi is wired to the 5v power supply via the GPIO power rails on the Pi and the composite video connection is wired from the Pi to the composite video input on the board. In testing that only the Video+ line needs to be connected, connecting the composite ground from the Pi seems to have no noticeable effect on video quality or reliability. I used the bottom half of a 3D printable slim case I found on thingiverse a while back as a shim.
4. To fit the camera, a hole is cut in the front of the outer shell to allow the lens assembly and its base to pass through. I personally found mounting the camera upside down with a ~5mm of space above the ribbon cable connector allowed for the easiest fitment in line with the LCD. The ribbon cable will need to be folded to allow it to connect correctly to the Pi. I personally fused the plastic base of the M12 lens mounting assembly to the outer shell to seal it off and to ensure it stays firmly in place.

I'm still working on fitting the Lepton w/ breakout board in the headset, after that comes the software side.

Some tips for using the FLIR Lepton 3 & 3.5 cores:
- Be careful when handling the shutter, the shutters on these things are delicate and FLIR does not sell them as seperate parts to my knowledge so replacement shutters are a PITA to find.
- If the shutter breaks you can either disable automatic FFC and have the front aperture covered before startup or use the external FFC flag and a cut filter from a cheap switchable IR Pi camera module.
- The VoSPI system on the Lepton 3.x series doesn't always seem to work as advertised, I'd recommend enabling and using the V-sync pin (GPIO3) if you cannot afford dropped frames.
- Many thin plastics can be used as makeshift windows, grocery bags tend to work very well.
- If you remove the shutter assembly you can refocus the lens.
- These things have a bad habit of falling out of their sockets, if you drop the device and the Lepton sensor stops responding first check if it is still pressed into the socket properly.
- In addition to salvaging them from various devices you can buy on ebay/craigslist, GroupGets sells the sensors new. They currently have the Lepton 2.5, 3.0, 3.5, and FS sensors as well as the Boson and Tau series and a wide assortment of interface boards for all of them. If you cannot find a device to salvage a sensor from at a good price I have used GroupGets and can recommend them. They also ship their cores in nice solid packaging similar to what FLIR themselves ships stuff in, which is nice if you want to be sure it arrives in working condition.
