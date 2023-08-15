from PIL import Image
from flask import Flask, render_template, send_file, request
import os

IMAGE_FORMATS = ["jpeg", "jpg", "png", "heic", "tiff"]
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def doImage():
    # input_image = Image.open(filename).convert("RGB")
    # file = request.files["png"]
    # file.save("test_image.png")
    input_image = Image.open(request.files["png"])
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
    # result_image_white = Image.new("RGB", (target_size, target_size), (255, 255, 255))
    # result_image_black = Image.new("RGB", (target_size, target_size), 0)
    print("After setting blank canvases")
    
    target_pixel = None
    if wbigger:
        target_pixel = (0, (width - height) // 2)
    else:
        target_pixel = ((height - width) // 2, 0)
    
    result_image_color.paste(input_image, target_pixel)
    # result_image_white.paste(input_image, target_pixel)
    # result_image_black.paste(input_image, target_pixel)
    print("After paste")

    result_image_color.save(f"output/eeeee_color.png", type="PNG")
    return send_file("output/eeeee_color.png")
    # result_image_black.save(f"output/{filename}_black.png", type="PNG")
    # result_image_white.save(f"output/{filename}_white.png", type="PNG")
    print("After saving files")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)