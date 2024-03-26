from PIL import Image, ImageFilter

img = Image.open('mmcm.jpg')
print(img)
print(img.format)
print(img.size)
print(img.mode)


##### Reducing Image quality without decreasing the size
##### Reducing the space required by the image

# img.save("image_resized.jpg", quality=25, optimize=True)
# red_img = Image.open('image_resized.jpg')
# print(red_img.size)


# crooked = img.rotate(90)
# crooked.save("twisted.png", 'png')


# resized_img = img.resize((300,300)) # accepts a tuple
# resized_img.save('resized.png', 'png')
#### The problem with resizing image is that it loses it's aspect ratio. That is why we use thumbnail
#### even if we specify random height and width, it won't go above the max and keep the aspect ratio the same.
#### So maybe it wont make it a square if the orignal image is not a square

# img.thumbnail((30,30))
# img.save("thumb.jpg")
# print(img.size) # you would see it created 30,20 (considering the image I have now) instead of 30x30

## crop
# box = (100, 100, 400, 400)
# region = img.crop(box)
# region.save('new.png', 'png')

# print(dir(img)) ### To check everything that can be done

# filter_img = img.filter(ImageFilter.GaussianBlur)
# filter_img.save("mmcm_blur.png", "png")
# new_img = Image.open("mmcm_blur.png")
# print(new_img.size)

# Look for options in ImageFilter

### Will convert the image to greyscale and also to PNG
# converted_img = img.convert('L')
# converted_img.save("grey.png", "png")

