# markable_test

simple instructions (tested on windows, python 2.7)

1) have python, opencv, numpy correctly installed

2) put all jpg images in a folder. 
Example in c:\test\images

3) run the script passing the folder as parameter. 
Example python bkremove.py c:\test\images

4) a third parameter is optional, it's the colorspace used for segmentation. 
I find that in some cases RGB works better, in some others HSV or HLS give better results. 
You can pass a number 1, 2, 3 as third parameter, with the meaning:
1: use RGB colorspace (default)
2: use HSV colorspace
3: use HLS colorspace
Example python bkremove.py c:\test\images 2
this uses HSV colorspace

5) the results are written in the same folder, but with "_out" suffix and png extension.
png is chosen to allow for multirun without reelaborating the elaborated images

The program makes a simple watershed segmentation, presuming that in the 
center of the image there is the dress and in the border there is the background. 
If the background and the dress are omogeneus enough, this works, at least I hope so.

There is a debug = 0 in the source. You can use debug = 1 to see the intermediate 
images (and not save them). The sofware also runs in single thread mode when debug = 1.
