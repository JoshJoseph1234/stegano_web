# 🕵️ Steganography Web Tool

A web-based tool to **hide and extract secret messages or tracking URLs inside images** using **LSB (Least Significant Bit) steganography**, built with Flask and Python.  
Perfect for demonstrating ethical cybersecurity practices, this tool was developed as part of a **Cyber Cell internship**.

### 🔗 Live Demo  
👉 [https://stegano-web.onrender.com/]

---

## 🚀 Features

- 🔐 **Encode messages or links** into PNG images
- 🧠 **Decode and reveal hidden messages** from stego-images
- ⚠️ Automatically detects if decoded content is a link (like a Grabify URL) and offers a "Visit" button
- 🎨 **Dark hacker-themed UI** with neon green styling and animated video background
- 🔒 Fully safe and educational – **does not auto-trigger links**

---

## 🖼️ Use Cases

- Cybersecurity training & awareness
- Demonstrations of data hiding techniques
- Ethical hacking / OSINT simulation
- Internship/academic cybersecurity projects

---

## 📸 Screenshots

| Encoding Page | Decoding Page |
|---------------|----------------|
| ![Encode](./screenshots/encode.png) | ![Decode](./screenshots/decode.png) |

*(Add your screenshots inside a `/screenshots` folder if you'd like to include visuals)*

---

## 🧪 How It Works

The tool uses **Least Significant Bit (LSB)** manipulation to store binary-encoded text within the RGB values of pixels in an image. It supports:
- UTF-8 encoding
- Dynamic message length encoding
- URL detection on decode

---

## 🛠️ Tech Stack

| Component      | Technology      |
|----------------|-----------------|
| Backend        | Python, Flask   |
| Image Handling | Pillow (PIL)    |
| Frontend       | HTML, CSS       |
| UI Styling     | Dark CSS theme, embedded video background |
| Hosting        | Render.com      |

---

## 📂 Folder Structure

steganography-web/
│
├── app.py # Flask server
├── steganography.py # LSB encode/decode logic
├── requirements.txt
├── README.md
├── static/
│ ├── style.css
│ └── hacker-bg.mp4 # Background video
├── templates/
│ └── index.html
└── uploads/ # Temporary image uploads


---

## 💻 Run Locally

1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/steganography-web.git
   cd steganography-web
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py


⚠️ Disclaimer
This tool is intended for ethical, educational, and demonstrative purposes only. Do not use it for malicious purposes or to bypass privacy/security protections.