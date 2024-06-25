import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import cv2
def opencamra():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video device.")
        exit()
    # Set video frame width and height (optional)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)
    # Loop to continuously get frame
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        # Display the resulting frame
        cv2.imshow('Camera', frame)
        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # Release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()
        # Open the default camera (usually the first camera available)


recognizer=sr.Recognizer()
engine=pyttsx3.init()

def processCommand(c):
    
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        speak("opening google")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
        speak("opening youtube")
    
    
        speak("opening Chatgpt")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/")
        speak("openinglinkedin")
    elif"open spotify" in c.lower():
        webbrowser.open("")
    elif "char kadam"in c.lower():
        # song=c.lower().split("")[1]
        # link= musiclibrary.music[song ]
        webbrowser.open("")
        speak("playing")
    elif "open camera" in c.lower():
        speak("opening camara")
        opencamra()
        
    else:
        pass


    pass

def speak(text):
    engine.say(text)
    engine.runAndWait()
if __name__=="__main__":
    speak("Initializing .... ")
    while True:
        r=sr.Recognizer()
        
        #recognize speech using 
        print("Recognizing")
        try:
          
            with sr.Microphone() as Source:
                print("Listning...")
                audio=r.listen(Source,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio)
            if (word.lower()=="hello"):
                speak("How can i help you")
                with sr.Microphone() as Source:
                    print("Jarvis Active...")
                    audio=r.listen(Source,timeout=2,phrase_time_limit=1)
                command=r.recognize_google(audio)

                processCommand(command)
                
            print(command)
        except Exception as e:
            print(e)