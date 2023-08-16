from PIL import Image
from flask import Flask, render_template, send_file, request
import os

IMAGE_FORMATS = ["jpeg", "jpg", "png", "heic", "tiff"]
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def fit_image_into_square(input_image):
    dominant_color = input_image.resize((1, 1)).getpixel((0, 0))
    width, height = input_image.size
    target_size = max(width, height)

    if width != height:
        result_image = Image.new("RGB", (target_size, target_size), dominant_color)
        if width > height:
            target_pixel = (0, (width - height) // 2)
        else:
            target_pixel = ((height - width) // 2, 0)
        result_image.paste(input_image, target_pixel)
    else:
        result_image = input_image.copy()  # No need to modify if already square

    return result_image

@app.route("/generate", methods=["POST"])
def doImage():
    try:
        uploaded_file = request.files["png"]
        if uploaded_file.filename == "":
            return "No file selected", 400

        image = Image.open(uploaded_file)
        image = image.convert("RGB")

        result_image = fit_image_into_square(image)

        output_path = "output/eeeee_color.png"
        result_image.save(output_path, format="PNG")

        return send_file(output_path)
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
