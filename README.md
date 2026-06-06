# 🎧 AudioFlow AI

> A modern, advanced web application that converts PDF documents into highly realistic, neural-powered spoken audiobooks.

AudioFlow is engineered to make reading more immersive by transforming your PDF files into listenable MP3 audiobooks in seconds. Featuring a premium, dark-mode glassmorphism interface and a robust AI text-to-speech engine, it delivers unparalleled voice accuracy and natural intonation.

---

## ✨ Features

- **Ultra-Realistic Neural TTS**: Upgraded to use **Microsoft Edge Neural TTS (`edge-tts`)** for extremely natural-sounding, high-fidelity AI voices (Aria, Swara, Elvira, Denise) that outperform traditional TTS models.
- **Intelligent Text Processing Engine**: Automatically repairs hyphenated words broken across lines and cleans extracted text for flawless and continuous pronunciation.
- **Premium Glassmorphism UI**: A stunning, modern, and interactive frontend complete with animated gradient orbs, frosted glass components, and an AI-wave loader.
- **Robust PDF Text Extraction**: Leverages `PyMuPDF` to accurately extract text, even from documents with complex layouts.
- **Customizable Playback**: Supports multiple languages (English, Hindi, Spanish, French) and adjustable reading speeds.

## 🛠️ Tech Stack

- **Backend**: Python 3, Flask
- **Text Extraction**: PyMuPDF (`fitz`)
- **AI Audio Generation**: edge-tts (Microsoft Neural TTS)
- **Frontend**: HTML5, CSS3 (Custom Glassmorphism + Phosphor Icons)

## 📂 Project Structure

```text
AudioFlow/
├── app.py                  # Main Flask application logic (AI TTS + Text Engine)
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── static/
│   └── style.css           # Premium glassmorphism styles and animations
└── templates/
    └── index.html          # UI template with custom SVG icons
```

## ⚙️ Installation & Setup

Follow these steps to run the application locally on your machine.

### 1. Clone the Repository
```bash
git clone https://github.com/abhranilsingharoy-cloud/AudioFlow.git
cd AudioFlow
```

### 2. Create a Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```

### 5. Access the Web App
Open your web browser and navigate to: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## 📖 Usage Guide

1. **Upload PDF**: Click the upload box or drag and drop your PDF file into the designated area.
2. **Select Neural Voice**: Choose your preferred AI voice (e.g., English - Aria, Hindi - Swara).
3. **Select Speed**: Choose between "Normal" or "Slow" synthesis speeds.
4. **Synthesize Audio**: Click the "Synthesize Audio" button to let the neural engine process your document.
5. **Listen**: The high-quality MP3 file will be downloaded automatically once processing is complete.

## 🛡️ Limitations

- **Scanned PDFs**: The current text extraction method does not support OCR. Scanned images or image-only PDFs will not yield text.
- **File Size**: Very large PDFs might experience longer processing times, as the Neural TTS engine communicates with the cloud to synthesize the high-fidelity audio.

## 🤝 Contributing

Contributions make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open-source and available under the MIT License.

---

<p align="center">
  <b>Designed and Developed by Abhranil Singha Roy</b>
</p>
