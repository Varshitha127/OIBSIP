import speech_recognition as sr
import pyttsx3
import datetime
import smtplib
import requests
import threading
import pywhatkit

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def listen(timeout=5):
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=timeout)
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print("User said:", query)
            return query.lower()
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return ""

def speak(text):
    engine.say(text)
    engine.runAndWait()

def send_email(receiver_email, subject, body):
    # Enter your email credentials
    sender_email = "lakkireddyvarshithareddy@gmail.com"  
    sender_password = "varshitha2005"     
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, receiver_email, message)
        server.quit()
        print("Email sent successfully")
    except smtplib.SMTPException as e:
        print("Error sending email:", str(e))
    except Exception as e:
        print("Unexpected error:", str(e))

def set_reminder(reminder_text, reminder_time):
    try:
        # Parse reminder time
        if "minutes" in reminder_time:
            minutes = int(reminder_time.split()[0])
            reminder_time_obj = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
        elif ":" in reminder_time:
            reminder_time_obj = datetime.datetime.strptime(reminder_time, "%H:%M")
        else:
            raise ValueError("Invalid time format. Please use 'HH:MM' or specify minutes.")
        
        current_time = datetime.datetime.now().replace(second=0, microsecond=0)
        if reminder_time_obj < current_time:
            print("Reminder time should be in the future")
            return

        delay = (reminder_time_obj - current_time).seconds
        reminder_timer = threading.Timer(delay, speak, args=[reminder_text])
        reminder_timer.start()
        print(f"Reminder set for {reminder_time_obj.strftime('%H:%M')}")
    except ValueError as e:
        print("Error setting reminder:", str(e))

def get_weather(city):
    
    api_key = "20362339eb365e9833713a824810cf01"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        temperature_celsius = temperature - 273.15
        return f"The weather in {city} is {weather_description}. The temperature is {temperature_celsius:.1f} degrees Celsius."
    else:
        return "Unable to fetch weather information."

def process_command(command):
    current_hour = datetime.datetime.now().hour
    if "send email" in command:
        speak("Who is the receiver?")
        receiver = listen()
        speak("What is the subject?")
        subject = listen()
        speak("What is the body of the email?")
        body = listen()
        send_email(receiver, subject, body)
    elif "set reminder" in command:
        speak("What should I remind you about?")
        reminder_text = listen()
        speak("At what time should I remind you? Please specify in HH:MM format or say 'Remind me in X minutes'.")
        reminder_time = listen()
        set_reminder(reminder_text, reminder_time)
    elif "weather update" in command:
        speak("Which city's weather would you like to know?")
        city = listen()
        weather_info = get_weather(city)
        speak(weather_info)
    elif any(greet in command for greet in ["good morning", "good afternoon", "good evening", "good night"]):
        if current_hour < 12:
            speak("Good morning!")
        elif 12 <= current_hour < 18:
            speak("Good afternoon!")
        elif 18 <= current_hour < 22:
            speak("Good evening!")
        else:
            speak("Good night!")
    elif "login whatsapp" in command:
        speak("Opening WhatsApp Web...")
        pywhatkit.sendwhatmsg_instantly("+918466000399", "Hello from Python!")
    elif "play youtube" in command:
        speak("What should I search on YouTube?")
        search_query = listen()
        speak(f"Playing {search_query} on YouTube...")
        pywhatkit.playonyt(search_query)
    elif "play song" in command:
        speak("What song would you like to play?")
        song_name = listen()
        speak(f"Playing {song_name}...")
        pywhatkit.playonyt(song_name)
    elif "stop" in command:
          speak("Have a nice day! Goodbye!")
          exit()

# Main loop
while True:
    query = listen()
    if query:
        process_command(query)
