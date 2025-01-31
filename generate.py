from PIL import Image, ImageDraw
import os

def cqr_generate(text_input):
    
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, f"output\\{text_input}.png")
    
    # The x and y size of the image in pixels
    image_size = 16
    
    # Creates image
    image = Image.new('RGBA', (image_size, image_size), color='white')
    
    # Gets pixel array of image
    pixels = image.load()
    
    alternator = 0
    
    for y in range(image_size):
        for x in range(image_size):
            if alternator == 0:
                colour = (255,0,0,255)
                alternator = 1
            else:
                colour = (0,255,0,255)
                alternator = 0
                
            pixels[x,y] = colour
    
    image.save(file_path)
    print(f"cqr saved to: {file_path}")