import streamlit as st
import time
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


def write_to_file(text): #takes the user entered input and writes it to a file when called below
    with open("prompt.txt", "w") as f: #file named prompt.txt
        f.write(text)

def upload_file(file_path): #upload the file to GCP, file path is the "prompt.txt" file that is passed when the function is called
    blob = bucket.blob(file_path) 
    blob.upload_from_filename(file_path)


if "submitted" not in st.session_state: #set the session state to be False
    st.session_state["submitted"] = False

if submit: #if the submit button is pressed, do this stuff.
    st.session_state["submitted"] = True #set the session state to be True
    st.session_state["my_input"] = my_input #set the session state to be the user input
    write_to_file(st.session_state["my_input"]) #write the user input to a file
    upload_file("prompt.txt") #upload the file to GCP


# exec(open("GeneratedStorybook.py").read()) #execute the GeneratedStorybook.py file

if "filled" not in st.session_state: #set the session state to be False
    st.session_state["filled"] = False

def filled():        
    if len(d) == 20: #if the dictionary has 20 keys, then the generators are done (10 text and 10 images)
        st.session_state["filled"] = True
        # print(len(d))

blobs = bucket.list_blobs() #list all the blobs in the bucket
collection = [] #create a collection to store the blobs
d = {} #create a dictionary to store the blobs

def list_blobs():

    for blob in blobs: #for each blob in the bucket
        if "text_" in blob.name: #if the blob name contains "text_"/ *change this to metadata*
            # print(blob.name)
            test_text = blob.download_as_string().decode("utf-8") 
            collection.append(test_text)

        if "image_" in blob.name: #if the blob name contains "image_"/ *change this to metadata*
            # print(blob)
            image = blob.download_as_bytes()
            collection.append(image)

list_blobs() #call the list_blobs function to filter through the bucket and store the blobs in the collection

d = {'image1': collection[0], 'text1': collection[10], 'image2': collection[1], 'text2': collection[11], 'image3': collection[2], 'text3': collection[12], 'image4': collection[3], 'text4': collection[13], 'image5': collection[4], 'text5': collection[14], 'image6': collection[5], 'text6': collection[15], 'image7': collection[6], 'text7': collection[16], 'image8': collection[7], 'text8': collection[17], 'image9': collection[8], 'text9': collection[18], 'image10': collection[9], 'text10': collection[19] } #create a dictionary to store the blobs

filled() #call the filled function to check if the dictionary has 20 keys and set the session state to be True


def card(text): #create a card with the id, text and image
    return f"""
    <div class="card" style="width: 18rem;">
    <div class="card-body">
        <p class="card-text">{text}</p>
    </div>
    </div>
    """

def output():
    if st.session_state["submitted"] and st.session_state["filled"]: #if the user has submitted and the dictionary has 20 keys, then do this stuff
        st.markdown("""
<style>
.big-font {
    font-size:50px !important;
}
</style>
""", unsafe_allow_html=True)
        st.markdown('<p class="big-font">Here&#8217s your story!!</p>', unsafe_allow_html=True)
        # st.write(d['text1'])
        st.markdown(card(d['text1']), unsafe_allow_html=True)
        st.image(d['image1'])
        # st.write(d['text2'])
        st.markdown(card(d['text2']), unsafe_allow_html=True)
        st.image(d['image2'])
        # st.write(d['text3'])
        st.markdown(card(d['text3']), unsafe_allow_html=True)
        st.image(d['image3'])
        # st.write(d['text4'])
        st.markdown(card(d['text4']), unsafe_allow_html=True)
        st.image(d['image4'])
        # st.write(d['text5'])
        st.markdown(card(d['text5']), unsafe_allow_html=True)
        st.image(d['image5'])
        # st.write(d['text6'])
        st.markdown(card(d['text6']), unsafe_allow_html=True)
        st.image(d['image6'])
        # st.write(d['text7'])
        st.markdown(card(d['text7']), unsafe_allow_html=True)
        st.image(d['image7'])
        # st.write(d['text8'])
        st.markdown(card(d['text7']), unsafe_allow_html=True)
        st.image(d['image8'])
        # st.write(d['text9'])
        st.markdown(card(d['text9']), unsafe_allow_html=True)
        st.image(d['image9'])
        # st.write(d['text10'])
        st.markdown(card(d['text10']), unsafe_allow_html=True)
        st.image(d['image10'])
    else:
        st.write("Nothing to see here......... yet! Submit your prompt to generate your book!")

def checker(): #check if the user has submitted and the dictionary has 20 keys
    if st.session_state["submitted"] and st.session_state["filled"]:
        output() #if the user has submitted and the dictionary has 20 keys, then call output to write the story
    else:
        with st.empty(): #empty the page
            for seconds in range(10): 
                st.write(f"⏳ generating....")
                time.sleep(20)
                st.empty()
                print("running2")
        checker() #if the user has not submitted or the dictionary has not 20 keys, then call checker to check again



if st.session_state["submitted"]: #if the user has submitted, then call checker to write the story
    checker() #call checker to write the story recursively?



