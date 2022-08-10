import streamlit as st
from google.oauth2 import service_account
from google.cloud import storage
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

lottie_hello = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_q77jpumk.json") 
# lottie_coding = load_lottiefile("sprinkle.json")

# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Create API client.
credentials = service_account.Credentials.from_service_account_info( 
    st.secrets["gcp_service_account"] #change to secrets, this lives in the "secrets.toml" file under ".streamlit" directory
)
client = storage.Client(credentials=credentials)  #change to credentials
bucket = client.get_bucket("et-test-bucket") #change to bucket name

st.set_page_config(page_title="SADA R&D Book Generator", page_icon="🤖") #change browser tab title


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


# def write_to_file(text): #takes the user entered input and writes it to a file when called below
#     with open("prompt.txt", "w") as f: #file named prompt.txt
#         f.write(text)

# def upload_file(file_path): #upload the file to GCP, file path is the "prompt.txt" file that is passed when the function is called
#     blob = bucket.blob(file_path) 
#     blob.upload_from_filename(file_path)

def postToFlask(prompt):
    # prompt = "what is broken"
# response = requests.get("http://127.0.0.1:5000/api/get-json")
    response = requests.post('http://127.0.0.1:5000/api/get-json', data = prompt)
    if (response.status_code == 200):
        print("The request was a success!")
    # Code here will only run if the request is successful
    elif (response.status_code == 404):
        print("Result not found!")
# print(response)
    print(response.json())

if "submitted" not in st.session_state: #set the session state to be False
    st.session_state["submitted"] = False

if submit: #if the submit button is pressed, do this stuff.
    st.session_state["submitted"] = True #set the session state to be True
    st.session_state["my_input"] = my_input #set the session state to be the user input
    st.write("Generating your story... go to the story tab!") #write to the streamlit page that the story is being generated
    postToFlask(my_input) #call the postToFlask function and pass the user input as the parameter
    # write_to_file(st.session_state["my_input"]) #write the user input to a file
    # upload_file("prompt.txt") #upload the file to GCP
    # exec(open("testoutput.py").read()) #execute the GeneratedStorybook.py file

#MAKE THIS CHECK IF BUCKET HAS ANYTHING IN IT, BEFORE INSTRUCTING TO GO TO STORY TAB!




#GET our test server
# URL = "http://34.172.48.39:5000/hello"
# location = "delhi technological university"
# PARAMS = {'address':location}
# r = requests.get(url = URL, params = PARAMS)
# data = r.json()
# print(data)




