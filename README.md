# 🧠 Visual Context + Memory Agent

This project is a smart image classification system that uses **computer vision**, **OCR**, **reinforcement learning**, and **metadata analysis** to understand and organize images based on their context.

## 🔍 What It Does

The system processes any uploaded image and automatically classifies it into one of the following four categories:
- 🧑‍💼 **Work-related**
- 🧠 **Informational**
- 🖼️ **Personal/Memory**
- 🚫 **Advertisement/Junk**

### Features:
- Extracts metadata from images: **timestamp, text, faces, color histogram**
- Stores metadata in a local JSON database
- Uses a **Q-learning RL agent** to improve classification over time based on rewards
- Real-time dashboard using **Flask + Matplotlib**
- Dashboard only displays the **latest uploaded image**
- Accepts both local and internet images for classification

---

## 🚀 How to Run It

### 1. Clone this repo
```bash
git clone https://github.com/atharvachemte/Visual-Context-Memory-Agent.git
cd visual-agent2
