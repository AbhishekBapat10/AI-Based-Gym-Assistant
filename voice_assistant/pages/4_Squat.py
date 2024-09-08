
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
        unsafe_allow_html=True
    )

# st.sidebar.markdown(
#                 f'<div class="exercise-section">Squat is an excellent exercise for building leg strength, targeting the quadriceps, hamstrings, and glutes.</div>',
#             unsafe_allow_html = True)
# st.sidebar.write("**Step 1: Stand Tall**\n 1. Stand with your feet shoulder-width apart, toes pointed slightly outward.")
# st.sidebar.write("**Step 2: Lowering**")
# st.sidebar.write("2. Push your hips back and bend your knees, lowering your body as if sitting into a chair.")
# st.sidebar.write("**Step 3: Depth**")
# st.sidebar.write("3. Go as low as your mobility allows, ideally until your thighs are at least parallel to the ground.")
# st.sidebar.write("**Step 4: Rising**")
# st.sidebar.write("4. Push through your heels and straighten your legs to return to the starting position.")

st.title("Squat 🏋️‍♂️")
# st.write("Squats are the key to strong legs and a firm lower body.")

async def ws_client_6():
 print("WebSocket: Client Connected.")
 url = "ws://localhost:8765"
 # Connect to the server
 async with websockets.connect(url) as ws_6:
  empty_element = st.sidebar.empty()
  while True:
   print("read to hear")
   msg = await ws_6.recv()
   if msg:
    empty_element.write(msg)
    speaker.Speak(msg)
    if "start".lower() in msg.lower():
     speaker.Speak("Starting Squats")
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
 


asyncio.run(ws_client_6())

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