# Streamlit book generator front end
This is the repo for the front-end component of the SADA-U/R&D team Baby Book generator app.

#Summary
The front-end captures a users story prompt via an input field which saves the prompt as a state variable which is then passed to the flask back-end server as a parameter in a GET request to the back-end API endpoint which kicks off our back-end AI text and image generators. Using Google Cloud PubSub, a relationship was created between this front end and our Google Cloud storage bucket. PubSub listens for changes in that bucket, in the form of AI generated images that have our AI generated story texts attached as metadata. Once a change is recognized, a callback is triggered for the front-end to go look into our Google Cloud storage bucket and display that item as well as save it locally to be used. The stored items are reformatted to acceptable pdf text and images to be saved if desired. 

#Installation Requirements
