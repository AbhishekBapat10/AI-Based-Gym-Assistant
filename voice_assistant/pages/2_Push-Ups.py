
import streamlit as st
from model import pushup2
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

# st.sidebar.markdown(
#     f'<div class="exercise-section">Push-ups are a versatile exercise that targets multiple muscle groups, including the chest, shoulders, and triceps.</div>',
#     unsafe_allow_html = True)
# st.sidebar.write("\nHere are some tips for performing the Push-Ups:")
# st.sidebar.write("Step 1: Starting Position")
# st.sidebar.write("1. Begin in a plank position, hands shoulder-width apart, arms fully extended, and body straight from head to heels.")
# st.sidebar.write("**Step 2: Descent**")
# st.sidebar.write("2. Lower your body by bending your elbows, keeping them close to your sides.\n3. Lower until your chest nearly touches the ground, or as far as your strength allows.")
# st.sidebar.write("**Step 3: Pushing Up**")
# st.sidebar.write("4. Push through your palms to straighten your arms, returning to the starting position.")


st.title("Push-Ups 🧎")
# st.write("Push-ups are a classic bodyweight exercise that target your chest, shoulders, and triceps.")



async def ws_client_4():
 print("WebSocket: Client Connected.")
 url = "ws://localhost:8765"
 # Connect to the server
 async with websockets.connect(url) as ws_4:
  empty_element = st.sidebar.empty()
  while True:
   print("read to hear")
   msg = await ws_4.recv()
   if msg:
    empty_element.write(msg)
    speaker.Speak(msg)
    if "start".lower() in msg.lower():
     speaker.Speak("Starting Pushups")
     pushup2()
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


asyncio.run(ws_client_4())

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