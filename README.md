🐄 Foot-and-Mouth Disease (FMD) Detector for Cattle using Computer Vision
📸 Overview
This project leverages computer vision and deep learning to help farmers and veterinary officers detect Foot-and-Mouth Disease (FMD) in cattle through images. The system is trained to recognize visible symptoms of FMD such as lesions on the mouth, hooves, and tongue, and then deployed in a user-friendly mobile/web app for real-time diagnosis support.

🚜 Problem Statement
Foot-and-Mouth Disease (FMD) is a highly contagious viral disease that affects livestock, leading to severe economic loss for farmers. Early detection is critical to control the spread and treat affected animals. However, access to veterinary care is limited in rural areas, and many cases go undiagnosed until it's too late.

This project aims to:

Empower farmers with AI-driven tools to perform preliminary diagnosis.

Assist vets and agricultural officers with a quick visual screening tool.

Reduce the economic impact of FMD through early detection.

🧠 What the Model Does
The trained model classifies images of cattle into two categories:

✅ Healthy (No signs of FMD)

❌ Infected (Signs of Foot-and-Mouth Disease present)

The model is trained on a curated dataset of cattle images with visible symptoms of FMD, using Convolutional Neural Networks (CNNs).

💻 Tech Stack

Component	Technology Used
Model Training	TensorFlow / Keras
Image Processing	OpenCV, Pillow
Deployment	Streamlit (Alt UI)
Hosting	 Streamlit Cloud
🚀 Features
📷 Upload or capture cattle images via camera

🔍 Real-time FMD detection using trained model

🧪 Visual indicators for suspected infection

🐄 Easy-to-use interface built for non-tech-savvy users

☁️ Deployed online—accessible from anywhere

