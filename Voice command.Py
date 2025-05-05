import speech_recognition as sr

def listen_for_command():
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    
    # Set up the microphone as the audio source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening for your command (speak now)!")
        audio = recognizer.listen(source)
    
    try:
        # Use Google's speech recognition service to convert audio to text
        command = recognizer.recognize_google(audio)
        command = command.lower()  # Normalize the command to lowercase
        print(f"Recognized command: {command}")
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that!")
        command = ""
    except sr.RequestError as e:
        print(f"Could not request results from the speech recognition service; {e}")
        command = ""
    
    return command

# Example game action mappings (replace with your game's methods)
def perform_game_action(command):
    if command == "jump":
        print("Player jumps!")
        # player.jump()  # Example: Call your player's jump function
    elif command == "shoot":
        print("Player shoots!")
        # player.shoot()  # Example: Call your player's shoot function
    elif command == "move left":
        print("Player moves left!")
        # player.move_left()  # Example: Call your player's move_left function
    elif command == "move right":
        print("Player moves right!")
        # player.move_right()  # Example: Call your player's move_right function
    else:
        print("No valid command recognized.")

if __name__ == "__main__":
    # Listen for a voice command
    command = listen_for_command()
    
    # Map and perform the in-game action associated with the command
    perform_game_action(command)
