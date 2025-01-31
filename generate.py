from PIL import Image, ImageDraw
import os

#
def cqr_generate(text_input):
    
    file_path = create_file_path(text_input)
    
    text_binary = str_to_binary(text_input)
    
    if len(text_binary) % 8 == 0: 
        image_generation(file_path,text_binary)
    else:
        print("Error at text binary: Not divisible by 8")


# File path
def create_file_path(input):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, f"output\\{input}.png")
    
    return file_path
    
    
# Converts string to binary representation
def str_to_binary(input):
    str_in_binary = ""
    
    for i in input:
        str_in_binary += char_to_binary(i)

    return str_in_binary
    
    
# Converts character to binary representation
def char_to_binary(char):
    char_to_int = ord(char)
    
    binary = bin(char_to_int)[2:]
    char_in_binary = binary.zfill(8)
    
    #print(char_in_binary)
    return char_in_binary


def image_generation(file_path,binary_input):
    # The x and y size of the image in pixels
    image_size = 16
    
    # Creates image
    image = Image.new('RGBA', (image_size, image_size), color='white')

    # Gets pixel array of image
    pixels = image.load()
    
    for y in range(image_size):
        for x in range(image_size):
            two_bit_number_set = (y * image_size + x) * 2
            colour = two_bit_colour(binary_input[two_bit_number_set:two_bit_number_set+2])
            
            if type(colour) == tuple:
                pixels[x,y] = colour
            
    image.save(file_path)
    print(f"cqr saved to: {file_path}")
    
def two_bit_colour(two_bit_input):
    black = (0,0,0,255)
    red = (255,0,0,255)
    green = (0,255,0,255)
    blue = (0,0,255,255)
    
    if len(two_bit_input) == 2:
        print(two_bit_input)
    
    match two_bit_input:
        case "00":
            return black
        case "01":
            return red
        case "10":
            return green
        case "11":
            return blue
        