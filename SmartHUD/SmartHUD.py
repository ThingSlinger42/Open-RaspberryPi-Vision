#Basic Raspberry Pi Camera Viewer with data overlay, optimized for HUD use

import picamerax
import time
import numpy
from PIL import Image, ImageDraw, ImageFont

#Display Resolution
vHeight = 320
vWidth = 480

dataOverlay = Image.new("RGB", (vWidth, vHeight))

with picamerax.PiCamera() as camera:
   camera.resolution = (vWidth, vHeight)
   #Camera settings are optimized for best low light performance without reducing framerate below useful levels
   camera.framerate = 24
   camera.iso = 1600
   camera.rotation = 180
   camera.led = False
   #these here are why picamerax is used, it includes the 'greyworld' awb mode for NoIR sensors and allows analog gain to be set manually
   camera.awb_mode = 'greyworld'
   camera.analog_gain = 8.0
   camera.start_preview()

   img = dataOverlay.copy()
   overlay = camera.add_overlay(img.tobytes(), layer = 3, alpha = 100) 
   #wait one second before updating HUD overlay
   time.sleep(1)
   try:
      while True:
         #Displays the current system time in 24h format in bottom left
         text = time.strftime('%H:%M:%S', time.localtime())
         img = dataOverlay.copy()
         draw = ImageDraw.Draw(img)
         draw.font = ImageFont.truetype("/usr/share/fonts/truetype/piboto/Piboto-Bold.ttf", 20)
         #This text color (#FF4400, red-orange) seems to give good readability without being an eyesore in most lighting conditions even when partially transparent
         draw.text((10, 280), text, (255, 68, 0))
         #this method of updating the overlay works, though it does spam errors in the console output every time this line runs
         overlay.update(img.tobytes())

   finally:
      camera.remove_overlay(overlay)
