import streamlit as st
import os
import argparse
from typing import Optional
from google.cloud import pubsub_v1
import time




st.set_page_config(page_title="Multipage APP", page_icon="✌")
st.sidebar.title("Select a page above!")


st.title("Input text to generate your own book!")


if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

st.write("This is a GCP project utilizing GPT3 and Dalle-2 AI to generate text and images to form a book.")
my_input = st.text_input("Enter a prompt here to create your story!", st.session_state["my_input"])
submit = st.button("Submit")
st.video('https://www.youtube.com/watch?v=Xw-zxQSEzqo&ab_channel=Decycle')

if "submitted" not in st.session_state:
    st.session_state["submitted"] = False

if submit:
    st.session_state["submitted"] = True
    st.session_state["my_input"] = my_input
    # st.write("You entered:", my_input)
    with st.empty():
     for seconds in range(5): #make this range wait for a pubsub message?
         st.write(f"⏳ {seconds} seconds have passed")
         time.sleep(1)
     st.write("✔️ your book is ready!")
    #pass all of this to Eleonors text generator?
    #then those inputs are saved to a bucket that is retrieved by Vita's image generator
    #this script then pulls those seperated bucket items into a booklike format demo'd on the BucketText.py page.

