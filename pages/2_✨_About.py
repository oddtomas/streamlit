import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests

st.markdown('<a href="/" target="_self">Home</a>', unsafe_allow_html=True)
st.markdown('<a href="/About" target="_self">About</a>', unsafe_allow_html=True)
if st.session_state.get("finished", True):
    st.markdown('<a href="/SavedBook" target="_self">Finished BooK</a>', unsafe_allow_html=True)
    
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

st_lottie( #create a lottie animation
    lottie_hello,
    height=500,
    width=500,
)
st.write("Frontend Repo: [Github](https://github.com/oddtomas/streamlit)")
st.write("Backend Repo: [Github](https://github.com/ertrtx/backend-bookgenerator)")
st.write("Group Documentation: [Group Doc](https://docs.google.com/document/d/1-3lxVgDYyr1lMRG55oV1xZKveldzhXtComIsQEUj5L0)")
st.write("Devs: [Thomas](https://www.linkedin.com/in/thomas-nguyen-9665761a7/), [Eleonor](https://www.linkedin.com/in/eleonor-t-a041b122/), [Vita](https://www.linkedin.com/in/vitarabinovich/)")
st.write("Mentor: Bob Bae")
# st.video('https://www.youtube.com/watch?v=Xw-zxQSEzqo&ab_channel=Decycle')

# lottie_yoda = load_lottieurl("https://assets2.lottiefiles.com/animated_stickers/lf_tgs_fhiz0fdc.json")

# st.warning('This is a warning')

# yoda = st.empty()
# with yoda.container():
#     st_lottie( #create a lottie animation
#     lottie_yoda,
#     height=250,
#     width=250,
#     key="yoda",
# )


# submit = st.button("Submit") #set submit

# if submit: #if the submit button is pressed, do this stuff.
#     yoda.empty()
