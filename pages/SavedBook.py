import streamlit as st
from google.oauth2 import service_account
from google.cloud import storage


imagePrompts = {}
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

    for blob in blobs:

        if blob.metadata['text'] in imagePrompts.values():
            print("already in collection")
        elif len(imagePrompts) >= 11:
            print("collection full")
        else:
            imagePrompts.update({blob.name:blob.metadata['text']})
            print("imagePrompts",imagePrompts)
            # st.write(blob.metadata['text']) 
            st.markdown(card(blob.metadata['text']), unsafe_allow_html=True)
            st.image(blob.download_as_bytes())
            # st.markdown(card(blob.download_as_bytes()), unsafe_allow_html=True)


# list_blobs_with_prefix("results/")
list_blobs_with_prefix()

