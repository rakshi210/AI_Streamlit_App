import streamlit as st

st.set_page_config(page_title="AI Streamlit App", page_icon="🤖")

st.title("🤖 Welcome to My First Streamlit App")
st.write("This application is deployed live using Streamlit Community Cloud.")

# Input form
with st.form(key="user_form"):
    user_name = st.text_input("Enter your name:")
    submit_button = st.form_submit_button(label="Submit")

# Output display
if submit_button:
    if user_name.strip():
        st.success(f"Hello, **{user_name}**! Your app is running successfully.")
    else:
        st.warning("Please enter a name before clicking submit.")