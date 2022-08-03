import streamlit as st
import os
import argparse
from typing import Optional
from google.cloud import pubsub_v1
import time
from google.oauth2 import service_account
from google.cloud import storage
# pdf test
# from fpdf import FPDF

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = storage.Client(credentials=credentials)

bucket = client.get_bucket("et-test-bucket")

st.set_page_config(page_title="Multipage APP", page_icon="✌")
# st.sidebar.title("Select a page above!")


st.title("Input text to generate your own book!")


if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

st.write("This is a GCP project utilizing GPT3 and Dalle-2 AI to generate text and images to form a book.")
my_input = st.text_input("Enter a prompt here to create your story!", st.session_state["my_input"])
submit = st.button("Submit")
st.video('https://www.youtube.com/watch?v=Xw-zxQSEzqo&ab_channel=Decycle')

def write_to_file(text):
    with open("prompt.txt", "w") as f:
        f.write(text)

def upload_file(file_path):
    blob = bucket.blob(file_path)
    blob.upload_from_filename(file_path)


if "submitted" not in st.session_state:
    st.session_state["submitted"] = False

if submit:
    st.session_state["submitted"] = True
    st.session_state["my_input"] = my_input
    write_to_file(st.session_state["my_input"])
    upload_file("prompt.txt")
    with st.empty():
     for seconds in range(5): #make this range wait for a pubsub message?
         st.write(f"⏳ {seconds} seconds have passed")
         time.sleep(1)
     st.write("✔️ your book is ready!")



