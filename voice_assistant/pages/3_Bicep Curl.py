
import streamlit as st
import websockets, asyncio
from bicep import bicep
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
#   f'<div class="exercise-section">Bicep Curl is a fantastic exercise for strengthening your biceps and improving upper arm strength.</div>',
#   unsafe_allow_html = True)
# st.sidebar.write("**Step 1: Starting Position**")
# st.sidebar.write(
#   "1. Stand with feet shoulder-width apart, holding dumbbells in each hand, arms fully extended, and palms facing forward.")
# st.sidebar.write("**Step 2: Curl**")
# st.sidebar.write(
#   "2. Keeping your upper arms stationary, exhale and curl the weights while contracting your biceps.\n3. Continue until the dumbbells are at shoulder level.")
# st.sidebar.write("**Step 3: Lowering**")
# st.sidebar.write("4. Inhale and slowly begin to lower the dumbbells back to the starting position.")

st.title("Bicep Curls 💪")
# st.write("Bicep Curls help sculpt and strengthen your arm muscles.")

async def ws_client_5():
 print("WebSocket: Client Connected.")
 url = "ws://localhost:8765"
 # Connect to the server
 async with websockets.connect(url) as ws_5:
  empty_element = st.sidebar.empty()
  while True:
   print("read to hear")
   msg = await ws_5.recv()
   if msg:
    empty_element.write(msg)
    speaker.Speak(msg)
    if "start".lower() in msg.lower():
     speaker.Speak("Starting Bicep Curl")
     bicep()
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


asyncio.run(ws_client_5())

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