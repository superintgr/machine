import numpy as np
import sounddevice as sd
import time

# Function to generate a stereo sine wave tone
def generate_stereo_tone(frequency_left, frequency_right, duration, sample_rate=192000):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    tone_left = 0.5 * np.sin(2 * np.pi * frequency_left * t)
    tone_right = 0.5 * np.sin(2 * np.pi * frequency_right * t)
    stereo_tone = np.vstack((tone_left, tone_right)).T
    return stereo_tone

# Function to play a stereo tone
def play_tone(frequency_left, frequency_right, duration):
    sample_rate = 192000  # 192kHz
    tone = generate_stereo_tone(frequency_left, frequency_right, duration, sample_rate)
    sd.play(tone, samplerate=sample_rate, channels=2)
    sd.wait()

# Timer with customizable announcements and urgency profiles
def countdown_timer(total_duration, announcements, urgency_profile):
    urgency_tones = {
        "keep me focused": [(660, 880), (2, 1)],
        "keep relaxed but awake": [(440, 440), (1, 2)],
        "stochastic awareness": [(550, 660), (1, 1.5)],
        "intermittent breathing between moments": [(330, 330), (2, 3)],
        "constant glide guide": [(220, 220), (3, 3)],
        "only last few minutes": [(880, 880), (1, 0.5)]
    }
    
    print("Timer started for {} seconds.".format(total_duration))
    
    for announcement in announcements:
        time.sleep(announcement['time'])
        freq_left, freq_right = urgency_tones[urgency_profile][0]
        duration = urgency_tones[urgency_profile][1][0 if announcement['relative'] else 1]
        play_tone(freq_left, freq_right, duration)
        print(announcement['message'])
    
    # Final announcement at the end of the timer
    time.sleep(total_duration - sum(a['time'] for a in announcements))
    freq_left, freq_right = urgency_tones[urgency_profile][0]
    duration = urgency_tones[urgency_profile][1][1]
    play_tone(freq_left, freq_right, duration)
    print("Timer complete!")

# Customize your timer here
total_duration = 15 * 60  # Total duration in seconds (15 minutes)
announcements = [
    {'time': 10 * 60, 'message': "10 minutes have passed. 5 minutes remaining.", 'relative': True},
    {'time': 4 * 60, 'message': "14 minutes have passed. 1 minute remaining.", 'relative': True}
]
urgency_profile = "keep me focused"

countdown_timer(total_duration, announcements, urgency_profile)
