# interview_helper.py
import pyautogui
import pyperclip
import time
import webbrowser
import keyboard
import speech_recognition as sr

CHATGPT_INPUT_COORDS = (1017, 889)  # Adjust to your setup

# Open ChatGPT in the default browser
webbrowser.open("https://chat.openai.com/")
time.sleep(5)  # Wait for the page to load

def transcribe_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening... Please speak clearly.")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

    try:
        text = recognizer.recognize_google(audio)
        print("Transcription:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio. Try speaking clearly.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""

def paste_text(text):
    # Add the interview question prompt to guide ChatGPT’s response
    prompt = f"This is an interview question: '{text}'. Please give me a concise answer so I can say it to the interviewer."
    pyperclip.copy(prompt)
    print(f"Text to send: {prompt}")

    print("Activating browser window...")
    pyautogui.hotkey("alt", "tab")
    time.sleep(1)

    print("Ensuring ChatGPT text input box is active...")
    pyautogui.click(*CHATGPT_INPUT_COORDS)
    time.sleep(0.5)

    print("Pasting text...")
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.press("enter")
    print("Text sent to ChatGPT.")
    time.sleep(2)
def main():
    print("Press 'left Shift' to start transcription and send to ChatGPT...")
    while True:
        if keyboard.is_pressed('shift'):
            print("Left Shift pressed, starting transcription...")
            text = transcribe_audio()
            if len(text) > 5:  # Avoid sending if transcription is too short
                paste_text(text)
            else:
                print("Transcription too short or unclear; not sending.")
            time.sleep(0.5)
            print("Press 'left Shift' to transcribe and send another input...")

if __name__ == "__main__":
    main()
