import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests

def load_lottiefile(filepath: str): #load the lottie file from the filepath
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url: str): #load the lottie file from the url
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_hello = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_lzpnnin5.json") 
# lottie_coding = load_lottiefile("sprinkle.json")

st.title("About")

# st.video('https://www.youtube.com/watch?v=Xw-zxQSEzqo&ab_channel=Decycle')
st_lottie( #create a lottie animation
    lottie_hello,
    height=500,
    width=500,
)
st.write("Repo: [Github](https://github.com/oddtomas/streamlit)")
st.write("Group Documentation: [Group Doc](https://docs.google.com/document/d/1-3lxVgDYyr1lMRG55oV1xZKveldzhXtComIsQEUj5L0)")

