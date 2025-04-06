import streamlit as st
import random
import string


def generate_password(lenght,use_digits,use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(lenght))
    return password

st.title("Password Generator")

lenght = st.slider("Select the lenght of the password", min_value=4, max_value=32, value=12) 

use_digits = st.checkbox("Include digits")
use_special = st.checkbox("Include special characters")

if st.button("Generate Password"):
    password = generate_password(lenght,use_digits,use_special)
    st.write(f"Generated Password: `{password}`")

st.write("-----------------------------")

st.write("Build with ❤️ by [Amna Shah]")
    