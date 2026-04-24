# Cat vs Dog Image Classification using CNN

##  Project Overview
This project is a deep learning-based image classification system that identifies whether an input image is a cat or a dog. It uses a Convolutional Neural Network (CNN), which is highly effective for image-related tasks.

The model is trained on a dataset of cat and dog images and learns patterns such as shapes, textures, and features to make accurate predictions.

---

##  Features
- Classifies images into **Cat** or **Dog**
- Built using **Convolutional Neural Network (CNN)**
- User

- ---

## ⚙️ How It Works

1. Load and preprocess image dataset  
2. Build CNN model using Keras  
3. Train the model on cat and dog images  
4. Save trained model (`model.h5`)  
5. Create Flask app (`app.py`)  
6. User uploads image via web interface  
7. Model predicts whether it's a cat or dog  

---

##  Model Performance
The CNN model achieves good accuracy in distinguishing between cat and dog images. Performance may vary depending on dataset size and training epochs.

---

##  Example

**Input:** Image of a dog  
**Output:** Dog 

**Input:** Image of a cat  
**Output:** Cat  

---

##  Future Improvements
- Improve model accuracy with more data  
- Add more classes (multi-class classification)  
- Deploy on cloud (Heroku / AWS)  
- Improve UI design  

---

##  Conclusion
This project demonstrates how CNN can be used for image classification tasks. It combines deep learning with a simple web application, making it a complete end-to-end project.
