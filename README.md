# InterviewHelper
# InterviewHelper

**InterviewHelper** is a Python-based tool designed to help users prepare for interviews by automating transcription of spoken questions and sending them to ChatGPT for response suggestions. 

## Features
- Listens to and transcribes spoken input
- Automates prompt creation and sends text to ChatGPT
- Provides concise, generated responses to assist in interview practice

## Installation
- Clone the repository:
  ```bash
  git clone https://github.com/yourusername/InterviewHelper.git

Install required packages:
  ```bash
pip install pyautogui pyperclip keyboard SpeechRecognition
```

## Usage
Make sure to adjust the CHATGPT_INPUT_COORDS in the script based on your screen resolution and ChatGPT input box position.
Run the script:
bash ```
python interview_helper.py
```
Press Left Shift to begin audio transcription.
After speaking, the transcribed text will be pasted into the ChatGPT input box as a prompt for an interview response.
Script Details
transcribe_audio(): Captures and transcribes audio from the microphone.
paste_text(text): Formats and pastes the transcribed text into ChatGPT.
main(): Initiates the transcription process when Left Shift is pressed.
Requirements
Python 3.x
Libraries: pyautogui, pyperclip, keyboard, SpeechRecognition
