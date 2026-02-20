![Uploading Screenshot 2026-02-20 150657.png…]()










# 😊 Real-Time Facial Emotion Detection

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white"/>
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"/>
  <img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
</p>

<p align="center">
  A deep learning-powered application that detects and classifies human emotions in real-time using a webcam feed. Built with OpenCV for face detection and a pre-trained Keras model for emotion classification.
</p>

---

## 📸 Demo

> Real-time detection of emotions directly from webcam or video input — with bounding boxes and emotion labels rendered on each detected face.

---

## ✨ Features

- 🎥 **Real-time detection** from live webcam feed
- 🧠 **Deep Learning model** (`.hdf5`) trained to classify facial emotions
- 👤 **Face detection** using Haar Cascade Classifier (`haarcascade_frontalface_default.xml`)
- 📊 **7 Emotion classes**: Angry, Disgust, Fear, Happy, Neutral, Sad, Surprise
- ⚡ Fast and lightweight — runs efficiently on standard hardware

---

## 🗂️ Project Structure

```
├── emotion_detection.py          # Main script for real-time emotion detection
├── emotion_model.hdf5            # Pre-trained Keras deep learning model
├── haarcascade_frontalface_default.xml  # OpenCV Haar Cascade for face detection
└── README.md
```

---

## 🧠 How It Works

1. **Face Detection** — OpenCV's Haar Cascade classifier scans each video frame and identifies face regions.
2. **Preprocessing** — Detected face ROIs (Regions of Interest) are extracted, converted to grayscale, resized to `48×48` pixels, and normalized.
3. **Emotion Prediction** — The preprocessed face is passed into the pre-trained Keras CNN model (`emotion_model.hdf5`), which outputs probability scores across 7 emotion categories.
4. **Visualization** — The predicted emotion label and confidence are overlaid on the original video frame with a bounding box around the detected face.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| OpenCV (`cv2`) | Face detection & video frame processing |
| TensorFlow / Keras | Loading and running the emotion classification model |
| NumPy | Array manipulation and preprocessing |

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Programmer-surajit123/real-time-emotion-detection.git
cd real-time-emotion-detection
```

### 2. Install Dependencies

```bash
pip install opencv-python tensorflow numpy
```

> **Python 3.8+** is recommended. You can also use a virtual environment:
> ```bash
> python -m venv venv
> source venv/bin/activate   # On Windows: venv\Scripts\activate
> pip install opencv-python tensorflow numpy
> ```

### 3. Run the Application

```bash
python emotion_detection.py
```

Press **`Q`** to quit the webcam window.

---

## 📦 Requirements

```
opencv-python>=4.5
tensorflow>=2.6
numpy>=1.19
```

---

## 🎯 Emotion Classes

The model is trained to detect the following **7 emotions**:

| Label | Emotion |
|---|---|
| 0 | 😠 Angry |
| 1 | 🤢 Disgust |
| 2 | 😨 Fear |
| 3 | 😊 Happy |
| 4 | 😐 Neutral |
| 5 | 😢 Sad |
| 6 | 😲 Surprise |

---

## 🚀 Future Improvements

- [ ] Add support for video file input
- [ ] Display a real-time emotion probability bar chart
- [ ] Build a web app interface using Flask or Streamlit
- [ ] Improve model accuracy with a larger dataset
- [ ] Add multi-face tracking support

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Surajit Das**

<p>
  <a href="https://github.com/Programmer-surajit123">
    <img src="https://img.shields.io/badge/GitHub-Programmer--surajit123-181717?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
  &nbsp;
  <a href="https://www.linkedin.com/in/surajit-das-04142533b/">
    <img src="https://img.shields.io/badge/LinkedIn-Surajit%20Das-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>
  </a>
</p>

---

<p align="center">⭐ If you found this project helpful, please give it a star!</p>
