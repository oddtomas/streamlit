import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests
import webbrowser
from google.oauth2 import service_account
from google.cloud import storage
from google.cloud import pubsub_v1
import os
from concurrent.futures import TimeoutError
import time
from fpdf import FPDF
from email.message import EmailMessage
import ssl
import smtplib
# from pages.SavedBook import savePDF



st.set_page_config(page_title="SADA R&D Book Generator", page_icon="🤖") #change browser tab title

def sendEmail():    
    email_sender = 'SADAUCOHORT6@gmail.com' 
    email_password = 'cubfalohweraqgyi' 
    email_receiver = 'thomas.nguyen@sada.com' 
    

    subject = 'Your book is done!'
    body = """
    The generator just finished creating your custom book, go back to the site to check it out or download it!
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())


def savePDF():
    text1 = imagePrompts['IMAGE_n00.jpg'].encode('latin-1', 'replace').decode('latin-1') #exception for non latin-1 characters
    text2 = imagePrompts['IMAGE_n01.jpg'].encode('latin-1', 'replace').decode('latin-1')
    text3 = imagePrompts['IMAGE_n02.jpg'].encode('latin-1', 'replace').decode('latin-1')
    text4 = imagePrompts['IMAGE_n03.jpg'].encode('latin-1', 'replace').decode('latin-1')
    text5 = imagePrompts['IMAGE_n04.jpg'].encode('latin-1', 'replace').decode('latin-1')
    text6 = imagePrompts['IMAGE_n05.jpg'].encode('latin-1', 'replace').decode('latin-1')
    text7 = imagePrompts['IMAGE_n06.jpg'].encode('latin-1', 'replace').decode('latin-1')
    text8 = imagePrompts['IMAGE_n07.jpg'].encode('latin-1', 'replace').decode('latin-1')
    text9 = imagePrompts['IMAGE_n08.jpg'].encode('latin-1', 'replace').decode('latin-1')
    text10 = imagePrompts['IMAGE_n09.jpg'].encode('latin-1', 'replace').decode('latin-1')
    # text11 = imagePrompts['IMAGE_n10.jpg'].encode('latin-1', 'replace').decode('latin-1')

    image1 = 'image0.jpg'
    image2 = 'image1.jpg'
    image3 = 'image2.jpg'
    image4 = 'image3.jpg'
    image5 = 'image4.jpg'
    image6 = 'image5.jpg'
    image7 = 'image6.jpg'
    image8 = 'image7.jpg'
    image9 = 'image8.jpg'
    image10 = 'image9.jpg'
    # image11 = 'image10.jpg'

    pdf = FPDF()
    pdf.set_auto_page_break(True, margin = 30)
    pdf.add_page()
    pdf.set_font('Arial', 'B', 15)
    pdf.cell(55)
    pdf.set_line_width(1)
    pdf.cell(75, 10, 'SADA R&D Book Generator', 1, 0, 'C')
    pdf.ln(20)
    pdf.set_font('Arial', 'I', 12)
    pdf.set_text_color(0, 0, 0)
    # pdf.image('sada.jpeg', w = 20, h = 20)
    pdf.multi_cell(0, 5, text1, align='C')
    pdf.cell(45)
    pdf.image(image1,w=100,h=100)
    # pdf.ln(10)
    pdf.write(4,'-------------------------------------------------------------------------------------------------------------------------------------')
    pdf.ln()
    pdf.multi_cell(0, 5, text2, align='C')
    pdf.cell(45)
    pdf.image(image2,w=100,h=100)
    pdf.add_page()    
    #####################################
    pdf.ln(15)
    pdf.multi_cell(0, 5, text3, align='C')
    pdf.cell(45)
    pdf.image(image3,w=100,h=100)
    pdf.ln(5)
    pdf.write(4,'-------------------------------------------------------------------------------------------------------------------------------------')
    pdf.ln(5)
    pdf.multi_cell(0, 5, text4, align='C')
    pdf.cell(45)
    pdf.image(image4,w=100,h=100)
    pdf.add_page()
    #####################################
    pdf.ln(15)
    pdf.multi_cell(0, 5, text5, align='C')
    pdf.cell(45)
    pdf.image(image5,w=100,h=100)
    pdf.ln(5)
    pdf.write(4,'-------------------------------------------------------------------------------------------------------------------------------------')
    pdf.ln(5)
    pdf.multi_cell(0, 5, text6, align='C')
    pdf.cell(45)
    pdf.image(image6,w=100,h=100)
    pdf.add_page()
    #####################################
    pdf.ln(15)
    pdf.multi_cell(0, 5, text7, align='C')
    pdf.cell(45)
    pdf.image(image7,w=100,h=100)
    pdf.ln(5)
    pdf.write(4,'-------------------------------------------------------------------------------------------------------------------------------------')
    pdf.ln(5)
    pdf.multi_cell(0, 5, text8, align='C')
    pdf.cell(45)
    pdf.image(image8,w=100,h=100)
    pdf.add_page()
    #####################################
    pdf.ln(15)
    pdf.multi_cell(0, 5, text9, align='C')
    pdf.cell(45)
    pdf.image(image9,w=100,h=100)
    pdf.ln(5)
    pdf.write(4,'-------------------------------------------------------------------------------------------------------------------------------------')
    pdf.ln(5)
    pdf.multi_cell(0, 5, text10, align='C')
    pdf.cell(45)
    pdf.image(image10,w=100,h=100)   
    pdf.output('book.pdf')
    #############################

def load_lottiefile(filepath: str): #load the lottie file from the filepath
    with open(filepath, "r") as f:
        return json.load(f)

lottie_gears = load_lottiefile("lottie/gears.json")
lottie_yoda = load_lottiefile("lottie/yoda.json")


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


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def card(text): #create a card with the id, text and image
    return f"""
    <div class="card" style="width: 10 rem;">
    <div class="card-body">
        <p class="card-text">{text}</p>
    </div>
    </div>
    """

st.title("SADA R&D Book Generator") #change page title

# 

if "my_input" not in st.session_state: #set the session state to be empty
    st.session_state["my_input"] = ""

st.write("This is a GCP project utilizing EleutherAI’s  GPT-J-6B and Imagen-pytorch Real-ESRGAN to generate text and images to form your own custom book.")

gears = st.empty()
with gears.container():
    st_lottie( #create a lottie animation
    lottie_gears,
    height=500,
    width=500,
    )

    st.write("Please enter the first sentence of your children's book.")
    my_input = st.text_input("Example: \"The rainbow unicorn and fluffy giraffe went hopping along the clouds.\"", st.session_state["my_input"]) #change prompt to be a text input and set the session state to input value
    submit = st.button("Submit") #set submit


if "submitted" not in st.session_state: #set the session state to be False
    st.session_state["submitted"] = False

if submit: #if the submit button is pressed, do this stuff.
    st.session_state["submitted"] = True #set the session state to be True
    st.session_state["my_input"] = my_input #set the session state to be the user input
    getToFlask(my_input)
    gears.empty() #empty the lottie animation   


# exec(open("testoutput.py").read()) #execute the GeneratedStorybook.py file
  

imagePrompts = {}
actualImages = []


def list_blobs_with_prefix( ):
# def list_blobs_with_prefix( prefix ):   
    credentials = service_account.Credentials.from_service_account_info( 
    st.secrets["gcp_service_account"] #change to secrets, this lives in the "secrets.toml" file under ".streamlit" directory
)
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.get_bucket("et-test-bucket")


    blobs = bucket.list_blobs()
    # blobs = bucket.list_blobs(prefix=prefix)

    print('Blobs:', blobs)
    ii = 0


    for blob in blobs:
        
        if blob.metadata['text'] in imagePrompts.values() and blob.name in imagePrompts.keys():
            print("already in collection")
        elif len(imagePrompts) >= 10:
            print("collection full")
        else:
            actualImages.append(blob)
            imagePrompts.update({blob.name: blob.metadata['text']})
            blob.download_to_filename('image{0}.jpg'.format(ii))
            ii+=1
            st.markdown(card(blob.metadata['text']), unsafe_allow_html=True)
            st.image(blob.download_as_bytes())


# ###########################`###############################

def subscriberz():
    credentials = service_account.Credentials.from_service_account_info( 
    st.secrets["GOOGLE_APPLICATION_CREDENTIALS"] #change to secrets, this lives in the "secrets.toml" file under ".streamlit" directory
)
   

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
            print("actualImages array at the end",actualImages)
            print("this is the end of the subscriber")
            if len(imagePrompts) >= 10:
                yoda.empty()
                # placeholder.empty()
                placeholder.text("Your book is ready SADAIAN!!")
                sendEmail()
                savePDF()
                with open("book.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                st.download_button(label="Download PDF", 
                    data=PDFbyte,
                    file_name="SADA R&D Babybook.pdf",
                    mime='application/octet-stream')
                streaming_pull_future.cancel()
                st.stop()
                
            else:
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
    placeholder.text("Your book is still generating.. patience young padawan")
    yoda = st.empty()
    with yoda.container():
        st_lottie( #create a lottie animation
        lottie_yoda,
        height=250,
        width=250,
        key="yoda",
        )
    
    subscriberz()








