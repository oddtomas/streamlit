import streamlit as st
from google.oauth2 import service_account
from google.cloud import storage


imagePrompts = {}

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
            st.write(blob.metadata['text']) 
            st.image(blob.download_as_bytes())

# list_blobs_with_prefix("results/")
list_blobs_with_prefix()