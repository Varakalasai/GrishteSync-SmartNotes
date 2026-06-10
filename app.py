# Created with GrishteSync
# https://suryasticsai.github.io/GrishteSync
# Suryasticsai | suryasticsai@gmail.com
import streamlit as st
import sessionstate
from PIL import Image

st.title("MagicNotes")

# Load logo
logo = Image.open("https://i.ibb.co/RGmb4FKk/1781072041102.png")

# Session state
if 'notes' not in st.session_state:
    st.session_state.notes = {}

# Dark mode toggle
dark_mode = st.checkbox("Dark Mode")
if dark_mode:
    st.markdown("<style>body {background-color: #333; color: #fff;}</style>", unsafe_allow_html=True)

# Search bar
search_query = st.text_input("Search Notes")

# Function to save note
def save_note(title, content):
    st.session_state.notes[title] = content

# Function to delete note
def delete_note(title):
    if title in st.session_state.notes:
        del st.session_state.notes[title]

# Save note form
with st.form("save_note"):
    title = st.text_input("Note Title")
    content = st.text_area("Note Content")
    if st.form_submit_button("Save Note"):
        save_note(title, content)

# Display notes
notes_to_display = {title: content for title, content in st.session_state.notes.items() if search_query.lower() in title.lower() or search_query.lower() in content.lower()}
for title, content in notes_to_display.items():
    with st.expander(title):
        st.write(content)
        if st.button("Delete Note", key=title):
            delete_note(title)

# Footer
st.markdown("<p style='text-align: center;'>Made with GrishteSync | Suryasticsai | suryasticsai@gmail.com</p>", unsafe_allow_html=True)