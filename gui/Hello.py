import streamlit as st
import subprocess
import time
import websockets, asyncio

st.set_page_config(
    page_title="Welcome",
    page_icon="👋",
)

st.write("# Welcome to AI Gym Assistant👋")

st.sidebar.markdown("""
<style>
[data-testid="stSidebar"] {
  height: 300px; /* Adjust height as needed */
  overflow-y: auto; /* Enable scrolling if content exceeds height */
}
</style>
""", unsafe_allow_html=True)


# if st.sidebar.button("Voice Assistant"):
#
#
#     # Path to the Python executable within your virtual environment
#     python_executable = r"C:\Users\siddh\OneDrive\Desktop\gym_project\gym_project\Scripts\python.exe"
#
#     # Path to the Python file you want to run
#     python_file_path = r"C:\Users\siddh\OneDrive\Desktop\gym_project\gui\voice_assistant.py"
#     python_file_path_1 = r"C:\Users\siddh\OneDrive\Desktop\gym_project\gui\server.py"
#     python_file_path_2 = r"C:\Users\siddh\OneDrive\Desktop\gym_project\voice_assistant\Hello.py"
#
#     # Command to run the Python file using the Python executable from the virtual environment
#     python_cmd = [python_executable, python_file_path]
#     python_cmd_1 = [python_executable, python_file_path_1]
#     python_cmd_2 = [python_executable, '-m', 'streamlit', 'run', python_file_path_2]
#
#
#     # Open a new Command Prompt window and run the Python file
#     subprocess.Popen(['start', 'cmd', '/k'] + python_cmd_1, shell = True)
#     subprocess.Popen(['start', 'cmd', '/k'] + python_cmd, shell = True)
#     subprocess.Popen(['start', 'cmd', '/k'] + python_cmd_2, shell = True)
















