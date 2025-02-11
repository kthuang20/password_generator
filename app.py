### import necessary packages
import streamlit as st
from source.generate_password import *

### create a session state to remember if text is valid for generating password
if "is_valid" not in st.session_state:
    st.session_state["is_valid"] = False

### handle button click
def handle_click(click_button):
    st.session_state["click_button"] = True

### ask and store the text the user wants to be converted
text = st.text_input("Enter a text with 12+ characters that you want to generate a password with:", )
### add button
st.button("Generate Password", on_click=handle_click, args=[text])

### check text is valid for generating password
st.session_state["is_valid"] = check_text(text)
### if text is valid,
if st.session_state["is_valid"]:
    ## generate password
    password = gen_password(text.title())
    ## show the user the generated password
    st.write("Your generated password is ", password)
    st.session_state["click_button"] = False
else:
    ## if the text is invalid, have the user keep trying until valid
    st.write("Please enter a different text with at least 12 characters")