import streamlit as st
from glob import glob
import json
import os

def load_json_file(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data

image_data = load_json_file("imagess.json")
# print(image_data)

st.title("Vaibhav POC")

# Path to your images folder
image_folder_path = "./images"

# List all files in the folder
# image_files = os.listdir(image_folder_path)



prompt = st.chat_input("Say something")

if prompt:
    for i in image_data:
        if i["clip_topic"] == prompt:
            image_path = os.path.join(image_folder_path, i["image"])
            st.image(image_path, caption=i["clip_topic"])
            break
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")

# Display each image
# for image_file in image_files:
#     image_path = os.path.join(image_folder_path, image_file)
#     st.image(image_path, caption=image_file)


# for image of glob("image"):
#     st.image(image,caption="test")

# uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
#     # To read file as bytes:
#     bytes_data = uploaded_file.getvalue()
#     st.write(bytes_data)

# with st.chat_message("user"):
#     st.write("Hello 👋")