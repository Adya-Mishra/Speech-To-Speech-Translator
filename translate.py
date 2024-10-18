import streamlit as st
import speech_recognition as sr
from googletrans import Translator, LANGUAGES
from gtts import gTTS
from playsound import playsound
import os
import time
import base64

# Initialize recognizer and Translator
r = sr.Recognizer()
translator = Translator()

# Streamlit app interface with custom design
st.set_page_config(page_title="Speech to Speech Translator", page_icon="🎤", layout="centered")

# Path to the image you want to use as the background
background_image_url = "speechtospeech.jpg"  # Ensure the image is in the same folder or provide a relative path

# Function to convert image to base64 (needed for inline display)
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Custom CSS to enhance UI and set the background image
st.markdown(f"""
    <style>
        /* Apply background image to the entire page */
        .stApp {{
            background-image: url('data:image/jpeg;base64,{get_image_base64(background_image_url)}');
            background-size: cover;
            background-position: center center;
            background-attachment: fixed;
            padding: 0;
        }}

        /* Styling for the main container with more transparency */
        .main {{
            background-color: rgba(0, 0, 0, 0.6); /* Darker background with transparency */
            padding: 3rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(10px); /* Add blur effect behind the container */
        }}

        /* Header styling with bold text and text shadow */
        .header {{
            font-size: 1.5rem;  /* Increased font size */
            color: #FF6347;  /* Tomato color for header */
            text-align: center;
            font-family: 'Monospace';
            font-weight: bold;
            text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.7);  /* Text shadow to make text pop */
            background-color: rgba(0, 0, 0, 0.7); /* Box background color */
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 1rem;
        }}
        
        /* Description styling with bold text and text shadow */
        .description {{
            padding: 2rem;
            font-size: 1rem;  /* Increased font size */
            text-align: center;
            color: #20B2AA; 
            font-family: 'Arial', sans-serif;
            font-weight: bold;
            text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.7);  /* Text shadow to make text pop */
            background-color: rgba(0, 0, 0, 0.7); /* Box background color */
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 2rem;
        }}

        /* Button styling */
        .btn-primary {{
            background-color: #0073e6;
            color: white;
            font-size: 1.2rem;
            padding: 1rem 2rem;
            border-radius: 5px;
            cursor: pointer;
            border: none;
        }}
        .btn-primary:hover {{
            background-color: #005bb5;
        }}
        
        /* Styling for select box */
        .select-box {{
            background-color: #e6f7ff;
            padding: 0.5rem;
            border-radius: 5px;
            border: 1px solid #ccc;
        }}
    </style>
""", unsafe_allow_html=True)

# App UI content
st.markdown('<div class="header">🎤 Speech to Speech Translator 🎤</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Speak in any language, and translate it into your chosen language!</div>', unsafe_allow_html=True)

# Dropdown to select target language
languages = list(LANGUAGES.values())
target_language = st.selectbox("Select target language for translation", languages, key="target_language", index=30, help="Select the language to which you want to translate your speech", label_visibility="collapsed")

# A button styled to look better
if st.button("Speak Now", key="speak_button", help="Click to start recording your speech", use_container_width=True):
    with sr.Microphone() as source:
        # Quickly adjust for ambient noise to improve recognition accuracy
        r.adjust_for_ambient_noise(source, duration=0.5)
        
        st.info("Listening... Please speak clearly.")
        try:
            # Listen continuously until the user stops speaking
            audio = r.listen(source, timeout=10, phrase_time_limit=5)
            st.info("Processing your speech...")

            # Recognize speech and detect the language
            speech_text = r.recognize_google(audio)
            detected_lang = translator.detect(speech_text).lang
            detected_lang_name = LANGUAGES.get(detected_lang, "Unknown")

            # Display recognized speech and detected language inside a box
            st.markdown(f'<div class="description">Recognized Speech: {speech_text}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="description">Detected Language: {detected_lang_name}</div>', unsafe_allow_html=True)

            if speech_text.lower() == "exit":
                st.write("Exiting...")
                st.stop()

            # Get the language code for the selected target language
            target_language_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(target_language)]

            # Translate the recognized speech into the selected target language
            translated_text = translator.translate(speech_text, src=detected_lang, dest=target_language_code).text
            st.markdown(f'<div class="description">Translated Text: {translated_text}</div>', unsafe_allow_html=True)

            # Convert the translated text to speech
            voice = gTTS(translated_text, lang=target_language_code)
            voice_file = "voice.mp3"
            voice.save(voice_file)
            

            # Remove the audio file after playing
            playsound(voice_file)
            os.remove(voice_file)

        except sr.UnknownValueError:
            st.error("Sorry, I could not understand you. Kindly repeat!")
        except sr.RequestError:
            st.error("Sorry, I could not request results from Google!")
        except sr.WaitTimeoutError:
            st.error("Listening timed out while waiting for phrase to complete. Please try again.")
        except Exception as e:
            st.error(f"An error occurred: {e}")