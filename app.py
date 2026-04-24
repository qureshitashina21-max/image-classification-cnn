from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Load model
model = load_model("model.h5")

# Prediction function
def predict_image(img_path):
    img = image.load_img(img_path, target_size=(128, 128))  
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    prediction = model.predict(img_array)

    if prediction[0][0] > 0.5:
        return "Dog 🐶"
    else:
        return "Cat 🐱"
    confidence = prediction[0][0]

    if confidence > 0.5:
        return f"Dog 🐶 ({confidence*100:.2f}%)"
    else:
        return f"Cat 🐱 ({(1-confidence)*100:.2f}%)"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]

        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            result = predict_image(filepath)

            return render_template("index.html", prediction=result, img_path=filepath)

    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True, port=5001)
