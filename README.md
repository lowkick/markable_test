# markable_test

simple instructions (tested on windows, python 2.7)

1) have python, opencv, numpy correctly installed

2) put all jpg images in a folder. 
Example in c:\test\images

3) run the script passing the folder as parameter. 
Example python bkremove.py c:\test\images

4) the results are written in the same folder, but with "_out" suffix and png extension

The program makes a simple watershed segmentation, presuming that in the center of the image there is the dress and in the border there is the background. 
If the background and the dress are omogeneus enough, this works, at least I hope so.

