import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests
import webbrowser
import streamlit as st
from google.oauth2 import service_account
from google.cloud import storage
from google.cloud import pubsub_v1
import os
from concurrent.futures import TimeoutError
import time

#USE FOR NAVBAR?

if "finished" not in st.session_state: #set the session state to be False
    st.session_state["finished"] = False

def load_lottiefile(filepath: str): #load the lottie file from the filepath
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url: str): #load the lottie file from the url
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_hello = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_q77jpumk.json") 
# lottie_coding = load_lottiefile("sprinkle.json")
lottie_yoda = load_lottieurl("https://assets2.lottiefiles.com/animated_stickers/lf_tgs_fhiz0fdc.json")


def getToFlask(prompt): 
    BASE = "http://34.172.48.39:5000/"
    # print("this is the passed prompt:",prompt)
    frontEndPrompt = prompt
    try:
        response = requests.get(BASE + "book/"+ frontEndPrompt,timeout=10) #GET is blocking, so we use a timeout
        if (response.status_code == 200):
            print("The request was a success!")
    # Code here will only run if the request is successful
        elif (response.status_code == 404):
            print("Result not found!")        
    except requests.exceptions.ReadTimeout: 
        pass
    # response = requests.get(BASE + "book/"+ frontEndPrompt)
    # response = requests.get(BASE + prompt)



# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.set_page_config(page_title="SADA R&D Book Generator", page_icon="🤖") #change browser tab title

st.markdown('<a href="/" target="_self">Home</a>', unsafe_allow_html=True)
st.markdown('<a href="/About" target="_self">About</a>', unsafe_allow_html=True)
def navFinishedBook():
    if st.session_state.get("finished", True):
        st.markdown('<a href="/SavedBook" target="_self">Finished BooK</a>', unsafe_allow_html=True)
# exec(open("GeneratedStorybook.py").read()) #execute the GeneratedStorybook.py file

st.title("SADA R&D Book Generator") #change page title

# 

if "my_input" not in st.session_state: #set the session state to be empty
    st.session_state["my_input"] = ""

st.write("This is a GCP project utilizing GPT3 and Dalle-2 AI to generate text and images to form your own custom book.")

st_lottie( #create a lottie animation
    lottie_hello,
    height=500,
    width=500,
)

my_input = st.text_input("Enter a prompt here to create your story!", st.session_state["my_input"]) #change prompt to be a text input and set the session state to input value
submit = st.button("Submit") #set submit


if "submitted" not in st.session_state: #set the session state to be False
    st.session_state["submitted"] = False

if submit: #if the submit button is pressed, do this stuff.
    st.session_state["submitted"] = True #set the session state to be True
    st.session_state["my_input"] = my_input #set the session state to be the user input
    getToFlask(my_input)   
    # url = "http://localhost:8501/GeneratedBook"
    # webbrowser.open_new_tab(url)



# exec(open("testoutput.py").read()) #execute the GeneratedStorybook.py file

#MAKE THIS CHECK IF BUCKET HAS ANYTHING IN IT, BEFORE INSTRUCTING TO GO TO STORY TAB!




# def getToFlask(prompt):
#     BASE = "http://34.172.48.39:5000/"
#     # print("this is the passed prompt:",prompt)
#     frontEndPrompt = prompt
#     response = requests.get(BASE + "book/"+ frontEndPrompt)
#     # response = requests.get(BASE + prompt)

#     if (response.status_code == 200):
#         print("The request was a success!")
#     # Code here will only run if the request is successful
#     elif (response.status_code == 404):
#         print("Result not found!")


# getToFlask(st.session_state["my_input"])    

imagePrompts = {}


def list_blobs_with_prefix( ):
# def list_blobs_with_prefix( prefix ):
#     credentials = service_account.Credentials.from_service_account_info( 
#     st.secrets["GOOGLE_APPLICATION_CREDENTIALS"] #change to secrets, this lives in the "secrets.toml" file under ".streamlit" directory
# )
   
    credentials = service_account.Credentials.from_service_account_info( 
    st.secrets["gcp_service_account"] #change to secrets, this lives in the "secrets.toml" file under ".streamlit" directory
)
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.get_bucket("et-test-bucket")


    blobs = bucket.list_blobs()
    # blobs = bucket.list_blobs(prefix=prefix)

    print('Blobs:', blobs)


    for blob in blobs:
        
        if blob.metadata['text'] in imagePrompts.values():
            print("already in collection")
        elif len(imagePrompts) >= 5:
            print("collection full")
        else:
            imagePrompts.update({blob.name: blob.metadata['text']})
            # imagePrompts[blob.name] = blob.metadata['prompt']
            print("imagePrompts",imagePrompts)
            print("imagePrompts.values()",imagePrompts.values())
            st.write(blob.metadata['text']) 
            st.image(blob.download_as_bytes())


# ###########################`###############################

def subscriberz():
    # credentials_path = '/Users/thomas.nguyen/Desktop/streamlit/.streamlit/key.json'
    # os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path
    # os.environ['GOOGLE_APPLICATION_CREDENTIALS']
    credentials = service_account.Credentials.from_service_account_info( 
    st.secrets["GOOGLE_APPLICATION_CREDENTIALS"] #change to secrets, this lives in the "secrets.toml" file under ".streamlit" directory
)
   
#     credentials = service_account.Credentials.from_service_account_info( 
#     st.secrets["gcp_service_account"] #change to secrets, this lives in the "secrets.toml" file under ".streamlit" directory
# )

    timeout = 10

    subscriber = pubsub_v1.SubscriberClient(credentials=credentials)
    subscription_path = 'projects/acto-su-1/subscriptions/bucket-updates'

# streamlit run homepage.py
    def callback(message):

        print("callback ran")
        message.ack()

    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print(f'Listening for messages on {subscription_path}')



    with subscriber:                                                # wrap subscriber in a 'with' block to automatically call close() when done
        try:
            streaming_pull_future.result(timeout=timeout)
        # streaming_pull_future.result()                          # going without a timeout will wait & block indefinitely

        except TimeoutError:
            streaming_pull_future.cancel()
            list_blobs_with_prefix()
            # list_blobs_with_prefix("results/")
            streaming_pull_future.result() 
            print("this is the dictionary at the end of a loop",imagePrompts)
            print("this is the end of the subscriber")
            if len(imagePrompts) >= 5:
                yoda.empty()
                # placeholder.empty()
                placeholder.text("Your book is ready SADAIAN!!")
                st.session_state["finished"] = True
                navFinishedBook()
                streaming_pull_future.cancel()
                st.stop()
            else:
                placeholder.text("Your book is still generating.. patience young padawan")
                subscriberz()

if st.session_state["submitted"] == True:
    placeholder = st.empty()
    with placeholder.container():
        st.write("Generating your story... ")
        my_bar = st.progress(0)

        for percent_complete in range(100):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1)
        time.sleep(5)
    placeholder.empty()
    yoda = st.empty()
    with yoda.container():
        st_lottie( #create a lottie animation
        lottie_yoda,
        height=250,
        width=250,
        key="yoda",
        )
    subscriberz()








