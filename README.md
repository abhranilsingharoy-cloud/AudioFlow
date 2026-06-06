# 🎧 AudioFlow

> A modern, lightweight web application that converts PDF documents into high-quality spoken audiobooks.

AudioFlow is designed to make reading more accessible by transforming your PDF files into listenable MP3 audiobooks in seconds. Featuring a clean, responsive user interface and robust text extraction capabilities, it offers customizable voice languages and adjustable reading speeds to suit your listening preferences.

---

## ✨ Features

- **Robust PDF Text Extraction**: Leverages `PyMuPDF` to accurately extract text, even from documents with complex layouts.
- **High-Quality Text-to-Speech**: Utilizes Google Text-to-Speech (`gTTS`) for natural-sounding audio generation.
- **Customizable Playback**: Supports multiple languages (English, Hindi, Spanish, French) and adjustable reading speeds (Normal/Slow).
- **Instant Processing & Download**: Seamlessly converts your file and initiates the MP3 download immediately upon completion.
- **Responsive Design**: A clean, professional interface built with HTML5, CSS3, and Flask, ensuring a smooth experience across devices.

## 🛠️ Tech Stack

- **Backend**: Python 3, Flask
- **Text Extraction**: PyMuPDF (`fitz`)
- **Audio Generation**: gTTS (Google Text-to-Speech)
- **Frontend**: HTML5, CSS3 (Vanilla)

## 📂 Project Structure

```text
AudioFlow/
├── app.py                  # Main Flask application logic
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── static/
│   └── style.css           # Frontend styling
└── templates/
    └── index.html          # UI template
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
2. **Select Language**: Choose your preferred language for the audio output (e.g., English, Hindi, Spanish, French).
3. **Select Speed**: Choose between "Normal" or "Slow" reading speeds.
4. **Convert**: Click the "Generate Audiobook" button.
5. **Listen**: The MP3 file will be downloaded automatically once processing is complete.

## 🛡️ Limitations

- **Scanned PDFs**: The current text extraction method does not support OCR. Scanned images or image-only PDFs will not yield text.
- **File Size**: Very large PDFs might experience longer processing times, as `gTTS` relies on an active internet connection to communicate with its API.

## 🤝 Contributing

Contributions make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open-source and available under the MIT License.
