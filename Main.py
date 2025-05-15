import streamlit as st
import requests

def get_random_dog_image():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["message"]
    else:
        return None

def main():
    st.title("🐶 Random Dog Image Viewer")

    if st.button("Show me a dog!"):
        img_url = get_random_dog_image()
        if img_url:
            st.image(img_url, width=400)
        else:
            st.error("Oops! Could not fetch a dog image.")

    else:
        st.write("Click the button to see a random dog image!")

if __name__ == "__main__":
    main()
