# Getting Started
* You need to install google cloud sdk which you can do so by following this link: **https://cloud.google.com/sdk/docs/install#deb**
* Once you do that, you also need to create a google cloud service account, and get the .json key.
* I will not be uploading my .json key for **security reasons** 
* Here is what you will be looking for: 
```
GOOGLE_APPLICATION_CREDENTIALS=path/to/key
```
* Then you need to run this:
```
python3 -m venv env
source env/bin/activate
```

# Libraries:
* *https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader*

# Creating the variable
* You need to set the env variable so it points to your .json key
* **Sources:**
  - *https://cloud.google.com/docs/authentication/application-default-credentials#GAC*
