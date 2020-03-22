from PIL import Image
# Load the Picture
# Make sure to change the path of the desired picture you want to downsize
# It can only be used for JPG/JPEG images
picture_path = (r"C:\Users\Rishav\Pictures\Rishav Mani Bhurtel.JPG")
picture = Image.open(picture_path)

# I downsize the image with an ANTIALIAS filter (gives the highest quality)
picture = picture.resize((picture.size),Image.ANTIALIAS)

# Save downsized image
picture.save(picture_path[:-4] + "_downsized.jpg",optimize=True,quality=50)
