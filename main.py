from PIL import Image
import os

IMAGE_FORMATS = ["jpeg", "jpg", "png", "heic", "tiff"]

def doImage(filename):
    input_image = Image.open(filename).convert("RGB")
    dominant_color = input_image.resize((1, 1)).getpixel((0, 0))
    width = input_image.size[0]
    height = input_image.size[1]
    target_size = None
    wbigger = False
    print("After init")
    if width == height:
        return
    if width > height:
        target_size = width
        wbigger = True
    else:
        target_size = height 
    
    result_image_color = Image.new("RGB", (target_size, target_size), dominant_color)
    result_image_white = Image.new("RGB", (target_size, target_size), (255, 255, 255))
    result_image_black = Image.new("RGB", (target_size, target_size), 0)
    print("After setting blank canvases")
    
    target_pixel = None
    if wbigger:
        target_pixel = (0, (width - height) // 2)
    else:
        target_pixel = ((height - width) // 2, 0)
    
    result_image_color.paste(input_image, target_pixel)
    result_image_white.paste(input_image, target_pixel)
    result_image_black.paste(input_image, target_pixel)
    print("After paste")

    result_image_color.save(f"output/{filename}_color.png", type="PNG")
    result_image_black.save(f"output/{filename}_black.png", type="PNG")
    result_image_white.save(f"output/{filename}_white.png", type="PNG")
    print("After saving files")

if __name__ == "__main__":
    print("hello")
    files = os.listdir()
    for file in files:
        print(file)
        try:
            if file.lower().split(".")[1] in IMAGE_FORMATS:
                print("Is an image file")
                doImage(file)
        except:
            print("Unlucky moment")