# Image Resizer

Resize your image like a pro. 
Choose what you want to change, height, width or both. 
Or You can scale it to change image size keeping the same aspect ratio.

# Quickstart

Run this script with Python 3.x. 
As a required parameter you should specify path to image file. 
By default output image will be saved in working directory.
As an optional parameter, you can specify path to save image and its name.
Then specify what to do with image. 
Available parameters are: change it height (-t) or/and width (w) or scale (-s) it.


Example of script launch on Linux, Python 3.5:

```bash
$ python image_resize.py -f <path to image> -s 0.2 -o ~/Pictures/my_image.png
```

All available parameters are:
```bash
usage: image_resize.py [-h] -f FILE [-o OUTPUT] [-w WIDTH] [-t HEIGHT]
                       [-s SCALE]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to image to resize
  -o OUTPUT, --output OUTPUT
                        Path to save image
  -w WIDTH, --width WIDTH
                        result image width
  -t HEIGHT, --height HEIGHT
                        result image height
  -s SCALE, --scale SCALE
```

 
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
