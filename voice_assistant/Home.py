
import streamlit as st
import websockets, asyncio
import time
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

st.set_page_config(
    page_title="Welcome",
    page_icon="👋",
)


page = []



st.write("# Welcome to AI Gym Voice Assistant")



async def ws_client_3():
 print("WebSocket: Client Connected.")
 url = "ws://localhost:8765"
 # Connect to the server
 async with websockets.connect(url) as ws_3:
  empty_element = st.sidebar.empty()
  while True:
   print("read to hear")
  
   msg = await ws_3.recv()
   
   if msg:
    empty_element.write(msg)
    speaker.Speak(msg)
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
  
  
   
   

st.sidebar.write("Waiting for commands...")
asyncio.run(ws_client_3())


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