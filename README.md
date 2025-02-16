# 🚦  Vehicle Count Using Computer Vision  

## 📌 Project Overview  
This project utilizes **computer vision and background subtraction algorithms** to detect and count moving vehicles in real-time. Using **OpenCV’s createBackgroundSubtractorMOG2()**, the system efficiently removes background noise and identifies vehicles on the road. The input is a real-time video (`video.mp4`), and the output displays the total vehicle count with live tracking.  

## 🔍 Features  
- **Real-Time Vehicle Detection** – Uses background subtraction and contour detection.  
- **Vehicle Counting** – Tracks vehicles crossing a predefined detection line.  
- **Noise Reduction** – Implements morphological operations for improved accuracy.  

## 🛠 Technology Stack  
- **Python**  
- **OpenCV**  
- **NumPy**  

## 📂 Project Files  
- `video.mp4` → Input traffic footage for vehicle detection.  
- `main.py` → Detects and tracks vehicles in real time.  

## 🚀 How It Works  
1. **Background Subtraction:** Removes unwanted background to isolate moving objects.  
2. **Contour Detection:** Identifies vehicle boundaries using `cv2.findContours()`.  
3. **Vehicle Counting:** Tracks vehicles crossing a predefined line.  
4. **Live Output Display:** Shows the vehicle count in real-time.  

## 🎯 Use Cases  
✅ **Smart Traffic Management** – Helps authorities analyze congestion and plan road systems.  
✅ **Automated Traffic Monitoring** – Reduces the need for manual vehicle counting.  
✅ **Smart City Integration** – Can be integrated into AI-driven city planning systems.  

## 📸 Demo  
![image](https://github.com/user-attachments/assets/7b787868-f68d-46ca-851f-cf964867c8c1)


## 📥 Installation & Usage  
1️⃣ Install dependencies:  
```bash
pip install opencv-python numpy
pip install opencv-contrib-python
