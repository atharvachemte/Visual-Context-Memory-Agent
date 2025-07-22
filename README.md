# 🧠 Visual Context + Memory Agent

This project is a smart image classification system that uses **computer vision**, **OCR**, **reinforcement learning**, and **metadata analysis** to understand and organize images based on their visual and contextual content.

---

## 🔍 What It Does

The system processes any uploaded image and automatically classifies it into one of the following four categories:

- 🧑‍💼 **Work-related**  
- 🧠 **Informational**  
- 🖼️ **Personal/Memory**  
- 🚫 **Advertisement/Junk**

### ✅ Features

- Extracts metadata: **timestamp**, **text (OCR)**, **faces**, **dominant colors**
- Uses **Q-learning RL agent** to improve classification accuracy with experience
- Stores metadata and classification results in a local **JSON database**
- Visualizes results via a **Flask + Matplotlib** dashboard
- Dashboard displays **only the latest uploaded image**
- Accepts images from both **local uploads** and **internet URLs**

---

## 🧠 How It Works

1. **Upload Image:** User uploads or pastes a URL via the web interface.
2. **Metadata Extraction:** Image is processed to extract faces (Haar cascades), text (Tesseract OCR), color histograms, and timestamps.
3. **Classification:** The image is classified into one of the four predefined categories.
4. **Reward System:**  
   - +2 for correctly classifying work  
   - +1 for personal memories  
   - −1 for misclassifying memories as junk  
   - −2 for treating memes as work  
   These rewards help the **RL agent** improve its decisions over time.
5. **Display:** The latest classification result and charts (category count, reward tracking) are displayed on the dashboard.

---

## 🚀 How to Run It

**Clone this repo**
```bash
git clone https://github.com/atharvachemte/Visual-Context-Memory-Agent.git
cd Visual-Context-Memory-Agent
