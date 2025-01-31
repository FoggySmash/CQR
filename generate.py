from PIL import Image, ImageDraw
import os

#
def cqr_generate(text_input,image_size):
    
    file_path = create_file_path(text_input)
    
    text_binary = str_to_binary(text_input)
    
    if len(text_binary) % 8 == 0: 
        image_generation(file_path,text_binary,image_size)
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


def image_generation(file_path,binary_input,image_size):   
    image_s = int(image_size) 
    # Creates image
    image = Image.new('RGBA', (int(image_s), int(image_s)), color='white')

    # Gets pixel array of image
    pixels = image.load()
    
    for y in range(image_s):
        for x in range(image_s):
            two_bit_number_set = (y * image_s + x) * 2
            colour = four_bit_colour(binary_input[two_bit_number_set:two_bit_number_set+4])
            
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
        
def four_bit_colour(four_bit_input):
    black = (0,0,0,255)
    red = (255,0,0,255)
    yellow = (255,255,0,255)
    green = (0,255,0,255)
    cyan = (0,255,255,255)
    blue = (0,0,255,255)
    magenta = (255,0,255,255)
    white = (255,255,255,255)
    darkred = (128,0,0,255)
    darkyellow = (128,128,0,255)
    darkgreen = (0,128,0,255)
    darkcyan = (0,128,128,255)
    darkblue = (0,0,128,255)
    darkmagenta = (128,0,128,255)
    darkwhite = (171,171,171,255)
    darkerwhite = (85,85,85,255)
    
    if len(four_bit_input) == 4:
        print(four_bit_input)
    
    match four_bit_input:
        case "0000":
            return black
        case "0001":
            return red
        case "0010":
            return yellow
        case "0011":
            return green
        case "0100":
            return cyan
        case "0101":
            return blue
        case "0110":
            return magenta
        case "0111":
            return white
        case "1000":
            return darkred
        case "1001":
            return darkyellow
        case "1010":
            return darkgreen
        case "1011":
            return darkcyan
        case "1100":
            return darkblue
        case "1101":
            return darkmagenta
        case "1110":
            return darkwhite
        case "1111":
            return darkerwhite