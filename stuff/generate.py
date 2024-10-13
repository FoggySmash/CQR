from PIL import Image, ImageDraw
import os


def generate(file_name):
    script_dir = os.path.dirname(__file__)

    file_path = os.path.join(script_dir,'..', 'input', file_name)
    print(file_path)
    
    with open(file_path, mode='r') as file:
        content = file.read()
    print(content)
        


#img = Image.new('RGB', (16, 16), color='white')
#d = ImageDraw.Draw(img)

#img.save("example.png")