import streamlit as st
import os
import argparse
from typing import Optional
from google.cloud import pubsub_v1
import time
from google.oauth2 import service_account
from google.cloud import storage
# from GeneratedStorybook import filled
# import GeneratedStorybook

# pdf test
# from fpdf import FPDF

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = storage.Client(credentials=credentials)

bucket = client.get_bucket("et-test-bucket")

st.set_page_config(page_title="SADA R&D Book Generator", page_icon="🤖")
# st.sidebar.title("Select a page above!")


st.title("Input text to generate your own book!")


if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

st.write("This is a GCP project utilizing GPT3 and Dalle-2 AI to generate text and images to form a book.")
my_input = st.text_input("Enter a prompt here to create your story!", st.session_state["my_input"])
submit = st.button("Submit")

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
         st.write(f"⏳ generating....")
         time.sleep(1)
         st.write("")
    
# check for blobs length
    # exec(open("GeneratedStorybook.py").read()) #pubsub to call this command?

bucket = client.get_bucket("et-test-bucket")
blobs = bucket.list_blobs()

collection = []
d = {}

if "filled" not in st.session_state:
    st.session_state["filled"] = False

def filled():        
    if len(d) == 20:
        st.session_state["filled"] = True
        print(len(d))

def list_blobs():
    """Lists all the blobs in the bucket."""

for blob in blobs:
        if "text_" in blob.name:
            print(blob.name)
            test_text = blob.download_as_string().decode("utf-8") 
            collection.append(test_text)

# for img in blobs:

        if "image_" in blob.name:
            print(blob)
            image = blob.download_as_bytes()
            collection.append(image)
            print(blob)

list_blobs()
d = {'image1': collection[0], 'text1': collection[10], 'image2': collection[1], 'text2': collection[11], 'image3': collection[2], 'text3': collection[12], 'image4': collection[3], 'text4': collection[13], 'image5': collection[4], 'text5': collection[14], 'image6': collection[5], 'text6': collection[15], 'image7': collection[6], 'text7': collection[16], 'image8': collection[7], 'text8': collection[17], 'image9': collection[8], 'text9': collection[18], 'image10': collection[9], 'text10': collection[19]}
filled()


# if st.session_state["filled"]:    
#     st.write(" your book is ready!")


def output():
    if st.session_state["submitted"] and st.session_state["filled"]: #change conditional to be if the generators are done/ send a pubsub?
# display in order of the keys
        st.markdown("""
<style>
.big-font {
    font-size:50px !important;
}
</style>
""", unsafe_allow_html=True)

        st.markdown('<p class="big-font">Here&#8217s your story!!</p>', unsafe_allow_html=True)
        st.write(d['text1'])
        st.image(d['image1'])
        st.write(d['text2'])
        st.image(d['image2'])
        st.write(d['text3'])
        st.image(d['image3'])
        st.write(d['text4'])
        st.image(d['image4'])
        st.write(d['text5'])
        st.image(d['image5'])
        st.write(d['text6'])
        st.image(d['image6'])
        st.write(d['text7'])
        st.image(d['image7'])
        st.write(d['text8'])
        st.image(d['image8'])
        st.write(d['text9'])
        st.image(d['image9'])
        st.write(d['text10'])
        st.image(d['image10'])
    else:
        with st.empty():
            for seconds in range(5): 
                st.write(".............")
                time.sleep(1)
                st.write("Nothing to see here......... yet! Submit your prompt to generate your book!")

if st.session_state["submitted"] and st.session_state["filled"]:
    output()
#else try to check dictionary length or blob again? and call output() if it's filled?
#create storage trigger to let me know when text and image 10 are ready?



