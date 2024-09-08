import streamlit as st
from model import deadlift
import websockets, asyncio
import time
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")


page = []
st.sidebar.empty()

st.sidebar.markdown(
 """
 <style>
	 .exercise-section {
		 background-color: #000000;
		 padding: 20px;
		 border-radius: 10px;
		 box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
	 }
 </style>
 """,
 unsafe_allow_html = True
)

st.title("Deadlift 🏋️‍♂️")
# st.write("Deadlift is a great exercise for building strength in your lower back, glutes, and hamstrings.")
# st.sidebar.markdown(
#  f'<div class="exercise-section">Deadlift is a great exercise for building strength.</div>',
#  unsafe_allow_html = True)

# st.sidebar.write("")
# st.sidebar.write("\nHere are some tips for performing the Deadlift:")
# st.sidebar.write(
#  "**Step 1: Set Up**.\n1. Stand on your feet shoulder-width apart, toes pointing forward.\n2. The barbell should be over the middle of your feet.")
# st.sidebar.write("**Step 2: Grip**")
# st.sidebar.write(
#  "3. Bend at the hips and knees to grasp the barbell with an overhand grip (palms facing you) or mixed grip (one palm facing you, one away).")
# st.sidebar.write("**Step 3: Stance**")
# st.sidebar.write(
#  "4. Your hands should be just outside your knees.\n5. Keep your back straight, chest up, and shoulders back.")
# st.sidebar.write("**Step 5: Lowering**")
# st.sidebar.write(
#  "9. Reverse the movement, pushing your hips back first.\n10. Lower the barbell with control, keeping it close to your body.")



async def ws_client_1():
 print("WebSocket: Client Connected.")
 url = "ws://localhost:8765"
 # Connect to the server
 async with websockets.connect(url) as ws_1:
  empty_element = st.sidebar.empty()
  while True:
   print("read to hear")
   msg = await ws_1.recv()
   if msg:
    empty_element.write(msg)
    speaker.Speak(msg)
    if "start".lower() in msg.lower():
     speaker.Speak("Starting Deadlift")
     deadlift()
    if "Home".lower() in msg.lower():
     page.append("Home")
     print("executed successfully")
     break
    if "deadlift".lower() in msg.lower():
     page.append("deadlift")
     print("executed successfully")
     break
    if "biceps".lower() in msg.lower():
     page.append("biceps")
     print("executed successfully")
     break
    if "pushups".lower() in msg.lower():
     page.append("pushups")
     print("executed successfully")
     break
    if "squats".lower() in msg.lower():
     page.append("squat")
     print("executed successfully")
     break
   else:
    empty_element.write("Message not received")
   time.sleep(1)
   
   


asyncio.run(ws_client_1())

index = len(page) - 1
if page[index] == "deadlift":
 speaker.Speak("Selecting Deadlift")
 st.switch_page("pages/1_Deadlift.py")
if page[index] == "biceps":
 speaker.Speak("Selecting Bicep Curl")
 st.switch_page("pages/3_Bicep Curl.py")
if page[index] == "pushups":
 speaker.Speak("Selecting Pushups ")
 st.switch_page("pages/2_Push-Ups.py")
if page[index] == "squat":
 speaker.Speak("Selecting Squats")
 st.switch_page("pages/4_Squat.py")
if page[index] == "Home":
 speaker.Speak("Selecting Home")
 st.switch_page("Home.py")
