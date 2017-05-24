# About
This is a simple tool to combine multiple small magnified images from flashphotograph and create a berrer image then those available free.

## API Description

http://images1.flashphotography.com/Magnifier/MagnifyRender.ashx?X=242&Y=140&O=26993095&R=00003&F=0045&A=71714&rand=0.6425606573905747
http://images1.flashphotography.com/Magnifier/MagnifyRender.ashx?X=320&Y=141&O=26993095&R=00001&F=0041&A=71714&rand=0.06721942701854688
```
R - Image Select
rand  - random to prevent cache
X - top x 0,0 - 500,700
Y - top y
o - user ID 
F = 0045
R - 00002 to 00012
F=0041
00001 x 0,0 to 500, 630
```

# Run steps

1. Install all pip dependency
```
> pip install requests
> pip install PIL

```
2. For each image check the URL in the Magnifier tab. 
    a. Main.py Line 20 url_path
```angular2html
Sample URL:
http://images1.flashphotography.com/Magnifier/MagnifyRender.ashx?X=242&Y=140&O=26993095&R=00003&F=0045&A=71714&rand=0.6425606573905747
http://images1.flashphotography.com/Magnifier/MagnifyRender.ashx?X=320&Y=141&O=26993095&R=00001&F=0041&A=71714&rand=0.06721942701854688
Copy the &O=26993095&R=00003&F=0045&A=71714 and set it in 
```

3. Run Main.py by changing the output_path in Line 19. This will download all the small images available through the magnifier.

4. In Combine.py change :
```
Line 15 : input_path to the folder where the Main.py downloaded all the images</br>
Line 20 : change the destination where you want to store the full merged image.
```    
5. To remove the border edges use image editing tools like Paint and crop the sides as per your needs.
