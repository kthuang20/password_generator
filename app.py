### import necessary packages
import streamlit as st
from source.generate_password import *

### configure settings of page
st.set_page_config(
    page_title="Password Generator",
    page_icon="🔑",
    layout="centered")

### add title
st.title("Password Generator")

### create a session state to remember if text is valid for generating password
if "is_valid" not in st.session_state:
    st.session_state["is_valid"] = False

### ask and store the text the user wants to be converted
text = st.text_input("Enter a text with 12+ characters that you want to generate a password with:", )
### add button
st.button("Generate Password", args=[text])

### if user inputted some text,
if text:
    ## check text is valid for generating password
    st.session_state["is_valid"] = check_text(text)

    ## if text is valid,
    if st.session_state["is_valid"]:
        # generate password
        password = gen_password(text.title())
        # show the user the generated password
        st.text(f"Your generated password is {password}")
    ## otherwise, if the text is invalid,
    else:
        # have the user keep trying until valid
        st.write("Please enter different text with at least 12 characters")

