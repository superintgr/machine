possible issues : [data is one dimensional while channels available are two, timer is predefined to show 15 mins where it should adjust based on given profile, there should be specifications in regards to how the reminders be scheduled]

import numpy as np
import sounddevice as sd
import time

# Function to generate a sine wave tone
def generate_tone(frequency, duration, sample_rate=192000):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    tone = 0.5 * np.sin(2 * np.pi * frequency * t)
    return tone

# Function to play a tone
def play_tone(frequency, duration):
    sample_rate = 192000  # 192kHz
    tone = generate_tone(frequency, duration, sample_rate)
    sd.play(tone, samplerate=sample_rate, channels=2)
    sd.wait()

# Timer with audio notifications
def countdown_timer(duration):
    print("Timer started for 15 minutes.")
    
    # Notify at the start
    play_tone(440, 1)  # A4 tone (440 Hz) for 1 second
    
    # Wait for the first notification (e.g., at 10 minutes)
    time.sleep(10 * 60)  # 10 minutes in seconds
    play_tone(550, 1)  # C#5 tone (550 Hz) for 1 second
    
    # Wait for the final notification (e.g., at 14 minutes)
    time.sleep(4 * 60)  # 4 more minutes in seconds
    play_tone(660, 1)  # E5 tone (660 Hz) for 1 second
    
    # Final wait until the end
    time.sleep(1 * 60)  # 1 more minute in seconds
    play_tone(880, 2)  # A5 tone (880 Hz) for 2 seconds

# Set the timer duration to 15 minutes (900 seconds)
countdown_timer(15 * 60)
