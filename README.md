## 📌 Overview
This is a mini project I built to practice **OpenCV** in Python.  
The program uses **YCrCb color space**, **contour detection**, and **convex hull / convexity defects** to estimate the number of fingers shown in front of the camera.

## 🛠 Requirements
- Python 3.x  
- OpenCV (`pip install opencv-python`)  
- (Optional) NumPy, Math (already included in Python standard library for math)

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/taco29/Finger-Tracking.git
   cd Finger-Tracking
   ```
2. Run the script:
   python FingerTracking.py
3. Show your hand in front of the camera.
   Press q to quit.
## 📸 Demo
<img width="633" height="473" alt="demo" src="https://github.com/user-attachments/assets/5931bb1e-5843-4b26-a759-b065fafd2476" />

## 🎯 Features
- Real-time skin detection with YCrCb color space
- Mask smoothing & cleanup using Gaussian blur & morphological operations
- Finger counting using convex hull & convexity defects

## 📚 Purpose
- This project is only for learning and practicing OpenCV.
- It can be extended into gesture recognition or human-computer interaction projects.
