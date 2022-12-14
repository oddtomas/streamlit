import streamlit as st
from google.oauth2 import service_account
from google.cloud import storage
import time
from fpdf import FPDF

imagePrompts = {}
actualImages = []
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
    with open("book.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(label="Download PDF", 
            data=PDFbyte,
            file_name="SADA R&D Babybook.pdf",
            mime='application/octet-stream')
# st.markdown("""

# <style>


#  .css-10xlvwk.e1fqkh3o3 {
#         display: none;
#     }

# </style>

# """, unsafe_allow_html=True)

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
            print("blob", blob.name)
            actualImages.append(blob)
            imagePrompts.update({blob.name:blob.metadata['text']})
            # print("imagePrompts",imagePrompts)
            # blob.download_to_filename('/Users/thomas.nguyen/Desktop/streamlit/test{0}.jpg'.format(ii))
            blob.download_to_filename('image{0}.jpg'.format(ii))
            ii+=1
            # list_blobs_with_prefix()
            #print everything inside a blob
            # st.write(blob.metadata['text']) 
            # print("actualImages",actualImages)
            st.markdown(card(blob.metadata['text']), unsafe_allow_html=True)
            st.image(blob.download_as_bytes())
            

list_blobs_with_prefix()

savePDF()







