# 🎤 Speech-to-Speech Translator

A user-friendly, multilingual speech translation application built using Streamlit, Google Translate API, SpeechRecognition, gTTS, and Playsound. This app allows users to speak in one language and receive real-time translation in both text and audio format in a language of their choice.

## 📝 Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [How It Works](#how-it-works)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [License](#license)

## 📖 Introduction
The **Speech-to-Speech Translator** app is designed to help users translate spoken words into another language, making communication seamless across different languages. This tool is particularly useful for travelers, language learners, and people communicating across different linguistic backgrounds.

## ✨ Features
- 🎙 **Real-Time Speech Recognition**: Recognizes speech from the user in real-time.
- 🌍 **Multilingual Support**: Supports translation into multiple languages using the Google Translate API.
- 📢 **Speech Playback**: Converts the translated text back into speech using the gTTS library.
- 🖼 **Custom UI**: A sleek, visually appealing interface with a custom background image and design enhancements.
- ⏸ **Ambient Noise Adjustment**: Automatically adjusts for ambient noise to enhance speech recognition accuracy.
- 🛠 **Simple User Experience**: Users can select their desired target language and translate their speech with just one click.

## 🛠 Technologies Used
- **Streamlit**: Framework for creating the web-based UI.
- **SpeechRecognition**: For recognizing and capturing speech from the microphone.
- **Google Translate API**: For detecting language and translating speech.
- **gTTS (Google Text-to-Speech)**: For converting the translated text back into speech.
- **Playsound**: For playing the translated speech as an audio output.
- **Base64**: For displaying background images inline.

## ⚙️ How It Works
1. **Speech Recognition**: The app captures the user's speech using the microphone.
2. **Language Detection**: The spoken text is converted to text, and the source language is detected automatically using Google Translate.
3. **Translation**: The recognized text is translated into the user's selected target language.
4. **Text-to-Speech**: The translated text is converted into speech using Google Text-to-Speech.
5. **Audio Playback**: The speech is played back to the user.

## 📦 Setup and Installation
1. **Clone the Repository**:
   
   ```bash
   git clone https://github.com/your-username/speech-to-speech-translator.git
   cd speech-to-speech-translator

3. **Install Required Dependencies**:

   ```bash
   pip install -r requirements.txt

## 🚀 Usage:
1. Run the app using:
   
   ```bash
   streamlit run translate.py
   
2. Choose the target language from the dropdown.
3. Click "Speak Now" and start speaking. The app will listen to your speech and process it.
4. The app will display the recognized speech, detected language, and translated text.
5. The translated speech will be played as audio output in the selected language.

## 📄 License:
This project is licensed under the MIT License.

