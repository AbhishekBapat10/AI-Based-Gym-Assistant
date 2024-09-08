import sounddevice as sd
import numpy as np
import tempfile
import os
from scipy.io.wavfile import write as write_wav
import webbrowser as wb
from load_model import pipe
import subprocess
import asyncio
import websockets
import conn
import mysql.connector
import time

async def ws_client(name):
    print("WebSocket: Client Connected.")
    url = "ws://localhost:8765"
    # Connect to the server
    async with websockets.connect(url) as ws:
        await ws.send(name)
        print("message sent")
        

send_message_list = ["True"]
def send_message():
    global send_message
    connection1 = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "ai_gym"
    )
    curr = connection1.cursor()
    # Execute the query to fetch the latest flag
    query = "SELECT flag FROM task ORDER BY id DESC LIMIT 1"
    curr.execute(query)
    result = curr.fetchone()  # Fetch only the latest row

    if result:
        latest_flag = result[0]
        print("Latest flag from database:", latest_flag)
        if latest_flag == "start":
            send_message_list.append("False")
        else:
            send_message_list.append("True")
    connection1.close()


# Function to record audio in real-time
def record_audio(max_duration = 3, sample_rate = 16000, silence_threshold = 500, max_silence_duration = 2):
    
    index = len(send_message_list) - 1
    if send_message_list[index] == "True":
        asyncio.run(ws_client("Listening"))
    time.sleep(1)
    # asyncio.run(ws_client("Listening"))
    print("Listening")
    
    audio_data = []
    silence_counter = 0
    
    while True:
        # Record a small chunk of audio
        chunk = sd.rec(int(1 * sample_rate), samplerate = sample_rate, channels = 1, dtype = np.int16)
        sd.wait()
        
        # Append the chunk to the ongoing audio data
        audio_data.extend(chunk.flatten())
        
        # Check if the sound level is below the threshold
        if np.max(np.abs(chunk)) < silence_threshold:
            silence_counter += 1
        else:
            silence_counter = 0
        
        # Check if the maximum duration or silence duration is reached
        if len(audio_data) / sample_rate >= max_duration or silence_counter >= max_silence_duration:
            break
    
    print("Recording finished.")
    return np.array(audio_data)

# Convert int16 audio data to raw PCM data
def int16_to_pcm(audio_data):
    return audio_data.tobytes()

# Save the audio to a temporary WAV file and return the file path
def save_audio_to_wav(audio_data, sample_rate, temp_dir):
    temp_file_path = os.path.join(temp_dir, "temp_audio.wav")
    write_wav(temp_file_path, sample_rate, audio_data)
    return temp_file_path

# Check if the audio signal is above a certain threshold
def is_sound_above_threshold(audio_data, threshold = 500):
    return np.max(np.abs(audio_data)) > threshold

# Perform automatic speech recognition on the recorded audio
def recognize_audio(audio_data, sample_rate):
    temp_dir = tempfile.mkdtemp()
    temp_wav_file = save_audio_to_wav(audio_data, sample_rate, temp_dir)
    result = pipe(temp_wav_file, generate_kwargs={"language": "english"})
    return result["text"]

# Record audio and perform automatic speech recognition
if __name__ == "__main__":
    try:
        while True:
            send_message()
            recorded_audio = record_audio()
            if is_sound_above_threshold(recorded_audio):
                start_time = time.time()
                result_text = recognize_audio(recorded_audio, sample_rate = 16000)
                end_time = time.time()
                index = len(send_message_list) - 1
                if send_message_list[index] == "True":
                    asyncio.run(ws_client(result_text))
                print("Results:", result_text)
                
                if "google".lower() in result_text.lower():
                    wb.open("https://www.google.com/")
                
                if "start".lower() in result_text.lower():
                    # pass
                    query = "insert into task (flag) values (%s)"
                    val = ("start",)
                    conn.cursor.execute(query, val)
                    conn.dataBase.commit()
                    print("start sent")
                    
                if "stop".lower() in result_text.lower():
                    # pass
                    query = "insert into task (flag) values (%s)"
                    val = ("stop",)
                    conn.cursor.execute(query, val)
                    conn.dataBase.commit()
                    print("stop sent")
                
                  
               
                if "sleep".lower() in result_text.lower():
                    break
                # time.sleep(end_time - start_time)
    
    
    except Exception as e:
        print(e)
      
