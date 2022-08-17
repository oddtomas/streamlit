# Streamlit book generator front end
This is the repo for the front-end component of the SADA-U/R&D team Baby Book generator app.

## Summary
The front-end captures a users story prompt via an input field which saves the prompt as a state variable which is then passed to the flask back-end server as a parameter in a GET request to the back-end API endpoint which kicks off our back-end AI text and image generators. Using Google Cloud PubSub, a relationship was created between this front end and our Google Cloud storage bucket. PubSub listens for changes in that bucket, in the form of AI generated images that have our AI generated story texts attached as metadata. Once a change is recognized, a callback is triggered for the front-end to go look into our Google Cloud storage bucket and display that item as well as save it locally to be used. The stored items are reformatted to acceptable pdf text and images to be saved if desired. 

## Installation Requirements
- Install modules
```
pip install google-cloud-storage
pip install streamlit_lottie
pip install google-auth
pip install google-cloud-storage
pip install streamlit
pip install google-cloud-pubsub
pip install fpdf
```
- Setting up PubSub to receive notification for your Google Cloud storage bucket in the cloud shell
```
gsutil mb gs://BUCKET_NAME
gcloud pubsub topics create TOPIC_NAME
gcloud pubsub subscriptions create SUBSCRIPTION_NAME
gsutil notification create -f json -t <TOPIC_NAME> gs://<BUCKET_NAME>

```
## special setup considerations
Streamlit manages keys via .toml files, if your keys are in json format they will have to be converted and placed in your .streamlit/secrets.toml file. If  you're using Streamlit to also deploy your app, these keys must be included in the app settings via their secrets manager because the keys would/should not be pushed to github. 
